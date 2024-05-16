from bs4 import BeautifulSoup # парсер
import requests # HTTP запросы
import re # регулярки
import os # для получения пути к исполняемому файлу 
import pandas as pd # DataFrame в которой сохраняются все данные 

# Класс скрапера
class ZabGuScraper:
    """Класс для запросов на сайт и получение списка новостей пустём парсинга данных сайта"""
    #Конструктор
    def __init__(self) -> None:
        """Класс скрапера для сайта ЗабГу \n
        Методы:\n
        _init_(self) - конструктор, создаёт переменные для обработки данных при парсинге, ссылки, путь сохранения файла, флаги и создаёт или открывает DataFrame \n
        update_df(self, content) - получает HTML код страницы, после парсинга данные добавляются в DataFrame\n
        request(urladr) - делает запрос сайта и возвращает HTML код страницы\n
        load_page(self, num) - получает num число страниц новостей которые будут загруженны в DataFrame\n
        start_loop(self) - консольный интерфейс программы\n
        """
        # Словарь для преобразования названия месяца в число
        self.month = {
            "ЯНВАРЬ"    : "01",
            "ФЕВРАЛЬ"   : "02",
            "МАРТ"      : "03",
            "АПРЕЛЬ"    : "04",
            "МАЯ"       : "05",
            "ИЮНЬ"      : "06",
            "ИЮЛЬ"      : "07",
            "АВГУСТ"    : "08",
            "СЕНТЯБРЬ"  : "09",
            "ОКТЯБРЬ"   : "10",
            "НОЯБРЬ"    : "11",
            "ДЕКАБРЬ"   : "12"
            }
        # Строка с месяцами для определения сокращённого названия месяца посредством регулярных выражений
        self.month_str = ' '.join(map(str,list(self.month)))

        # Путь к дерективе
        self.file_path = os.path.dirname(os.path.abspath(__file__)) 

        # Флаг сохранение, при добавлении новых данных = 1
        self.save_flag = 0

        # Ссылка на следующую страницу чтении сайта
        self.next_page = ""
        
        # Начальная ссылка на страницу новостей
        self.page = "https://zabgu.ru//php/news.php?category=1&page=1"

        # получение из файла dataframe
        if os.path.exists(self.file_path + '/df.csv'):
            print("Файл есть\nЧтение файла...")
            self.df = pd.read_csv(self.file_path + '/df.csv', index_col=0)
        #если файл не создан то создаст с именами солбцов
        else:
            print("Файа нету\nСоздание файла...")
            self.df = pd.DataFrame( columns=['date', 'mark', 'news', 'link', 'file'])
            self.df.to_csv(self.file_path + '/df.csv')

    # Деструктор
    def __del__(self):
        """Сохраняет данные с уничтожением объекта"""
        if self.save_flag == 1:
            print("Сохранение")
            self.df.to_csv(self.file_path + '/df.csv')



    # Добавляет новые данные
    def update_df(self, content):
        """Добовляет новые данные в DataFrame"""
        soup = BeautifulSoup(content, 'lxml') # Парсер
        ad = soup.find_all('div', class_='news_line')

        pattern = "((preview_new)(_end)?)" # Регулярное выражение для получения всех новостей в строке

        frame = [] # Список добавляемых файлов
        for i in range(len(ad)):
            ad1 = ad[i].find_all(class_ = re.compile(pattern))
            for j in range(len(ad1)):
                #============================================
                #               ПОЛУЧЕНИЕ ДАТЫ
                ad2 = ad1[j].find('p', class_='day')

                day = re.search("[\d]+",ad2.text).group()

                pat = (re.search("[\D]+",ad2.text).group()).upper() + "[А-Я]*"
                mon = self.month[re.search(pat, self.month_str).group()]
                
                year = ad1[j].find('p', class_='yearInTileNewsOnPageWithAllNews').text

                date = day + "-" + mon + "-" + year
                #============================================
                #               ПОЛУЧЕНИЕ ЗАГОЛОВКА НОВОСТИ
                news = ad1[j].find('div', class_='headline').text
                #============================================
                #               ПРОВЕРКА ПО ДАТЕ И ЗАГОЛОВКУ НА ПОВТОРЕНИЕ НОВОСТИ
                dd = self.df.loc[self.df['news'].isin([news])]
                dd = dd.loc[self.df['date'].isin([date])]
                if dd.empty == False:
                    print("Такие данные уже есть")
                    continue
                print("Обнаруженны новые данные")
                self.save_flag = 1
                #============================================
                #               ПОЛУЧЕНИЕ МЕТОК
                mark_list = list()
                ad2 = ad1[j].find_all('a', class_='marker_news')
                for k in range(len(ad2)):
                    mark_list.append(ad2[k].text)   
                #============================================
                #               ПОЛУЧЕНИЕ ССЫЛКИ НА НОВОСТЬ
                link = 'https://zabgu.ru' + ad1[j].find('a').get('href')
                #============================================

                #============================================
                #       Сохранение текста новости
                text = self.request(link)
                soup2 = BeautifulSoup(text, 'lxml')
                ad3 = soup2.find('div', id='full_text')
                ad3.find('div', class_="date").decompose() # удаление лишних тегов
                ad3.find('div', class_="markersContainer openNewsMarkersContainer").decompose()
                file = ad3.text
                #============================================

                # Список добавляемых данных
                pddata = [date, mark_list, news, link, file]
                frame.append(pddata)

        #============================================
        #           Получение номера страницы 
        #           и создание ссылки следующей
        pag = soup.find('div', id='pagination_wrapper')
        l = int(pag.find('div', id='current_pagination_pos').text)
        l = l+1

        p = pag.find("a",string = l)
        if p != None:
            self.next_page = 'https://zabgu.ru/' + p.get('href')[2:]
        else:
            self.next_page = "None"
        #============================================

        # Добавление всех новых данных в DataFrame
        for i in range(len(frame)):
            self.df.loc[len(self.df.index)] = frame[i]


    # получение ответа (объект типа Response) на HTTP запрос
    @staticmethod
    def request(urladr):
        """Requests get сайта, возвращает текст HTML"""
        res = requests.get(urladr)        
        return res.text     # текстовое содержимое страницы

    def load_page(self, num):
        """Загружает num страниц в DataFrame"""
        # Первая страница
        content = self.request(self.page)
        self.update_df(self, content)

        # Сколько страниц новостей будет прочитанно с сайта
        for i in range(num):
            content = self.request(self.next_page)
            self.update_df(self, content)

    # Цикл с вывоом заголовков новостей, их даты, тега и вывод всей новости
    def start_loop(self):
        """Консольный интерфейс"""
        while(True):
                print(f"====================")
                for i in range(len(self.df)):
                    df_date = self.df['date'].loc[i]
                    df_mark = self.df['mark'].loc[i]
                    df_news = self.df['news'].loc[i]

                    print(f"Новость №{i}")
                    print(f"Дата: {df_date}")
                    print(f"Теги: {df_mark}")
                    print(f"Заголовок: {df_news}")
                    print(f"====================")

                n = int(input("Введите номер новости: "))
                if not((n >= len(self.df)) or (n < 0)):
                    print(self.df['file'].loc[n])
                else:
                    break
                input("Конец новости")
                os.system('cls')
            

def main():
    scrap = ZabGuScraper() 
    scrap.load_page(0)
    scrap.start_loop()
    print(scrap.df)


if __name__ == '__main__':
    main()