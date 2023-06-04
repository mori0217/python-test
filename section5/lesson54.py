def example_func(param1, param2):
    """Example Function サンプル関数

    Args:
        param1 (int): 数値
        param2 (str): 文字列

    Returns:
        bool: True or False
    """
    print(param1)
    print(param2)
    return True


print(example_func.__doc__)

# help(example_func)
