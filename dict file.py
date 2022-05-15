n = input("Enter a string:")
a = {}
for i in n:
    if i not in a:
        a[i] = 1
    else:
        a[i] = a[i]+1

decreasingOrderFrequency = dict(sorted(a.items(), key=lambda x: x[1], reverse=True))
for x, y in decreasingOrderFrequency.items():
    print(x, "=", y, end=" ")
