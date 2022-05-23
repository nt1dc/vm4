# Логарифмическая аппроксимация
import math

import numpy as np

from Approximation_class_file import Approximation
from calculations import calc_system


def ln_approximate(input_points):
    points = []

    for i in input_points:
        if i[0] == 0:
            points.append([i[0] + 0.001, i[1] + 0.001])
        if i[0] > 0:
            points.append(i)

    # if len(points) < 2:, но это будет неидеальная аппроксимация
    if len(points) != len(input_points):
        return Approximation("Логарифмическая", None, None, None, None)

    n = len(points)

    summ_x = 0.0
    summ_x_sqd = 0.0
    summ_y = 0.0
    summ_x_y = 0.0

    for point in points:
        summ_x += math.log(point[0])
        summ_x_sqd += math.log(point[0]) ** 2
        summ_y += point[1]
        summ_x_y += math.log(point[0]) * point[1]

    try:
        ans = calc_system([[summ_x_sqd, summ_x, summ_x_y], [summ_x, n, summ_y]], 2)
    except Exception:
        return Approximation("Логарифмическая", None, None, None, None)
    result_func = lambda x: ans[0] * np.log(x) + ans[1]

    str_result_func = f"{round(ans[0], 3)} ln(x) + {round(ans[1], 3)}"

    # СКО
    errors = [(points[i][1] - result_func(points[i][0])) ** 2 for i in range(n)]
    mid_sqd_err = math.sqrt(sum(errors) / n)

    return Approximation("Логарифмическая", result_func, str_result_func, errors, mid_sqd_err)
