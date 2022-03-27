#Find Greatest Common divisor and Least Common Multiple among 2 numbers

def gcd_lcm(n1,n2):
    gcd = 1
    i = 2
    while (i <= n1 and i <= n2) :
        print("Entered while")
        if (n1 % i == 0 and n2 % i == 0) :
            n1= n1 // i
            n2= n2 // i
            gcd = gcd * i
        else :
            i = i + 1

    lcm = gcd * n1 * n2
    return(gcd,lcm)

print("Enter 2 numbers")
n1 = int(input("Enter first number"))
n2 = int(input("Enter second number"))
gcd,lcm = gcd_lcm(n1,n2)

print("GCD of {} and {} is {}".format(n1,n2,gcd))
print("LCM of {} and {} is {}".format(n1,n2,lcm))

    
    
