# экспоненциальная аппроксимация
import math

import numpy as np

from Approximation_class_file import Approximation
from calculations import calc_system


def exp_approximate(input_points):
    name = "экспоненциальная"
    points = []

    for i in input_points:
        if i[0] == 0:
            points.append([i[0] + 0.001, i[1] + 0.001])
        if i[0] > 0:
            points.append(i)

    # if len(points) < 2:но это будет неидеальная аппроксимация
    if len(points) != len(input_points):
        return Approximation(name, None, None, None, None)

    n = len(points)
    summ_x = 0
    summ_x_sqd = 0
    summ_y = 0
    summ_x_y = 0

    for i in range(n):
        summ_x += points[i][0]
        summ_x_sqd += points[i][0] ** 2
        summ_y += math.log(points[i][1])
        summ_x_y += points[i][0] * math.log(points[i][1])

    try:
        ans = calc_system([[summ_x_sqd, summ_x, summ_x_y], [summ_x, n, summ_y]], 2)
    except Exception:
        return Approximation(name, None, None, None, None)
    result_func = lambda x: np.exp(ans[1]) * np.exp(ans[0] * x)

    str_result_func = f"{round(math.exp(ans[1]), 3)}e^{round(ans[0], 3)}*x"
    # СКО
    errors = [(points[i][1] - result_func(points[i][0])) ** 2 for i in range(n)]
    mid_sqd_err = math.sqrt(sum(errors) / n)

    return Approximation("экспоненциальная", result_func, str_result_func, errors, mid_sqd_err)
