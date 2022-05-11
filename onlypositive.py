n = list(map(int, input("Enter integer values").split()))
for i in n:
    if i < 0:
        n.remove(i)
print(n)
