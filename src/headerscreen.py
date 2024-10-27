#!/usr/bin/env python3

import os

import colors as c


def clear_screen():
    # Check the operating system and clear the screen accordingly
    if os.name == "nt":  # For Windows
        os.system("cls")
    else:  # For macOS and Linux
        os.system("clear")


def display_header():
    clear_screen()

    # Display ASCII art with different shades of blue
    print()
    print(c.color_text("         ██████╗  █████╗ ██████╗ ██╗  ██╗", c.DEEP_DARK_RED))
    print(c.color_text("         ██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝", c.DEEP_DARK_RED))
    print(c.color_text("         ██║  ██║███████║██████╔╝█████╔╝", c.MEDIUM_RED))
    print(c.color_text("         ██║  ██║██╔══██║██╔══██╗██╔═██╗", c.DEEP_DARK_RED))
    print(c.color_text("         ██████╔╝██║  ██║██║  ██║██║  ██╗", c.DEEP_DARK_RED))
    print(c.color_text("         ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝", c.DEEP_DARK_RED))
    print(f"{c.color_text('⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣠⣤⣄⡀⠀⠀', c.WHITE)} {c.color_text(' ██████╗  ██████╗ ██╗    ██╗███╗   ██╗', c.DEEP_DARK_RED)}")
    print(f"{c.color_text(' ⠀⣠⣴⣾⣿⢿⣿⣻⣟⣿⣻⢯⣿⢿⣦⠀', c.WHITE)} {c.color_text('██║  ██║██║   ██║██║ █╗ ██║██╔██╗ ██║', c.DEEP_DARK_RED)}")
    print(f"{c.color_text(' ⢰⣿⣟⡷⣯⣿⡾⢿⣾⣽⣯⢿⣽⣯⣿⠀', c.WHITE)} {c.color_text('██║  ██║██║   ██║██║███╗██║██║╚██╗██║', c.MEDIUM_RED)}")
    print(f"{c.color_text(' ⠘⣿⣾⣻⣽⡾⣿⠀⢀⣭⣿⣟⡷⣯⣿⡆', c.WHITE)} {c.color_text('██████╔╝╚██████╔╝╚███╔███╔╝██║ ╚████║', c.DEEP_DARK_RED)}")
    print(f"{c.color_text(' ⠀⣿⣷⣻⢷⣟⣿⣶⣿⣟⡷⣯⣿⣻⣾⠇', c.WHITE)} {c.color_text('╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝', c.DEEP_DARK_RED)}")
    print(c.color_text(" ⠀⢹⣯⣟⡿⣾⢯⣷⣟⣾⣿⣽⣾⠷⠋", c.WHITE))
    print(c.color_text(" ⠀⠀⠀⠉⠛⠛⠋⠉⠁", c.WHITE))


if __name__ == "__main__":
    display_header()
