l = [1, 2, 3]
i = 5
# del l

try:
    l[i]
except IndexError as ex:
    print("index error:{}".format(ex))
except NameError as ex:
    print("name error:{}".format(ex))
except Exception as ex:
    print("error:{}".format(ex))
else:
    print("success")
finally:
    print("clean up")
