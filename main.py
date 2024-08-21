#fibonacci series

def fibonacci(n):

    #best case: when n==0 or n==1
    if n<=1:
        return n
    #recursive case: when n>1
    else:
        return fibonacci(n-1) +fibonacci(n-2)
    
number = 10
print(f"The fibonacci series till {number} is")
for i in range(number):
     print(fibonacci(i), end=" ")

#best case: when n==0 or n==1
#recursive case: when n>1 we have to recursive call the function again and again
#Time complexity: 0(2^n) worst case - exponential graph
#space complexity = 0(n) - linear graph