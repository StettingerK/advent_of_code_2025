      
def main():
    with open(".\\day_5\\input_5.txt", "r") as file:
        data = file.readlines()

    result = 0

    check_begin = False
    fresh_range = []
    for i in range(0,len(data)):
        if data[i] == '\n':  # aufteilen in fresh_range und check_range
            check_begin = True
            continue
        if not check_begin: # check_begin == False
            fresh_range.append(data[i].strip())
        else:
            break
    
    # fresh_range aufsplitten
    edited_array = []
    for line in fresh_range: # für alle ranges in fresh_range
        r_split = line.split("-")
        edited_array.append([int(r_split[0]),int(r_split[1])])

    # überflüssige doppelte Zahlen in den ranges entfernen
    changed = True
    while changed:
        changed = False
        for check_array in edited_array:
            for array in edited_array:
                if check_array == array:
                    continue
                # 10 <= 12 <= 14 und 10 <= 13 <= 14 also dazwischen dann range 12-13 löschen
                if check_array[0] <= array[0] <= check_array[1] and check_array[0] <= array[1] <= check_array[1]:
                    # print(f"Array: {array} and check_array: {check_array}")
                    edited_array.remove(array)
                    changed = True
                else:
                    if check_array[0] <= array[0] <= check_array[1]:
                        # array[0] zwischen check_array[0] und check_array[1] 10 <= 12 <= 14 dann 12 auf 15 setzen
                        # anfang der überscheindenden Range auf das ende der check_array + 1 setzen
                        i = edited_array.index(array)
                        new_array = [check_array[1]+1,array[1]]
                        edited_array[i] = new_array
                        changed = True
                    if check_array[0] <= array[1] <= check_array[1]:
                        # array[1] zwischen check_array[0] und check_array[1] 10 <= 13 <= 14 dann 13 auf 9 setzen
                        # ende der überscheindenden Range auf das Anfang der check_array - 1 setzen
                        i = edited_array.index(array)
                        new_array = [array[0],(check_array[0])-1]
                        edited_array[i] = new_array
                        changed = True  
    
    # doppelte werte rauswerfen
    temp_array = []
    temp_array_full = []
    for single_array in edited_array:
        if single_array[0] not in temp_array:
            temp_array.append(single_array[0])
            temp_array_full.append(single_array)
    edited_array = temp_array_full

    # Bubble Sort ist optional nur für debuggen
    # changed = True
    # while changed:
    #     changed = False
    #     for line in range(0,len(edited_array)-1):
    #         if edited_array[line] > edited_array[line+1]:
    #             line1 = edited_array[line]
    #             edited_array[line] = edited_array[line+1]
    #             edited_array[line+1] = line1
    #             changed = True

    # result addieren (ausrechnen)
    for r in edited_array:
        result = result + (int(r[1]) - int(r[0])) + 1
    print(f"result = {result}")

if __name__ == "__main__":
    main()
 