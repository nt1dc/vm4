import math


class Approximation:
    def __init__(self, name, func, str_func, err, squad_err):
        self.name = name
        self.func = func
        self.str_func = str_func
        self.err = err
        self.squad_err = squad_err
        self.to_string()

    def to_string(self):
        if self.func is None:
            print(f"Нет ни одной точки в области определения {self.name}  функции")
            self.squad_err = math.inf
        else:
            print(
                f"{self.name} аппроксимацией получена функция: {self.str_func}, S = {round(sum(self.err), 3)}, sigma = {round(self.squad_err, 3)}\n")
