def write_data(mylist):
    my_columns = ['result', 'conversion_rate', 'conversion_type', "Amount"]
    mylist.insert(0, my_columns)
    with open("alldata.txt", 'w') as file:
        for row in mylist:
            line = str(row).strip("[]") + "\n"
            file.write(line)
    return

def make_file_into_list():
    result = []
    with open("/Users/ofir/mysh/only_course2/alldata.txt", 'r') as file:
        for line in file:
            line = line.strip()  # Remove whitespace and newline characters
            line = line.strip(")")
            line = line.strip("(")
            if line:
                sublist = line.split(",")  # Split the line into elements using a comma
                result.append(sublist)
    return result
