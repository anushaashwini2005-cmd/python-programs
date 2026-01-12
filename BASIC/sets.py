a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)
print("Symmetric Difference:", a ^ b)

print("Subset:", a.issubset(b))
print("Superset:", a.issuperset(b))
print("Disjoint:", a.isdisjoint(b))

s = {1, 2, 3}

s.add(4)
s.update([5, 6])

s.remove(2)
s.discard(10)

print("After add/update/remove:", s)

s.pop()
print("After pop:", s)

copy_set = s.copy()
print("Copied Set:", copy_set)

s.clear()
print("Cleared Set:", s)