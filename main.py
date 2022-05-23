import functions
from approximations.degree_approximate import degree_approximate
from approximations.exp_approximate import exp_approximate
from approximations.linear_approximate import linear_approximate
from approximations.ln_approximate import ln_approximate
from approximations.qub_approximate import qub_approximate
from approximations.squad_approximate import squad_approximate
from input import *

if __name__ == "__main__":

    points = get_points()
    zxc=0
    # 1.2381𝑥 − -1.152
    # for p in points:
    #     zxc+=(abs(functions.input_func(p[0])-(-0.07*p[0]+0.68)))
    # print(zxc)
    # exit()
    print(f"Полученные точки: {points}\n")
    linear_approximation = linear_approximate(points)

    squad_approximation = squad_approximate(points)

    qub_approximation = qub_approximate(points)

    exp_approximation = exp_approximate(points)

    ln_approximation = ln_approximate(points)

    degree_approximation = degree_approximate(points)

    min_r = min(linear_approximation.squad_err, squad_approximation.squad_err, qub_approximation.squad_err,
                exp_approximation.squad_err,
                ln_approximation.squad_err, degree_approximation.squad_err)

    print(f"Минимальное среднеквадратичное отклонение: {round(min_r, 3)}")
    for approxi in {ln_approximation, linear_approximation, qub_approximation, exp_approximation, ln_approximation,
                    degree_approximation}:
        if min_r == approxi.squad_err:
            print(f"Лучшая аппроксимация: {approxi.name}")

    ploting(points, linear_approximation.func, squad_approximation.func, qub_approximation.func, exp_approximation.func,
            ln_approximation.func, degree_approximation.func)
