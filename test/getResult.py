import numpy as np
def getResult(frist:bool,second:bool,operator:str) :
    if operator == "!" : #frist = True False second = None
        if type(second) == type(None):
            return not(frist)
        else:
            return not(second)
    elif operator == "&":
        return np.logical_and(frist,second)
    elif operator == "|" :
        return np.logical_or(frist,second)
    elif operator == ">" :
        return np.logical_or(not(frist),second)
    elif operator == "%" :
        return not(np.logical_xor(frist,second))
#print(getResult(True,False,"!"))

 