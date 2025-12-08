      
def main():
    with open(".\\day_5\\input_5.txt", "r") as file:
        data = file.readlines()

    result = 0

    check_begin = False
    fresh_range = []
    check_range = []
    for i in range(0,len(data)):
        if data[i] == '\n':  # aufteilen in fresh_range und check_range
            check_begin = True
            continue
        if not check_begin: # check_begin == False
            fresh_range.append(data[i].strip())
        else:
            check_range.append(int(data[i].strip()))
    
    # print(fresh_range)
    # print(check_range)

    # fresh_ids = []
    # counter = 0
    # for line in fresh_range: # alle ids speichern die fresh sind
    #     print(f"Range: {counter}")
    #     array = line.split("-")
    #     for number in range(int(array[0]),int(array[1])+1):
    #         fresh_ids.append(number)
    #     counter += 1
    # fresh_ids  = list(set(fresh_ids)) # doppelte ids entfernen
    
    # print("Fresh_IDs geladen")

    for number_to_check in check_range:
        is_fresh = False
        for line in fresh_range: 
            array = line.split("-")
            if int(array[0]) <= number_to_check <= int(array[1])+1:
                is_fresh = True
                break
        if is_fresh:
            result += 1


    print(f"result = {result}")


if __name__ == "__main__":
    main()
