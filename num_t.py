def H_n(n) :
    #Calculates the Hermonic Series the nth term
    z1 = 0
    for i in range(1, n + 1) :
        z2 = 1 / i
        z1 = z1 + z2
    return z1
    
def polygamma(n) :
    #Calculates the polygamma function (Only real int)
    z1 = 1 - math.log(2)
    for i in range(2,1000000) :
        z2 = 1 / i - math.log(1 + (1 / i))
        z1 = z1 + z2
    z3 = H_n(n - 1) - z1
    return z3
    
euler_c = - polygamma(1)