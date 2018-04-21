#import getSubExpression as gse 
#operand,subExpression=gse.getSubExpression()
#print(opreand,subExpression)
#เรียงโจทย์ย่อย
def sortSubExpression (subExpression:list) :
    sortedSubExpression = []
    lenNowString = len(subExpression[0])
    while  len(sortedSubExpression) < len(subExpression):
        for r in subExpression :
            if (len(r) == lenNowString )and(r not in sortedSubExpression) :
                sortedSubExpression.append(r)
        lenNowString +=1
    #print("lst",sortedSubExpression)
    return sortedSubExpression
#SubExpression = sortSubExpression(subExpression)
#ได้ดิกที่มีค่าความจริง
def getDictElement (operand:list,subExpression:list):
    #เอาลิตมาต่อกันเป็นดิก
    dictElement = {}
    for i in operand :
        dictElement[i] = [0 for i in range(2**len(operand))]
    for i in  subExpression :
        dictElement[i] = [0 for i in range(2**len(operand))]
    return dictElement
#DictE = getDictElement(operand,SubExpression)
#print(DictE)

        