a,b = map(int,input().split())
c = list(map(int,input().split()))
result=[]
for i in c:
    if i < b:
        result.append(i)
print(*result)