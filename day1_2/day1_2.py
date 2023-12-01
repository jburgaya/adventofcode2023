import re

mapping = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

num = "1, 2, 3, 4, 5, 6, 7, 8, 9, 0"

data = open('data', 'r')
lines = data.readlines()

num1 = []
num2 = []

def replace_letters(text):
    for i in mapping.keys():
        if i in text:
            text = re.sub(i,i[:2] + mapping[i] + i[2:], text)
    return text

for v in lines:
    v = replace_letters(v)
    for c in v:
        if c in num:
            num1.append(c)
            break

for v in lines:
    v = replace_letters(v)
    vv = v[::-1]
    for c in vv:
        if c in num:
            num2.append(c)
            break

print(num1)
print(num2)

nums = [int(str(x) + str(y)) for x, y in zip(num1, num2)]

print(nums)

out = sum(nums)

print(out)