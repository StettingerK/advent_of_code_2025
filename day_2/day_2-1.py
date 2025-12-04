def main():
    with open(".\\day_2\\input.txt", "r") as file:
        data = file.readline()

    invalid = []
    data_splited = data.split(",")
    for single_data in data_splited:
        rangeing = single_data.split("-")
        for value in range(int(rangeing[0]),int(rangeing[1])+1):
            value = str(value)
            first_value = value[0:int(len(value)/2)]
            second_value = value[int(len(value)/2):]
            # print(f"first: {first_value} , second: {second_value}")
            if first_value == second_value:
                invalid.append(value)
    
    _sum = 0
    for i in invalid:
        # print(i)
        _sum += int(i)
    print(f"sum: {_sum}")

if __name__ == "__main__":
    main()