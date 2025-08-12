def print_array(arr):
    New_string = ""
    for i in arr:
        New_string += str(i) + "," 
    
    
    return New_string[:-1]

print(print_array(["N", "I", "C", "E"]))