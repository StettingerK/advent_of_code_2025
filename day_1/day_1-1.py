# with open(".\\data_test.txt", "r", encoding="UTF-8") as file:
with open(".\\day_1\\input_1.txt", "r", encoding="UTF-8") as file:
    lines = file.readlines()

position = 50
zero_conter = 0
for line in lines:
    direction = line[0]
    number = int(line[1:])
    if direction == "L":
        position = (position - number) % 100
    else:
        position = (position + number) % 100
    if position == 0:
        zero_conter += 1
print(f"Zero Counter: {zero_conter}")

    