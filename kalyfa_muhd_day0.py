points = {
    1:['a', 'e', 'i', 'l', 'n', 'o', 'r', 's', 't','u'],
    2:['d','g'],
    3:['b','c','m','p'],
    4:['f','h','v','w','y'],
    5:['k'],
    8:['j','x'],
    10:['q','z']
}

def word(string):
    score = 0
    for i in string:
        for k,v in points.items():
            if i in v:
                score = score + k
    return score

print(word('fortune'))