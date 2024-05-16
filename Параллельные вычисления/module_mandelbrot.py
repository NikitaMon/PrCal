import multiprocessing as mp
import time

import numpy as np
import matplotlib.pyplot as plt

from multiprocessing import shared_memory, Process

# 
def funk(p1,ip1,q1,iq1,max_iterations, infinity_border, shm_name, size1, size2):
    """Вычисление точек и сохранение их в общую память"""

    print("процесс запуск")
    # Получение доступа к общей памяти
    existing_shm = shared_memory.SharedMemory(name=shm_name)
    # Превращение пространства общей памяти в массив
    shared_array = np.ndarray((size1,size2), dtype=np.int64, buffer=existing_shm.buf)

    
    # точки которые расчитываются ip, iq
    for ip, p in zip(ip1, p1):
        for iq, q in zip(iq1, q1):
            # буквой j обозначается мнимая единица: чтобы Python понимал, что речь
            # идёт о комплексном числе, а не о переменной j, мы пишем 1j
            c = p + 1j * q
            z = 0
            for k in range(max_iterations):
                z = z ** 2 + c
                # Самая Главная Формула
                if abs(z) > infinity_border:
                    shared_array[ip,iq] = 1
                    break

    # Закрытие общей памяти
    existing_shm.close()

def mandelbrot(thread_num, ppoints, qpoints):
    """Выводит множество Мандельброта с колиичеством процессов thread_num"""
    pmin, pmax, qmin, qmax = -2.5, 1.5, -2, 2
    # пусть c = p + iq и p меняется в диапазоне от pmin до pmax,
    # а q меняется в диапазоне от qmin до qmax
    max_iterations = 300 # максимальное количество итераций
    infinity_border = 100 # если ушли на это расстояние, считаем, что ушли на бесконечность
    

    # Глубина прорисовки
    p = np.linspace(pmin, pmax, ppoints)
    q = np.linspace(qmin, qmax, qpoints)

    # Индексы для 'p' и 'q'
    ip = list(range(0, len(p)))
    iq = list(range(0, len(q)))

    # Разделение изображения на секции которые будут отправлены в поток для обработки
    # nep = np.array_split(p, len(p) // int(len(p) / thread_num))
    # neip = np.array_split(ip, len(ip) // int(len(ip) / thread_num))
    neq = np.array_split(q, len(q) // int(len(q) / thread_num))
    neiq = np.array_split(iq, len(iq) // int(len(iq) / thread_num))

    # Создание общей памяти для потоков
    shm = shared_memory.SharedMemory(create=True, size=ppoints*qpoints*np.int64().itemsize)
    shared_array = np.ndarray((ppoints*qpoints), dtype=np.int64, buffer=shm.buf)

    # Начало отсчёта
    start_time = time.time()

    # Пул потоков
    procs = []

    # Запуск потоков
    for i in range(thread_num):
        processes = mp.Process(target=funk, args=(p,ip,neq[i],neiq[i],max_iterations,infinity_border, shm.name, ppoints, qpoints) )
        procs.append(processes)
        processes.start()

    # Конец работы потоков
    for proc in procs:
        proc.join()
    
    print(f"затраченное время: {(time.time() - start_time):.2f} секунд")

    plt.xticks([])
    plt.yticks([])
    plt.imshow(shared_array[:].reshape(qpoints,ppoints).T, cmap='Greys')
    plt.show()