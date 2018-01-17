x = [1, 2, 3]

y = [4, 5, 6]

z = [7, 8, 9]
# x = list(zip(*x[::-1]))
xyz = zip(x, y, z)
print(list(xyz))
u = zip(*xyz)
print(list(u))