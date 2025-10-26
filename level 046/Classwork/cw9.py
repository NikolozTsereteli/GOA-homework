def number(bus_stops):
    sum1 = 0
    sum2 = 0
    for i in bus_stops:
        sum1 += i[0]
        sum2 += i[1]
        
    return sum1 - sum2
        
print(number([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]))

