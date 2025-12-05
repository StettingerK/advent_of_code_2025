def get_specific_value(value:str,value_lenth:int):
    list_all_values = []
    for i in range(1,value_lenth):
        if i > value_lenth/2:
            break
        counter = 0
        list_step_values = []
        while counter < value_lenth:
            list_step_values.append(value[counter:counter+i])
            counter = counter + i
        list_all_values.append(list_step_values)
    return list_all_values


def main():
    # with open(".\\day_2\\input_beispiel.txt", "r") as file:
    with open(".\\day_2\\input_2.txt", "r") as file:
        data = file.readline()

    invalid = []
    data_splited = data.split(",")
    for single_data in data_splited:
        rangeing = single_data.split("-")
        for value in range(int(rangeing[0]),int(rangeing[1])+1):
            value = str(value)
            value_length = len(value)

            list_values = get_specific_value(value,value_length)
            for single_list in list_values:
                pruef_block = single_list[0]
                number_invalid = True
                for number in single_list:
                    if number != pruef_block:
                        number_invalid = False
                        break
                if number_invalid:
                    invalid.append(value)
                    # print(value)
                    break
    
    _sum = 0
    for i in invalid:
        # print(i)
        _sum += int(i)
    print(f"sum: {_sum}")

if __name__ == "__main__":
    main()