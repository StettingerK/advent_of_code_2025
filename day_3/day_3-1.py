def main():
    with open(".\\day_3\\input_3.txt", "r") as file:
        data = file.readlines()
    
    result = []
    for line in data:
        line = line.strip()
        # print(line)
        value_ges = 0
        for i in range(0,len(line)): # ersten value bestimmen
            value1 = line[i]
            for z in range(i+1,len(line)): # zweiten value bestimmen abhänig der position des ersten wertes
                value2 = line[z]
                temp = int(str(value1) + str(value2)) 
                if value_ges < temp:
                    value_ges = temp
        
        # print(f"Value 1: {value1}\tValue 2: {value2}\tValue_str: {value_ges}")
        result.append(value_ges)
    print(f"Sum: {sum(result)}")


if __name__ == "__main__":
    main()