import inputFilter as nft
import getPostfix as gpf
import getDictElement as gde
import getSubExpression as gse
import getOperandVal as gopv
import getSubExpressionVal as gsev
import getEternityChecked as gec
import writefile as wf

class checkEternity():
    def Eternity(self):
        try :
            postfix = gpf.INfixToPostfix(self.expression)
            #print(postfix)
            operand,subExpression = gse.getSubExpression(postfix)
            #print(operand,subExpression)
            dictElement = gde.getDictElement(operand,subExpression)
            #print(dictElement)
            dictElement = gopv.getOperandVal(operand,dictElement)
            #print(dictElement)
            completeDict = gsev.getSubExpressionVal(operand,dictElement)
            #print(completeDict)
            sortedExpression = gde.sortSubExpression(subExpression)
            #print(sortedExpression)
           
            result = "ประพจน์นี้ "+gec.eternityCheck(completeDict,sortedExpression)
            
            wf.exportResultET(self.expression,result,operand,sortedExpression,completeDict)
            return result
        except Exception as e:
            return "ขออภัยโปรเเกรมไม่สามารถคำนวณได้ เนื่องจาก {}".format(e)


class checkEquivalent ():
     def Equivalent(self,another:"checkEquivalent"):
        try :
            postfix1 = gpf.INfixToPostfix(self.expression)
            postfix2 = gpf.INfixToPostfix(another.expression)
            #print(postfix)
            operand1,subExpression1 = gse.getSubExpression(postfix1)
            operand2,subExpression2 = gse.getSubExpression(postfix2)
            #print(operand,subExpression)
            dictElement1 = gde.getDictElement(operand1,subExpression1)
            dictElement2 = gde.getDictElement(operand2,subExpression2)
            #print(dictElement)
            dictElement1 = gopv.getOperandVal(operand1,dictElement1)
            dictElement2 = gopv.getOperandVal(operand2,dictElement2)
            #print(dictElement)
            completeDict1 = gsev.getSubExpressionVal(operand1,dictElement1)
            completeDict2 = gsev.getSubExpressionVal(operand2,dictElement2)
            #print(completeDict)
            sortedExpression1 = gde.sortSubExpression(subExpression1)
            sortedExpression2 = gde.sortSubExpression(subExpression2)
            #print(sortedExpression)
            result = gec.equalCheck(completeDict1,completeDict2,sortedExpression1,sortedExpression2)
            print(result)
            wf.exportResultEV(self.expression,another.expression,result,operand1,operand2,sortedExpression1,sortedExpression2,completeDict1,completeDict2)
    
            return self.expression +" เเละ "+ another.expression + result
        except Exception as e  :
             return "ขออภัยโปรเเกรมไม่สามารถคำนวณได้ เนืองจาก {}".format(e)  

#main

choice = input("""คุณต้องการทำอะไร
      กด 1 เพื่อตรวจสอบสัจจนิรันดร์
      กด 2 เพื่อตรวจสอบสมมูล
      กด เลขอื่น เพื่อไม่ทำอะไรเลย
      กรุ่ณาเลือก   
      """)
if choice == "1" :
    p = checkEternity()
    print("ตรวจสอบสัจจนิรันดร์")
    print("""เครื่องหมาย มีดังนี้
          ! คือ นิเสธ 
          & คือ เเละ
          | คือ หรือ
          > คือ ถ้าเเล้ว
          % คือ ก็ต่อเมื่อ
          โปรดตรวจสอบวงเล็บให้ดีๆ เเละกรอกประพจน์โดยไม่มีช่องว่าง""")
    text = False
    while text == False:
        text =nft.inputfilter((input("กรุณากรอกประพจน์ :")).strip())
    else:
        p.expression = text
        print(p.Eternity())
elif choice == "2" :
    p1 = checkEquivalent ()
    p2 = checkEquivalent ()
    print("ตรวจสอบสัจจนิรันดร์")
    print("""เครื่องหมาย มีดังนี้
          ! คือ นิเสธ 
          & คือ เเละ
          | คือ หรือ
          > คือ ถ้าเเล้ว
          % คือ ก็ต่อเมื่อ
          โปรดตรวจสอบวงเล็บให้ดีๆ เเละกรอกประพจน์โดยไม่มีช่องว่าง""")
    
    text1 = False
    while text1 == False:
        text1 =nft.inputfilter((input("กรุณากรอกประพจน์เเรก :")).strip())
    else:
        p1.expression = text1
    
    text2 = False
    while text2 == False:
        text2 =nft.inputfilter((input("กรุณากรอกประพจน์สอง :")).strip())
    else:
        p2.expression = text2
    
    print(p1.Equivalent(p2))

print("โปรเเกรมถูกปิดเเล้ว")

    