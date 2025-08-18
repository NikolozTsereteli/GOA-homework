def descending_order(num):
    str_num = str(num)
    sorted_num = sorted(str_num, reverse = True)
    sorted_str = "".join(sorted_num)
    end = int(sorted_str)
    
    return end

print(descending_order(5123890352836))