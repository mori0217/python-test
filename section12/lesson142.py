import pickle


class Test:
    def __init__(self, data):
        self.data = data


data = {
    "a": [1, 2, 3],
    "b": ("test", "test2"),
    "c": {"key": "value"},
    "d": Test("test pickling"),
}

with open("section12/data.pickle", "wb") as f:
    pickle.dump(data, f)

with open("section12/data.pickle", "rb") as f:
    data_loaded = pickle.load(f)
    print(data_loaded)
    print(data_loaded["d"].data)
    print(type(data_loaded["a"]))
    print(type(data_loaded["b"]))
    print(type(data_loaded["c"]))
    print(type(data_loaded["d"]))
