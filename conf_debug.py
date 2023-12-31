"""Configure what prints should be activated."""

DEBUG_MODE = True
DEBUG_MODE2 = False  # even more detail


def debug_print(string):
        if DEBUG_MODE:
            print(string)

def debug_print2(string):
        if DEBUG_MODE2:
            print(string)


