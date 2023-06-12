import glob
import zipfile

with zipfile.ZipFile("section8/test.zip", "w") as z:
    # z.write("section8/test_dir")
    # z.write("section8/test_dir/sub_dir")
    # z.write("section8/test_dir/sub_dir/sub.txt")
    for f in glob.glob("section8/test_dir/**", recursive=True):
        print(f)
        z.write(f)

with zipfile.ZipFile("section8/test.zip", "r") as z:
    # z.extractall("section8/test_zip")
    with z.open("section8/test_dir/sub_dir/sub.txt") as f:
        print(f.read())
