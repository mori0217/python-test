import tarfile

with tarfile.open("section8/files.tar.gz", "w:gz") as tr:
    tr.add("section8/test_dir")

# with tarfile.open("section8/files.tar.gz", "r:gz") as tr:
# tr.extractall("section8/test_tar")
# with tr.extractfile("section8/test_dir/sub_dir/sub.txt") as f:
# print(f.read())
