def _list(a=[1, 2, 3]):
    a.append(1)
    return a

print(_list([1, 2, 3]))
print(_list())
print(set(_list()))