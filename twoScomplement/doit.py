#Coded By B3mB4m

def twoScomplement( hexdecimal):
    db = bin(int(hexdecimal, 16))[2:]
    cache = ""
    last = db.rindex('1')
    catch = db[:last]

    for x in catch:
        if x == "1":
            cache += "0"
        else:
            cache += "1"
    cache += db[last:]
    return cache
