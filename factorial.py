#factorial using while loop
n = int(input("Enter the number to find factorial"))
fact =1
while(n>0):
    fact = fact*n
    n = n-1
    
print(fact)
