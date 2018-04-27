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
def countOperand(text:str):
    count = 0
    for i in text :
        if i.isalpha() :
            count += 1
    if count > 5 :
        return True
    else :
        return False
def countOperator(text:str):
    count = 0
    operator ="!%&>|"
    for i in text :
        if i in operator :
            count += 1
    if count >6 :
        return True
    else :
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
        print("กรุณากรอกโจทย์ที่ถูกต้องตามเงื่อนไขครับ")
        return False
    elif checkNum(textInput):
        print("กรุณากรอกโจทย์ที่ไม่มีตัวเลขครับ")
        return False    
    elif countOperand(textInput):
        print("กรุณากรอกโจทย์ที่มีนิพจน์ซ้อนกันไม่เกิน 4 ตัวครับ")
        return False
    elif countOperator(textInput):
        print("กรุณากรอกโจทย์ที่มีโอเปอร์เรชั่นซ้อนกันไม่เกิน 6 ตัวครับ")
        return False
    elif checkOperand(textInput):
        print("กรุณากรอกโจทย์ที่ถูกต้องตามเงื่อนไขครับ")
        return False     
    elif checkBracket(textInput):
        print("กรุณากรอกโจทย์โดยตรวจสอบวงเล็บอีกรอบครับ") 
        return False
      
    else:
        return textInput
#