import random 

def rand_bool() -> bool:
    variable = random.randint(0,1) 
    if variable == 0:
        return False
    else:
        return True
    
