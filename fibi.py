n = int(input("Enter the no of terms: "))
a = [0, 1]
for i in range(0, n-2):
    c = a[i]+a[i+1]
    a.append(c)
print(a)
