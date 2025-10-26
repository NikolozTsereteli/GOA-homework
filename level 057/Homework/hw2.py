def to_csv_text(array):
    New_string = ""
    for listt in array:
        for i in listt:
            New_string += str(i) + ","
        New_string = New_string[:-1]
        New_string += "\n"
    
    return New_string[:-1]