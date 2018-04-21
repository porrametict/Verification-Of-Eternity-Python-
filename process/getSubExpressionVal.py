import random
#import getOperandVal as gov
import getResult as grs
#import getSubExpression as gse
#operand,subExpression=gse.getSubExpression()
#dictElement = gov.d

def addBoolInString (dictElement:dict,expression:str,operand:set,nowrow:int):
    newString = ""
    for i in expression :
        if i in operand :
           newString += str(dictElement[i][nowrow])[0]
        else :
            newString += i 
    return newString

    
def getSubExpressionVal (operand:set,dictElement:dict) :
    row = 0 
    lenVal = len(random.choice((list(dictElement.values())))) #สุ่มเวลูที่เป็นลิตมาเพื่อต้องรู้ว่ามีทั้งหมด จำนวนกี่เเถว
    while row < lenVal :
        for k in dictElement.keys() :
            #print(k,dictElement[k][row]) #k==key, dictElement[k][row]==Val in this row     
            stringBool = addBoolInString(dictElement,k,operand,row) #ได้ TF%
           # print(sb)
            nowExpression = ""
            val = []
            countOperand = 0
            for s in stringBool :
                nowExpression += s
                if s =="T":
                    val.append(True)
                    countOperand +=1
                elif s == "F" :
                    val.append(False)
                    countOperand +=1
                elif s == "!" :
                    val.append(grs.getResult(val[-1],None,s))
                    del val[-2]
                    continue 
                else :
                    if countOperand == 0 : #ติดกับโอเปอร์เรน
                        val.append(grs.getResult(val[-2],val[-1],s))
                        del val[-2],val[-2] #เคลียค่าใน เวล
                        countOperand =0
                    elif countOperand == 1: #pq&!r| เป็นตรงตัว r
                        val.append(grs.getResult(val[-2],val[-1],s))
                        countOperand =0
                        del val[-2],val[-2] #เคลียค่าใน เวล
                    elif countOperand == 2 :  #pq&!r|s>sr|% เป็นตรง sr 
                        val.append(grs.getResult(val[-2],val[-1],s))            
                        del val[-2],val[-2] #เคลียค่าใน เวล
                        countOperand =0
            dictElement[k][row]=val[0]
                
        row+=1
    return  dictElement
   
#cd = getSubExpressionVal(operand,dictElement)
