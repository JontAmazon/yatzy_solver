"""Print in color."""


OMIT_PRINTS = True


# ANSI color codes
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
PURPLE = '\033[95m'
CYAN = '\033[96m'
RESET = '\033[0m'  # Reset color to default


def rprint(text):
    print(RED + text + RESET)

def gprint(text):
    print(GREEN + text + RESET)

def yprint(text):
    if not OMIT_PRINTS:
        print(YELLOW + text + RESET)

def bprint(text):
    if not OMIT_PRINTS:
        print(BLUE + text + RESET)

def pprint(text):
    if not OMIT_PRINTS:
        print(PURPLE + text + RESET)

def cprint(text):
    print(CYAN + text + RESET)
