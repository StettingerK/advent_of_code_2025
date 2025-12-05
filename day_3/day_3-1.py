def main():
    with open(".\\day_3\\input_b_3.txt", "r") as file:
        data = file.readlines()
    
    max_digit_list = []
    for line in data:
        line = line.strip()
        print(line)
        value1 = [0,0]
        value2 = [0,1]
        counter = 0
        for digit in line:
            digit = int(digit)
            if value1[1] < value2[1] and value1[0] < digit: # auswahl in welche Variable geschrieben wird anhand wo der vorherige wert steht
                # if value1[0] < digit:
                value1[0] = digit
                value1[1] = counter
            else:
                if value2[0] < digit:
                    value2[0] = digit
                    value2[1] = counter
            counter += 1

            # if value1 < digit:
            #     value2 = value1
            #     value1 = digit
            # elif value2 < digit:
            #     value2 = digit
        value_str = str(value1) + str(value2)
        print(f"Value 1: {value1}\tValue 2: {value2}\tValue_str: {value_str}")
        max_digit_list.append(value1)
        max_digit_list.append(value2)
    print(f"Sum: {sum(max_digit_list)}")


if __name__ == "__main__":
    main()