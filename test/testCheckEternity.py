#import getResult as gr
def CheckEternity(Postfix=""):
    expression = "pq&!r|s>sr|%" #Postfix
    output = True  # เป็นสัจนิรันดิ์ หรือ ไม่เป็น 
    #print("Infunc")
    allElement = dict() #dict เก็บข้อมูลทุกอย่าง โดยเก็บก {key:value }
    # โดย Key = หัวตารางนั้นๆ(คอลัม) เช่น P q PVQ เป็นต้น
    # โดย value = ลิตของค่าความจริงเเต่ล่ะอย่าง(เเถว) ซึ่ง มีจำนวน n ยกกำลังสอง ซึ่งจะไม่เกิน 16 เเถว อย่างเเน่นอน เนื่องจาก n ต้อง n <= 4   
    #ส่วนเก็บข้อมูล ของ 
    #เเยกโอเปอร์เรน
    operand = []
    operator = {"!","&","|",">","%","(",")"}#เซตของโอเปอร์เตอร์เเละ วงเล็บ
    for i in expression :
        if i not in operator and i not in operand :
            operand.append(i)
    #เเยกโจทย์ย่อย
    #print("Bloop")
    def findSubExpression ():
        subExpression = []
        forAddToSubExpression = "" 
        
        for i in expression :
     #       print(i)
      #      print(forAddToSubExpression)
            if i in operand : 
                forAddToSubExpression+= i
            elif((forAddToSubExpression +(i)) not in subExpression) : #ตรวจสอบว่าโจยท์ย่อยในปัจจุบัน มีในลิตโจทย์ย่อยหรือยัง
                forAddToSubExpression += i #เอา ตัวปัจจุบันไปต่อท้ายใน
                subExpression.append(forAddToSubExpression) # เพิ่มในลิตของโจทย์ย่อย
                #forAddToSubExpression = "" #ล้างข้อมูล
            else: # ถ้าโจทย์ย่อย มันซ้ำกับ โจทย์ย่อยในลิตต์
                forAddToSubExpression += i
        forAddToSubExpression = "" #ล้างข้อมูล
        subExpression.append(forAddToSubExpression) # เพิ่มในลิตของโจทย์ย่อย
        for i in expression :
     #       print(i)
      #      print(forAddToSubExpression)
            if i in operand : 
                forAddToSubExpression+= i
            elif((forAddToSubExpression +(i)) not in subExpression) : #ตรวจสอบว่าโจยท์ย่อยในปัจจุบัน มีในลิตโจทย์ย่อยหรือยัง
                forAddToSubExpression += i #เอา ตัวปัจจุบันไปต่อท้ายใน
                subExpression.append(forAddToSubExpression) # เพิ่มในลิตของโจทย์ย่อย
                forAddToSubExpression = "" #ล้างข้อมูล
            else: # ถ้าโจทย์ย่อย มันซ้ำกับ โจทย์ย่อยในลิตต์
                forAddToSubExpression += i
        subExpression.append(forAddToSubExpression) # เพิ่มในลิตของโจทย์ย่อย
        forAddToSubExpression = "" #ล้างข้อมูล
        return subExpression
    
                
    scsubExpression = [s for s in findSubExpression()]
   #print("BEFOR : "+str(scsubExpression))
    # กรองง่วนที่ไม่ต้องการออก
    for e in range(len(scsubExpression)) :
    #    print(e)
        if (len(scsubExpression[e])<=1 )or(len(scsubExpression[e]) == 2 and (not scsubExpression[e].endswith("!"))) or scsubExpression.count(scsubExpression[e]) >1: #ลบตัวที่มีจนาด หนึ่ง หรือ ขนาดสองเเละไมมี นิเสษ
            #print(scsubExpression[e] + "died")
            scsubExpression[e] = 0
        else:
            #print(scsubExpression[e]+" alived ")
            SubExpression = [d for d in scsubExpression if d != 0 ]
    #print("AFTER : "+str(SubExpression))
    #รวมเข้า Expression to allElement
    for i in operand : # นิพจน์เดี่ยว
        allElement[i] = [ 0 for i in range(2**len(operand))]
    for se in SubExpression : #โจยท์ย่อยๆ
        allElement[se]  = [0 for i in range(2**len(operand))]
    return allElement , operand #dict เเละ list
DE,operand = CheckEternity()
def getval(dictElement,SingleOperand):
    n = 0 
    forChange = len(SingleOperand)-1 #เอาไว้ตัวยกกำลัง 
    lenSO = len(SingleOperand)
    #  กำหนดค่าให้กับตัวเเปรเดียว
    dElement = dictElement
    #ประพจน์ปัจจุบัน
    while n < lenSO :
        thisVal = SingleOperand[n]  # key 
        nowAssign = True #ค่าที่กำลัง เเอด ลงไนดิก
        countChange = 0 # นับรอบใน For loop 
        valChange = (2**(forChange-n)) #ตัวที่ยกำลังเสร็จเเล้ว เอาไว้เป็น เพดานการเปลี่ยน
        for i in range(len(dElement[thisVal])):#วนลูปในลิตvalueนั้นๆ
     #       print(valChange)
            if countChange == valChange :
                nowAssign = not(nowAssign)
                countChange = 0
            dElement[thisVal][i] =nowAssign
            countChange +=1 
        n+=1
    #print(dElement)
    return dElement
AfterAssignSingleOperand = getval(DE,operand)
print(AfterAssignSingleOperand)
