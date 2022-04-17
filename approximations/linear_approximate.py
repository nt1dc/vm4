# Линейная аппроксимация
import math

from Approximation_class_file import Approximation
from calculations import calc_system


def linear_approximate(points):
    n = len(points)

    summ_x = 0
    summ_x_sqd = 0
    summ_y = 0
    summ_x_y = 0

    for i in range(n):
        summ_x += points[i][0]
        summ_x_sqd += points[i][0] ** 2
        summ_y += points[i][1]
        summ_x_y += points[i][0] * points[i][1]

    # коэффициент корреляции Пирсона
    mid_x = summ_x / n
    mid_y = summ_y / n
    # числитель
    summ_1 = 0
    summ_2 = 0
    summ_3 = 0

    for i in range(n):
        summ_1 += (points[i][0] - mid_x) * (points[i][1] - mid_y)
        # знаменатель (суммы 2 и 3)
        summ_2 += (points[i][0] - mid_x) ** 2
        summ_3 += (points[i][1] - mid_y) ** 2

    try:
        r = summ_1 / (math.sqrt(summ_2 * summ_3))
        print(f"Коэффициент корреляции Пирсона равен: {round(r, 3)}")
    except Exception:
        print("Не получилось посчитать коэффициент корреляции Пирсона")
    ans = calc_system([[summ_x_sqd, summ_x, summ_x_y], [summ_x, n, summ_y]], 2)

    result_func = lambda x: ans[0] * x + ans[1]

    str_result_func = f"{round(ans[0], 3)}x + {round(ans[1], 3)}"

    # среднеквадратичное отклонение
    errors = [(points[i][1] - result_func(points[i][0])) ** 2 for i in range(n)]
    mid_sqd_err = math.sqrt(sum(errors) / n)

    return Approximation("линейная", result_func, str_result_func, errors, mid_sqd_err)
