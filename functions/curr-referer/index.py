import sys

from function import handler


def get_stdin():
    buf = ""
    while True:
        line = sys.stdin.readline()
        buf += line
        if line == "":
            break
    if buf == "":
        raise ValueError("Must pass a value to the function.")
    return buf


if __name__ == "__main__":
    st = get_stdin()
    handler.handle(st)
