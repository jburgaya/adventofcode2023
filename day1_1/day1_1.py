num = "1, 2, 3, 4, 5, 6, 7, 8, 9, 0"

data = open('data', 'r')
lines = data.readlines()

print(lines)

num1 = []
num2 = []

for v in lines:
    print(v)
    for c in v:
        print(c)
        if c in num:
            num1.append(c)
            break

for v in lines:
    vv = v[::-1]
    print(vv)
    for c in vv:
        print(c)
        if c in num:
            num2.append(c)
            break

print(num1)
print(num2)


nums = [int(str(x) + str(y)) for x, y in zip(num1, num2)]

out = sum(nums)

print(out)
