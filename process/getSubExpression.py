def getSubExpression (expression:str) :
   # expression = "pq&!r|s>sr|%" #Postfix
    #ผลที่ความหวัง [p ,q ,r, s, pq& ,sr|, pq&!, pq&!r|, pq&!r|s>, pq&!r|s>sr|%]
    operand = []
    operator = {"!","&","|",">","%","(",")"} #เซตของโอเปอร์เตอร์เเละ วงเล็บ
    # เเยกโอเปอร์เรน p ,q ,r, s
    for i in expression:
        if i not in operator and i not in operand:
            operand.append(i)
    #เเยกโจทย์ย่อย  pq& ,sr|, pq&!, pq&!r|, pq&!r|s>, pq&!r|s>sr|% 
    subExpression = []
    stringToadd = ""
    countOperand = 0 
    for i in expression :
        stringToadd += i

        if i in operator : #ถ้าตัวปัจจุบันเแป็นโอเปอร์เรเตอร์
            if countOperand == 2 : #เป็นโจยท์ย่อยของย่อย 
                subExpression.append(stringToadd[-3:])
            else:
                subExpression.append(stringToadd)
            countOperand = 0
        else :
            countOperand += 1 
   # print(subExpression)
    return operand,subExpression
#opreand,subExpression=getSubExpression()
#print(opreand,subExpression)
        