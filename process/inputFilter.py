def checkWhitespace(text:str) :
    for i in text :
        if i == " ":
            return True
    else:
        return False
            
def checkNum(text:str):
    for i in text :
        if i.isdigit() :
            return True
    else:
        return False

def checkOperand(text:str):
    operator ="()!%&>|"
    r = False
    for i in text :       
        if (i not in operator) and not(i.isalpha())  :
            r = False

         
    else:
        r = False
    return r
def checkBracket(text:str) :
    countOpen = 0
    countClose = 0 
    for i in text :
        if i =="(":
            countOpen += 1 
        elif i == ")":
            countClose +=1           
    return not(countOpen==countClose)
  
def inputfilter(textInput : str) :
    if textInput == "" :
        print("A")
        return False
    elif checkOperand(textInput):
        return False
        print("C")
    elif checkBracket(textInput):
        return False
        print("D")  
    elif checkNum(textInput):
        return False
        print("F")
    else:
        return textInput
#