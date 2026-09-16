
import tui
from math import floor, ceil
from decimal import Decimal

#--- helper functions

from decimal import Decimal
from typing import List, Union

from decimal import Decimal
from typing import List, Union

def arange(start, stop, step) -> list[float]:
    current = Decimal(str(start))
    target = Decimal(str(stop))
    increment = Decimal(str(step))

    if increment == 0:
        raise ValueError("arange() step argument must not be zero")

    result = []

    if increment > 0:
        while current <= target:
            result.append(float(current))
            current += increment
    else:
        while current >= target:
            result.append(float(current))
            current += increment

    return result

#--- graphs

# bar graph

bar_symbols = ' ▁▂▃▄▅▆▇█'

class bar:
    def __init__(self, values: list[float], width: int = 1, res: float = .5, spacing: int = 1, colourful: bool = True):
        self.values = values
        self.res = res
        self.width = width
        self.spacing = spacing
        self.colourful = colourful

        # calculate max and min bounds in steps of res
        self.n_y = ceil(max(values) / res)
        # ensure 0 or negative minimums are caught
        self.min_y = floor(min(0, min(values)) / res)

        # include self.min_y down to self.n_y
        self.max_y_str_len = max(len(str(i * self.res)) for i in range(self.n_y, self.min_y - 1, -1))

    def draw(self):
        print()
        for i in range(self.n_y, self.min_y - 1, -1):
            # step
            y = i * self.res
            # include spaces if needed to maintain alignment
            y_level = str(y) + ' ' + (self.max_y_str_len - len(str(y))) * '▔' + '▔▏'
            tui.printf(y_level)
            # print each line
            for j, val in enumerate(self.values):
                if val >= y:
                    sym = bar_symbols[len(bar_symbols) - 1]
                elif y - val < self.res and val > y - self.res:
                    sym = bar_symbols[floor(((val % self.res) / self.res) * len(bar_symbols))]
                else:
                    sym = ' '

                if self.colourful:
                    sym = tui.ANSI.colours[j % len(tui.ANSI.colours)] + sym + tui.ANSI.reset

                tui.printf(sym * self.width)
                tui.printf(' ' * self.spacing)
            print()
        print()

#--- running as main
# WIP: only bar graph

if __name__ == "__main__":
    inp = input("List of values or f(x) in Python: ")

    if 'x' in inp:
        # interval
        inp_interval = input("Interval (start,stop,step) or x-values: ")
        if ',' in inp_interval:
            start, stop, step = inp_interval.split(',')
            interval = arange(start, stop, step)
        else:
            interval = [float(f) for f in inp_interval]

        # calculate f(x) in interval
        values = []
        for x in interval:
            values.append(eval(inp.replace('x', str(x))))

    else:
        values = [float(f) for f in inp.split()]

    try:
        res = float(input("Resolution (1): "))
    except:
        res = 1

    try:
        spacing = int(input("Spacing (1): "))
    except:
        spacing = 1

    b = bar(values, spacing, res)
    b.draw()
