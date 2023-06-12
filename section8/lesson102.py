# import os
import subprocess

# subprocess.run(["ls", "-l"])

# subprocess.run(["ls -l"], shell=True)
# r = subprocess.run(["ls -l"], shell=True, check=True)
# print(r.returncode)
# r = subprocess.run(["a"], shell=True)
# print(r.returncode)

p1 = subprocess.Popen(["ls", "-l"], stdout=subprocess.PIPE)
p2 = subprocess.Popen(["grep", "README"], stdin=p1.stdout, stdout=subprocess.PIPE)
p1.stdout.close()
output = p2.communicate()[0]
print(output)
