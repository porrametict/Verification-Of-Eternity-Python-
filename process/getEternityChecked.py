
#d = gev.cd
#se = gde.SubExpression
def eternityCheck (completeDict:dict,sortedExpreesion:list):
   # print(sortedExpreesion[-1])
    for v in completeDict[sortedExpreesion[-1]] :
        if v == False :
            return "ไม่เป็นสัจนิรันดร์"
    else:
        return "เป็นสัจนิรันดร์"
#r = eternityCheck(d,se)
#print(r)
def equalCheck (Dict1:dict,Dict2:dict,sortedExpreesion1:list,sortedExpreesion2:list) :
    data1 = [x for x in Dict1[sortedExpreesion1[-1]]]
    data2 = [x for x in Dict1[sortedExpreesion2[-1]]]
    #print("infuc",data1,data2)
    for v1,v2 in zip(data1,data2):
       # print(v1,v2)
        if v1 != v2 :
            return " ไม่สมมูลกัน"
    else:
        return " สมมูลกัน"