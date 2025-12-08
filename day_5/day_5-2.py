      
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
    
    # print(fresh_range)

    count = 0
    fresh_ids = []
    for line in fresh_range: # alle ids speichern die fresh sind
        print(f"count: {count}")
        array = line.split("-")
        for number in range(int(array[0]),int(array[1])+1):
            fresh_ids.append(number)
        count += 1
    fresh_ids  = list(set(fresh_ids)) # doppelte ids entfernen
    result = len(fresh_ids)

    print(f"result = {result}")


if __name__ == "__main__":
    main()
