def max_value_in_str(string:str, start:int, end:int): # aus einem bestimmten stueck string den höchsten wert holen und dazu an welcher stelle dieser steht zurueckgeben
    check_string = string[start:len(string)-end]
    value = 0
    value_index = 0
    for i in range(0,len(check_string)):
        if value < int(check_string[i]):
            value = int(check_string[i])
            value_index = i+1
    return value,value_index



def main():
    with open(".\\day_3\\input_3.txt", "r") as file:
        data = file.readlines()
    
    result = []
    for line in data:
        line = line.strip()
        value_index = 0 # wird hochgezählt wo der string zum heraussuchen der zahlen starten darf
        number = ""
        for i in range(12,0,-1):
            value, temp_index = max_value_in_str(line,value_index,i-1) # line 12 mal durchgehen und dabei i weit vom ende des strings entfernt bleiben und bei value_index beginnen
            number += str(value)
            value_index += temp_index
        # print(number)
        result.append(int(number))
    print(f"Sum: {sum(result)}")


if __name__ == "__main__":
    main()
