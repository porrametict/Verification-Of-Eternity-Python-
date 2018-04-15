import numpy as np
def getResult(frist,second,operator) :
    if operator == "!" : #frist = True False second = None 
        return not(frist)
    elif operator == "&":
        return np.logical_and(frist,second)
    elif operator == "|" :
        return np.logical_or(frist,second)
    elif operator == ">" :
        return np.logical_or(not(frist),second)
    elif operator == "%" :
        return not(np.logical_xor(frist,second))
print(getResult(True,False,"!"))
 