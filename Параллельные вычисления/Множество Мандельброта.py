__author__ = "Монастыршин Никита"
from module_mandelbrot import *


if __name__ == '__main__':
    # print("Number of cpu : ", mp.cpu_count())
    # Количество потоков
    # можно сделать проверку mp.cpu_count() чтобы не превышал 
    thread_num = 2
    ppoints, qpoints = 500, 500 # число точек по горизонтали и вертикали
    mandelbrot(thread_num, ppoints, qpoints)