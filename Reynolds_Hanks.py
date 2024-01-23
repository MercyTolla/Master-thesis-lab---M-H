def Re_hanks():
    a = 3
    b = 15
    R = a/b
    F_R = 1
    Z = 1
    
    #Symmetric case
    if R == 1: 
        eta = xi = 0.637
    elif R > 1: 
        eta = 1 #?
        xi = 1 #?
    #? Z 
    #? F(R)
    
    Re_c = (4848*R)/((1+R)*F_R*Z)
    return Re_c


    
        