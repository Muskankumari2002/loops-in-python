# Sum of even numbers
# calculate the sum of even numbers up to a given number n
n = int(input("Enter number"))
sum_even =10
for i in range(1,n+1):
    if(i%2==0):
        sum_even +=1
        
print ("sum of even number is", sum_even)
