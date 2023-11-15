#!/usr/bin/env python


def colorize(color_code, s):
    return f"\033[{color_code}m{s}\033[0m"


def bold(s):
    return colorize(1, s)


def reverse(s):
    return colorize(7, s)


def strikeout(s):
    return colorize(9, s)


def underline(s):
    return colorize(21, s)


def black(s):
    return colorize(30, s)


def red(s):
    return colorize(31, s)


def green(s):
    return colorize(32, s)


def yellow(s):
    return colorize(33, s)


def blue(s):
    return colorize(34, s)


def magenta(s):
    return colorize(35, s)


def cyan(s):
    return colorize(36, s)


def white(s):
    return colorize(37, s)


def bg_black(s):
    return colorize(40, s)


def bg_red(s):
    return colorize(41, s)


def bg_green(s):
    return colorize(42, s)


def bg_yellow(s):
    return colorize(43, s)


def bg_blue(s):
    return colorize(44, s)


def bg_magenta(s):
    return colorize(45, s)


def bg_cyan(s):
    return colorize(46, s)


def bg_white(s):
    return colorize(47, s)


def print_log(s):
    print(reverse(blue("[*]")) + " " + s)


def print_warn(s):
    print(reverse(yellow("[!]")) + " " + yellow(s))


def print_error(s):
    print(reverse(red("[X]")) + " " + bold(red(s)))


if __name__ == "__main__":
    s = "Hello World!"
    print(white("Hello World!"))
    print(red("Hello World!"))
    print(green("Hello World!"))
    print(yellow("Hello World!"))
    print(reverse(yellow("Hello World Reversed!")))
    print(blue("Hello World!"))
    print(magenta("Hello World!"))
    print(cyan("Hello World!"))
    print(bold(cyan("Hello World Bolded!")))
    print(reverse(cyan("Hello World Reversed!")))
    print(white("Hello World!"))
    print(bg_black(s))
    print(bg_red(s))
    print(bg_green(s))
    print(bg_yellow(s))
    print(bg_blue(s))
    print(bg_magenta(s))
    print(bg_cyan(s))
    print(bg_white(s))
    print(bg_green(blue(s)))  # You can combine colorizations!
    print_log("This is a good log.")
    print_warn("This is a warning log.")
    print_error("This is an error log.")
