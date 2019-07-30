# objects = [1, 2, 1, 2, 3]
objects = [1, 2, False, 0, 1, True, 2, 3]
ans = 0
ids = []
objects.sort()
for obj in objects: # доступная переменная objects
    # ans += 1
    if id(obj) not in ids:
        ids.append(id(obj))
    print (id(obj))
print(f"number={len(ids)}\nids={ids}\nobjects={objects}")
# print(ans)