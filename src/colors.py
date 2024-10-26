# Four Red Categories
LIGHT_RED = "38;5;210"  # Light red
MEDIUM_RED = "38;5;160"  # Medium red (Classic red)
DARK_RED = "38;5;124"  # Dark red (Crimson red)
DEEP_DARK_RED = "38;5;88"  #

# Normal Colors
BLACK = "30"
RED = "31"
GREEN = "32"
YELLOW = "33"
BLUE = "34"
MAGENTA = "35"
CYAN = "36"
WHITE = "37"

# Bright Colors
BRIGHT_BLACK = "90"
BRIGHT_RED = "91"
BRIGHT_GREEN = "92"
BRIGHT_YELLOW = "93"
BRIGHT_BLUE = "94"
BRIGHT_MAGENTA = "95"
BRIGHT_CYAN = "96"
BRIGHT_WHITE = "97"

# Background Colors
BG_BLACK = "40"
BG_RED = "41"
BG_GREEN = "42"
BG_YELLOW = "43"
BG_BLUE = "44"
BG_MAGENTA = "45"
BG_CYAN = "46"
BG_WHITE = "47"

# Bright Background Colors
BG_BRIGHT_BLACK = "100"
BG_BRIGHT_RED = "101"
BG_BRIGHT_GREEN = "102"
BG_BRIGHT_YELLOW = "103"
BG_BRIGHT_BLUE = "104"
BG_BRIGHT_MAGENTA = "105"
BG_BRIGHT_CYAN = "106"
BG_BRIGHT_WHITE = "107"

# Text Styles
BOLD = "1"
DIM = "2"
ITALIC = "3"
UNDERLINE = "4"
BLINK = "5"
REVERSE = "7"
HIDDEN = "8"
STRIKETHROUGH = "9"

# Reset
RESET = "0"


def color_text(text, *color_codes):
    """
    Apply multiple color codes to text.
    Usage: color_text("Hello", BRIGHT_RED, BG_YELLOW, BOLD)
    """
    color_string = ";".join(color_codes)
    return f"\033[{color_string}m{text}\033[0m"
