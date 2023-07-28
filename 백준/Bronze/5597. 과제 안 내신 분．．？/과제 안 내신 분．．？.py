list = [ _ for _ in range(1,31)]
for j in range(28):
    k = int(input())
    list.remove(k)
print(min(list))
print(max(list))