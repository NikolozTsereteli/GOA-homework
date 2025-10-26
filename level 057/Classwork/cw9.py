def fake_bin(x):
    z = ""
    for i in x:
        if int(i) < 5:
            z += "0"
        else:
            z += "1"
    
    return z

print(fake_bin("124273582893528754545647858959076457846534504846894764897032434234345"))
            

