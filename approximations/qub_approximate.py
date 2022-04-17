# Кубическая аппроксимация
import math

from Approximation_class_file import Approximation
from calculations import calc_system


def qub_approximate(points):
    n = len(points)

    summ_x = 0
    for i in range(n):
        summ_x += points[i][0]

    summ_x_sqd = 0
    for i in range(n):
        summ_x_sqd += points[i][0] ** 2

    summ_x_qub = 0
    for i in range(n):
        summ_x_qub += points[i][0] ** 3

    summ_x_forth = 0
    for i in range(n):
        summ_x_forth += points[i][0] ** 4

    summ_x_fifth = 0
    for i in range(n):
        summ_x_fifth += points[i][0] ** 5

    summ_x_six = 0
    for i in range(n):
        summ_x_six += points[i][0] ** 6

    summ_y = 0
    for i in range(n):
        summ_y += points[i][1]

    summ_x_y = 0
    for i in range(n):
        summ_x_y += points[i][0] * points[i][1]

    summ_x_sqd_y = 0
    for i in range(n):
        summ_x_sqd_y += (points[i][0] ** 2) * points[i][1]

    summ_x_cub_y = 0
    for i in range(n):
        summ_x_cub_y += (points[i][0] ** 3) * points[i][1]

    system = [
        [n, summ_x, summ_x_sqd, summ_x_qub, summ_y],
        [summ_x, summ_x_sqd, summ_x_qub, summ_x_forth, summ_x_y],
        [summ_x_sqd, summ_x_qub, summ_x_forth, summ_x_fifth, summ_x_sqd_y],
        [summ_x_qub, summ_x_forth, summ_x_fifth, summ_x_six, summ_x_cub_y]
    ]

    ans = calc_system(system, 4)

    result_func = lambda x: ans[3] * (x ** 3) + ans[2] * (x ** 2) + ans[1] * x + ans[0]

    str_result_func = f"{round(ans[3], 3)}x^3 + {round(ans[2], 3)}x^2 + {round(ans[1], 3)}x + {round(ans[0], 3)}"

    # СКО
    errors = [(points[i][1] - result_func(points[i][0])) ** 2 for i in range(n)]
    mid_sqd_err = math.sqrt(sum(errors) / n)

    return Approximation("Кубическая", result_func, str_result_func, errors, mid_sqd_err)
