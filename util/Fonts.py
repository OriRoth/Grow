from enum import Enum


class Control(Enum):
    reset = "\033[0;1m"
    clear_console = "\033[H\033[2J"


class Color(Enum):
    black = "\033[30;1m"
    red = "\033[31;1m"
    green = "\033[32;1m"
    yellow = "\033[33;1m"
    blue = "\033[34;1m"
    purple = "\033[35;1m"
    cyan = "\033[36;1m"
    white = "\033[37;1m"


class Background(Enum):
    black = "\033[40;1m"
    red = "\033[41;1m"
    green = "\033[42;1m"
    yellow = "\033[43;1m"
    blue = "\033[44;1m"
    purple = "\033[45;1m"
    cyan = "\033[46;1m"
    white = "\033[47;1m"


class Text(Enum):
    bold = "\033[1;1m"
    italic = "\033[3;1m"
    underline = "\033[4;1m"


if __name__ == '__main__':
    print('This should not be shown...')
    print(Control.clear_console.value)
    print('Fonts test...')
    print(Color.green.value + 'green text' + Control.reset.value)
    print(Background.cyan.value + 'cyan background' + Control.reset.value)
    print(Text.underline.value + 'underline' + Control.reset.value)
