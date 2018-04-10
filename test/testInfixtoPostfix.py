#Infix To Postfix 
inPut ="" #รับค่าไม่เกิด 4 นิพจน์ เเละ โอเปอร์เตอร์ซ้อนกันไม่เกิน  6 ชั้น เช่น ~(p^q)Vr<>S-->(sVr)
stack = []
#
# เนื่องจาก ตัวโอเปอร์เรชั่น เเละ หรือ ถ้าเเล้ว ก็ต่อเมื่อ ไม่มีลำกับความสำคัญ ถ้าผู้ใช้ไม่กำหนด วงเล็บให้ ดีๆ 
# โปรเเกรมจะทำการคำนวณจากซ้ายไปขวาตาม
# ดักเรื่อง จำนวน การซ้อนของโอเปอร์เรเตอร์ จำนวนตัวเเปร
# ดักหรื่องวงเล็บเปิดปิดของผู้ใช้ ถ้าใช้วงเล็บเปิดเเล้วจำเป็นต้องใส่วงเป็บปิด
# INfix = !(p&p)|!r>s%q
# กำหนดให้ เครื่องหมาย  !  คือ  นิเสธ
# กำหนดให้ เครื่องหมาย  &  คือ  เเละ
# กำหนดให้ เครื่องหมาย  |  คือ  หรือ
# กำหนดให้ เครื่องหมาย  >  คือ  ถ้า..เเล้ว
# กำหนดให้ เครื่องหมาย  % คือ  ก็ต่อเมื่อ
#Postfixmujคาดหวัง  = pp&r!|s>q%
operator ={"(":4,"not":2, "and":2,"or":2}  
PostfixOutput = ""