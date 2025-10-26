def remove_url_anchor(url):
    New_string = ""
    for char in url:
        if char == "#":
            break
        else:
            New_string += char
    
    return New_string

print(remove_url_anchor("www.codewars.com/katas/?page=1#about"))