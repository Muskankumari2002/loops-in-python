#Multiplication table printer
#print the multiplication table for a given number up to 10, but skip the 5th iteration
n = int(input("Enter the table number to print"))
for i in range(1,11):
    if(i==5):
        continue
    print(n, "x", i, "=", n*i)
    
