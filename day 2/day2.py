def split_command(cmd: str) -> tuple:
    cmd = cmd.replace("\n", "")
    dir = cmd.split()[0]
    amount = int(cmd.split()[1])
    return dir, amount


with open("day2.txt") as source:
    data = source.readlines()
    x = 0
    z = 0
    for command in data:
        direction, amount = split_command(command)
        if direction == "forward":
            x += amount
        elif direction == "up":
            z -= amount
        elif direction == "down":
            z += amount
        else:
            x -= amount
        multiple = x * z
    print(f"forward: {x}, down: {z}, multiple = {multiple}")


with open("day2.txt") as source:
    data = source.readlines()
    aim = 0
    forward = 0
    depth = 0
    for command in data:
        dir, amount = split_command(command)

        if dir == "down":
            aim += amount
        elif dir == "up":
            aim -= amount
        elif dir == "forward":
            forward += amount
            depth += aim * amount
    final = depth * forward
    print(f"aim: {aim}, forward: {forward}, depth: {depth}, final = {final}")
