# objects = [1, 2, 1, 2, 3]
objects = [1, 2, False, 0, 1, True, 2, 3]
ids = []
for obj in objects: # доступная переменная objects
    if id(obj) not in ids:
        ids.append(id(obj))
print(len(ids))