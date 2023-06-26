import re

html = "<html><head><title>Title</title></head></html>"

# greedy
print(re.match("<.*>", html).group())
# not greedy
print(re.match("<.*?>", html).group())
