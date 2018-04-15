import numpy as np 
#นิเสธ
n1 = not(True)
n2 = not(False)
print("นิเสธ" , n1,n2)
# เเละ 
x1 = np.logical_and(True,True)
x2 = np.logical_and(False,True)
x3 = np.logical_and(True,False)
x4 = np.logical_and(False,False)
print("เเละ  ", x1,x2,x3,x4)
#หรือ 
r1 = np.logical_or(True,True)
r2 = np.logical_or(False,True)
r3 = np.logical_or(True,False)
r4 = np.logical_or(False,False)
print("หรือ " ,r1,r2,r3,r4)

#ก็ต่อเมื่อ 
l1 = not(np.logical_xor(True,True))
l2 = not(np.logical_xor(False,True))
l3 = not(np.logical_xor(True,False))
l4 = not(np.logical_xor(False,False))
print("ก็ต่อเมื่อ ", l1,l2,l3,l4)

#ถ้า......เเล้ว
rb1 = np.logical_or(not(True),True)
rb2 = np.logical_or(not(False),True)
rb3 = np.logical_or(not(True),False)
rb4 = np.logical_or(not(False),False)
print("ถ้าเเล้ว " , rb1,rb2,rb3,rb4)

