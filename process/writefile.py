#สร้างไฟล์
def CreateflieET(expression:str,result:bool):
    f = open("./result/result.html", "w" ,encoding ="utf8")
    if result == "ประพจน์นี้ เป็นสัจนิรันดร์" :
        bgcolor ="d2f4b2" 
    else :
        bgcolor = "f4b2b2"

    data = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>result</title>
</head>
<body style="background-color:#{}">
<h1 align="center"> {} {}</h1>

 """.format(bgcolor,expression,result)
    f.write(data)
    f.close()
    
def CreateflieEV(expression1:str,expression2:str,result:bool):
    f = open("./result/result.html", "w" ,encoding ="utf8")
    if result == " สมมูลกัน" :
        bgcolor ="d2f4b2" 
    else :
        bgcolor = "f4b2b2"

    data = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>result</title>
</head>
<body style="background-color:#{}">
<h1 align="center"> {} เเละ {} {}</h1>

 """.format(bgcolor,expression1,expression1,result)
    f.write(data)
    f.close()
    
def writeTableET(operand:list,sortedList:list,Dict:dict):
    with open("./result/result.html" ,"a",encoding ="utf8") as f:
        f.write("""<table align="center" border="1" bgcolor="white"  cellpadding="10">
    <tr>""")
        
        for i in sortedList+operand :
            #print(i,end= "+")
            data = """<th align="center">{}</th>""".format(i)
            f.write(data)
        f.write("""</tr>""")
        
        lengeList = (Dict[sortedList[0]])
        #print("!!!!")
        #print(lengeList)
        for row in range(len(lengeList)) :
            #print(row)
            f.write("""<tr>""")
            for col in (sortedList+operand) :
                #print(col)             
                data = """<td align="center">{}</td>""".format(Dict[col][row])
                f.write(data)
            #print("--")
                
            f.write("""</tr>""")
        f.write("""</table>
</body>
</html>""")
 
    

def writeTableEV(operand1:list,operand2:list,sortedList1:list,sortedList2:list,Dict1:dict,Dict2:dict):
    with open("./result/result.html" ,"a",encoding ="utf8") as f:
        f.write("""<table align="center" border="1" bgcolor="white"  cellpadding="10">
    <tr>""")
        
        for i in operand1+sortedList1 :
            #print(i,end= "+")
            data = """<th align="center">{}</th>""".format(i)
            f.write(data)
        f.write("""</tr>""")
        
        lengeList = (Dict1[sortedList1[0]])
        #print("!!!!")
        #print(lengeList)
        for row in range(len(lengeList)) :
            #print(row)
            f.write("""<tr>""")
            for col in (operand1+sortedList1) :
                #print(col)             
                data = """<td align="center">{}</td>""".format(Dict1[col][row])
                f.write(data)
            #print("--")
                
            f.write("""</tr>""")
        f.write("""</table>""")
        
        
        f.write("<hr>")
        f.write("""<table align="center" border="1" bgcolor="white"  cellpadding="10"><tr>""")
        for i in operand2+sortedList2 :
            #print(i,end= "+")
            data = """<th align="center">{}</th>""".format(i)
            f.write(data)
        f.write("""</tr>""")
        
        lengeList = (Dict2[sortedList2[0]])
        #print("!!!!")
        #print(lengeList)
        for row in range(len(lengeList)) :
            #print(row)
            f.write("""<tr>""")
            for col in (operand2+sortedList2) :
                #print(col)             
                data = """<td align="center">{}</td>""".format(Dict2[col][row])
                f.write(data)
            #print("--")
                
            f.write("""</tr>""")
        f.write("""</table>""")
     
        f.write("""
</body>
</html>""")
 
def exportResultET(expression,result,operand,sortedList,Dict) : #result คือ Ture Flase 
    CreateflieET(expression,result)
    writeTableET(sortedList,operand,Dict)
    
def exportResultEV(expression1,expression2,result,operand1,operand2,sortedList1,sortedList2,Dict1,Dict2):
    CreateflieEV(expression1,expression2,result)
    writeTableEV(operand1,operand2,sortedList1,sortedList2,Dict1,Dict2)

