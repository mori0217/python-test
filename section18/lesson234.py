import re

RE_CLOUDFORMATION_ARN = re.compile(r"""
    arn:aws:cloudformation:
    (?P<region>[\w-]+):
    (?P<account_id>[\d]+):
    stack/
    (?P<stack_name>[\w]+)/
    (?P<stack_id>[\w-]+)""", re.VERBOSE)

s1 = "arn:aws:cloudformation:us-east-1:123456789012:stack/MyProductionStack/abc9dbf0-43c2-11e3-a6e8-50fa526be49c"
s2 = "arn:aws:cloudformation:us-east-1:123456789098:stack/MyDevelopmentStack/abc9dbf0-43c2-11e3-a6e8-50fa526be49a"

for s in [s1, s2]:
    m = RE_CLOUDFORMATION_ARN.match(s)
    if m:
        print(m.group("region"))
        print(m.group("account_id"))
        print(m.group("stack_name"))
        print(m.group("stack_id"))
    else:
        print("No match")
