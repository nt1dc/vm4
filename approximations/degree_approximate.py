# Степенная аппроксимация
import math

import numpy as np

from Approximation_class_file import Approximation
from calculations import calc_system


def degree_approximate(input_points):
    points = []

    # добавляем в массив только те точки, которые подходят по ОДЗ логарифма
    for i in input_points:
        if i[1] > 0 and i[0] > 0:
            points.append(i)

    # if len(points) < 2:, но это будет неидеальная аппроксимация
    if len(points) != len(input_points):
        return Approximation("Степенная", None, None, None, None)

    n = len(points)
    summ_x = 0
    for i in range(n):
        summ_x += math.log(points[i][0])

    summ_x_sqd = 0
    for i in range(n):
        summ_x_sqd += math.log(points[i][0]) ** 2

    summ_y = 0
    for i in range(n):
        summ_y += math.log(points[i][1])

    summ_x_y = 0
    for i in range(n):
        summ_x_y += math.log(points[i][0]) * math.log(points[i][1])
    try:
        ans = calc_system([[summ_x_sqd, summ_x, summ_x_y], [summ_x, n, summ_y]], 2)
    except Exception:
        print(Exception)
        return Approximation("Степенная", None, None, None, None)
    result_func = lambda x: np.exp(ans[1]) * (x ** ans[0])

    str_result_func = f"{round(math.exp(ans[1]), 3)}x^{round(ans[0], 3)}"

    # СКО
    errors = [(points[i][1] - result_func(points[i][0])) ** 2 for i in range(n)]
    mid_sqd_err = math.sqrt(sum(errors) / n)

    return Approximation("Степенная", result_func, str_result_func, errors, mid_sqd_err)
