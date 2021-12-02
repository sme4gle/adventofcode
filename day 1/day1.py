def readfile() -> list:
    with open("data.txt") as f:
        return [int(x) for x in f.read().splitlines()]


def solution_one() -> int:
    data = readfile()
    prev_entry = 0
    count = 0
    for entry in data:
        if int(entry) >= prev_entry:
            count += 1
        prev_entry = int(entry)
    return count


def solution_two() -> int:
    data = readfile()
    count = 0
    for enum, entry in enumerate(data):
        if enum > 2 and sum(data[enum - 3 : enum]) < sum(data[enum - 2 : enum + 1]):
            count += 1

    return count


print(solution_one())
print(solution_two())
