# program to map the collatz conjecture steps for a given input

# variables
Var1 = 0


# For even numbers
def even(x):
    return x / 2
# For odd numbers
def odd(x):
    return (x * 3)+1


#introduction
print ("Collatz Conjecture:")
print ("If a number is even, n/2")
print ("If a number is odd, 3n+1")
Var1 = int(input ("Give a number to map..."))

# nice bro
if Var1 == 69:
    print ("nice")
    
# Declares input as odd or even for absolutely no reason
if (Var1 % 2 ) == 0:
    print ("Your number is even")
else:
    print ("Your number is odd")
    
#Checks for odd/even, prints applicable adjustment to Var1, then adjusts Var1
while True:
    if Var1 % 2 == 0:
        print (even(Var1))
        Var1 = (Var1 / 2)
        # This section ends the cycle prior to an infinite 4,2,1 loop
        if Var1 == 1:
            print ("Complete")
            break
    else:
        print (odd(Var1))
        Var1 = (Var1 * 3) +1
        
 # if ya dun goofed       
else:
    print ("Input Error")

