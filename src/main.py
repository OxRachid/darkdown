from src import colors as c
from src import deepdownload as deep_d
from src import functions as fun
from src import headerscreen as header
from src import normaldownload as normal_d

# print header screen
header.display_header()


def main_menu():
    fun.title_screen("* Select a Download Method *")
    print(" " * 20 + c.color_text("[1] Normal Download ", c.BRIGHT_WHITE, c.BOLD))
    print(" " * 20 + c.color_text("[2] Deep Download   ", c.BRIGHT_WHITE, c.BOLD))
    print(" " * 20 + c.color_text("[3] Exit            ", c.RED, c.BOLD))
    print(" " * 14 + c.color_text("╚════════════════════════════════╝   ", c.MEDIUM_RED))


def main():
    while True:
        main_menu()
        choice = fun.get_user_option(1, 3, c.color_text("\n[*] Enter your choice: ", c.BLUE, c.BOLD))
        fun.exit_option(choice, 3)

        if choice == 1:
            normal_d.main()  # Execute the normal download
            break
        elif choice == 2:
            deep_d.main()
            break
    pass


if __name__ == "__main__":
    main()
