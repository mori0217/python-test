import contextlib
import logging
import sys

# x = input("x: ")
# print(x)

# for line in sys.stdin:
# print(line)

# print("hello")
# sys.stdout.write("hello")

# logging.error("Error")
# sys.stderr.write("Error")

# with open("section18/stdout.log", "w") as f:
# with contextlib.redirect_stdout(f):
# print("Hello World")

with open("section18/stderr.log", "w") as f:
    with contextlib.redirect_stderr(f):
        logging.error("Hello Error")
