'''
Task is to remove duplicates from a given string.
Remove duplicates from string given " bananas " Return "bans" 
There are two solutions:
	One is of the order O(n) using dictionary.
	Another one is of Order(n2), but without using extra buffer, 
        though I need to convert string to list so it might taking some memory I don't understand 
'''
def reDuplicate(inStr):
    chars = {}
    output = []

    for i in range(len(inStr)):
        if inStr[i] in chars:
            continue
        else:
            chars[inStr[i]] = 1
            output.append(inStr[i])
    return "".join(output)

def reDuplicate2(inStr):
    inStr = list(inStr)
    if len(inStr) == 0:
        return ""
    elif len(inStr) == 1:
        return "".join(inStr)
    else:
        tail = 1
        for i in range(1, len(inStr)):
            j = 0
            for x in range(tail):
                if inStr[i] == inStr[j]:
                    break
                else:
                    j = j+1
            if j == tail:
                inStr[tail] = inStr[i]
                tail = tail + 1
        return "".join(inStr[:tail])



assert reDuplicate("bananas") == "bans"
assert reDuplicate2("bananas") == "bans"