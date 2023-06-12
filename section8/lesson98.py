import os
import pathlib
import glob
import shutil

# print(os.path.exists("section8/test.txt"))
# print(os.path.isfile("section8/test.txt"))
# print(os.path.isdir("section8/test.txt"))
# print(os.path.isdir("section8/design"))

# os.rename("section8/test2.txt", "section8/test_rename2.txt")
# os.symlink("section8/test_rename2.txt", "section8/test2_symlink.txt")

# os.mkdir("section8/test_dir")
# os.rmdir("section8/test_dir")

# pathlib.Path("section8/empty.txt").touch()
# os.remove("section8/empty.txt")

# os.mkdir("section8/test_dir")
# os.mkdir("section8/test_dir/test_dir2")
# print(os.listdir("section8/test_dir"))
# pathlib.Path("section8/test_dir/test_dir2/empty.txt").touch()
# print(os.listdir("section8/test_dir/test_dir2"))
# shutil.copy("section8/test_dir/test_dir2/empty.txt", "section8/test_dir/test_dir2/empty2.txt")
# print(glob.glob("section8/test_dir/test_dir2/*"))

# shutil.rmtree("section8/test_dir")
print(os.getcwd())
