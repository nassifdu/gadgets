
from time import sleep

#--- printing

def printf(*text: str):
    for t in text:
        print(t, end='', flush=True)

def typewrite(text: str, delay: float = 0.05):
    for char in text:
        print(char, end='', flush=True)
        sleep(delay)
    print()

#--- styling

class ANSI:
    red = "\033[31m"
    green = "\033[32m"
    yellow = "\033[33m"
    blue = "\033[34m"
    bold = "\033[1m"
    italic = "\033[3m"
    reset = "\033[0m"
    colours = [red, green, yellow, blue]

class symbols:
    class flower:
        line = '❀'
        fill = '✿'
        full = '⚘'
        left = '꧁'
        right = '꧂'
    class square:
        line = '□'
        fill = '■'
        rounded = '▢'
        small = '▫'
        tiny = '⬞'
        hole = '◘'
        two = '⧉'
        barred = '⧯'
        diamond = '⛋'
        horizontal = '▤'
        vertical = '▥'
        diagonal = '▧'
        halves = '◫'
        trigram = '☰'
    class triangle:
        class up:
            line = '△'
            fill = '▲'
        class down:
            line = '▽'
            fill = '▼'
        class left:
            line = '◁'
            fill = '◀'
        class right:
            line = '▷'
            fill = '▶'
    class dot:
        line = '○'
        fill = '●'
        big = '𒊹'
        dot = '☉'
        left = '◖'
        right = '◗'
        plus = '⊕'
        cross = '⊗'
        asterisk = '⊛'
        uranus = '⛢'
        cut = '⦵'
        perp = '⦹'
        star = '✪'
        wheel = '𖥞'
        dashed = '◌'
    class slice:
        one = '◔'
        two = '◑'
        three = '◕'
        four = '◍'
        left = '◐'
        right = '◑'
        lower = '◒'
        upper = '◓'
    class heart:
        line = '♡'
        fill = '♥'
        right = '❥'
        short = '❤'
    class moon:
        line = '☾'
        fill = '⏾'
    class dice:
        one = '⚀'
        two = '⚁'
        three = '⚂'
        four = '⚃'
        five = '⚄'
        six = '⚅'
    class smile:
        line = '☺'
        fill = '☻'
    class star:
        line = '☆'
        fill = '★'
        david = '✡'
    class spark:
        line = '✧'
        fill = '✦'
    class vortex:
        cw = '֎'
        ccw = '֍'
    class whole:
        vertical = '│'
        horizontal = '─'
        upper = '▀'
        lower = '▄'
        left = '▌'
        right = '▐'
        fill = '█'
