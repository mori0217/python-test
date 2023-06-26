import contextlib
import os

try:
    os.remove("not_exist_file.txt")
except FileNotFoundError:
    pass

with contextlib.suppress(FileNotFoundError):
    os.remove("not_exist_file.txt")
