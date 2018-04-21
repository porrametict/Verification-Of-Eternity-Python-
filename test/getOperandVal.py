#import getDictElement as gde
#import getSubExpression as gse 
#operand,subExpression=gse.getSubExpression()
#SubExpression = gde.sortSubExpression(subExpression)
#DictE = gde.getDictElement(operand,SubExpression)

#กำหนดค่าให้โอเปอร์เรน
def getOperandVal (operand:list,dictElement:dict):
    n = 0 
    forChange = len(operand)-1 #เอาไว้ยกกำลัง
    ###
    while n < len(operand) :
        thisVal = operand[n] #key 
        nowAssign = True # ค่าที่กำลัง เพิ่มลงในดิก 
        countChange = 0 # รับรอบในลูป For  
        valChange = (2**(forChange-n)) #ตัวที่ยกกำลังเสร็จเเล้วเอาไว้เป็นจุดเปลี่ยน
        for i in range(len(dictElement[thisVal])): #ลูปในลิตของเวลู ของ คีย์นั้นๆ
            if countChange == valChange :
                nowAssign = not(nowAssign)
                countChange = 0
            dictElement[thisVal][i] = nowAssign
            countChange += 1 
        n+=1
        
    #print(dictElement)
    return dictElement 
    
#d = getOperandVal(operand,DictE)
