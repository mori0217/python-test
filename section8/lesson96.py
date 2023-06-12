import string

s = """\
Hi $name.

$contents

Have a good day
"""

t = string.Template(s)
contents = t.substitute(name="Mike", contents="How are you?")
print(contents)

with open("section8/design/email_template.txt") as f:
    t = string.Template(f.read())
contents = t.substitute(name="Mike", contents="How are your parents?")
print(contents)
