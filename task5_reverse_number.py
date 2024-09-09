a = int(input())
b = a % 10 * 100 + a//10 % 10 * 10 + a//100
c = str(b).strip()
print(c)
