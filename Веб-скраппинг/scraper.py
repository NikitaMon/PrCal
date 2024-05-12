from bs4 import BeautifulSoup # парсер
import requests # HTTP запросы
import re # регулярки
import codecs # Для избежания ошибок с кодировками текстового файла
import os
import pandas as pd 
import hashlib

class ZabGuScraper:
    def __init__(self, num) -> None:
        # Добавляет новые данные
        def update_df(self, content):
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
                    
                    # По умолчанию файла нету
                    file = "НЕТУ"

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
            

        # Считывает новости и сохраняет/загружает в/из файл(а)
        def file_df(self, id):
            # Если данных нету то сохранять ничего не нужно
            if (id >= len(self.df)) or (id < 0):
                return -1

            # Если файла нету значит надо зайти на сайт и считать
            if self.df['file'].loc[id] == "НЕТУ":
                print("         Создание файла...")
                
                df_link = self.df['link'].loc[id]    # Получает из DataFrame адрес на новость
                content = request(df_link)      # Запрос
                soup = BeautifulSoup(content, 'lxml')
                ad = soup.find('div', id='full_text')
                ad.find('div', class_="date").decompose() # удаление лишних тегов
                ad.find('div', class_="markersContainer openNewsMarkersContainer").decompose()

                tex = ad.find('strong').text # Получение заголовка

                hexfile = hashlib.sha256(tex.encode()).hexdigest() # Шифрование заголовка для названия файла
                #сохранение
                with open(self.file_path + "/" + hexfile + ".txt", "w", encoding="utf-8") as file:
                    file.write(ad.text)

                # назначение названия для файла в DataFrame
                self.df.at[id,'file'] = hexfile
                self.save_flag = 1
                print(ad.text)
                return 0
                
            print("         Открытие файла...")

            # Открытие файла
            path_f = self.df['file'].loc[id]
            file_r = codecs.open(self.file_path + "/" + path_f + ".txt", "r", "utf_8_sig" )
            content = file_r.read() 
            file_r.close()
            print(content)
            return 0

        # получение ответа (объект типа Response) на HTTP запрос
        def request(urladr):
            res = requests.get(urladr)        
            return res.text     # текстовое содержимое страницы
            

        #=============== INIT ===============
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
        self.file_path = os.path.dirname(os.path.abspath(__file__)) # Путь к дерективе
        self.save_flag = 0
        self.next_page = ""
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

        # Первая страница
        content = request(self.page)
        update_df(self, content)

        # Сколько страниц новостей будет прочитанно с сайта
        for i in range(num):
            content = request(self.next_page)
            update_df(self, content)

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
                    file_df(self, n)
                else:
                    break
                input("Конец новости")
                os.system('cls')
                
        if self.save_flag == 1:
            print("Сохранение")
            self.df.to_csv(self.file_path + '/df.csv')

    # Вывод содержимого DataFrame
    def pandas_print(self):
        print(self.df)


def main():
    scrap = ZabGuScraper(1) 
    scrap.pandas_print()

if __name__ == '__main__':
    main()