def bergenung(number: int):
    if number < 0:
        number = 100 + number
    if number > 99:
        number = number - 100
    return number


# with open(".\\data_test.txt", "r", encoding="UTF-8") as file:
with open(".\\Input_data.txt", "r", encoding="UTF-8") as file:
    lines = file.readlines()

position = 50
zero_conter = 0
for line in lines:
    direction = line[0]
    # print(f"diresction: {direction}")
    number = int(line[1:])
    # print(f"number: {number}")
    # print(f"Position davor: {position}")
    if direction == "R":
        position = bergenung(position + number)
    elif direction == "L":
        position = bergenung(position - number)
    # print(f"Position danach: {position}")
    if position == 0:
        zero_conter += 1
print(f"Zero Counter: {zero_conter}")

    