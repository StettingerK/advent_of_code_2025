def try_line(_list:list,key:int):
    if key == -1 or key > len(_list)-1:
        string = ""
        for i in range(0,len(_list)):
            string += "."
        return string
    return _list[key]

        

def main():
    with open(".\\day_4\\input_4.txt", "r") as file:
        data = file.readlines()

    result = 0
    for i in range(0,len(data)):
        line_up = try_line(data,i-1).strip()
        line_main = try_line(data,i).strip()
        line_down = try_line(data,i+1).strip()

        for z in range(0,len(line_main)-1):
            counter = 0
            if line_main[z] == "@":
                if z != 0 and z:
                    if line_up[z-1] == "@":
                        counter += 1
                    if line_main[z-1] == "@":
                        counter += 1
                    if line_down[z-1] == "@":
                        counter += 1
                if z < len(line_main):
                    if line_up[z+1] == "@":
                        counter += 1
                    if line_main[z+1] == "@":
                        counter += 1
                    if line_down[z+1] == "@":
                        counter += 1
                if line_up[z] == "@":
                    counter += 1
                if line_down[z] == "@":
                    counter += 1
                if counter < 4:
                    result += 1



        # print(f"i: {i-1} line: {line_up}")
        # print(f"i: {i} line: {line_main}")
        # print(f"i: {i+1} line: {line_down}")

    print(f"result = {result}")


if __name__ == "__main__":
    main()
