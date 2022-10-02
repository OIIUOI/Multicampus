res = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
}

arr = []
for i in range(3):
    arr.append(input())
# yellow, violet, red

total = (res[arr[0]] * 10 + res[arr[1]]) * (10 ** res[arr[2]])
print(total)
