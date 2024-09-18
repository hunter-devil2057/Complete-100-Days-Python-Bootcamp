# Fibonacci Series
numTerms=int(input("Enter the Number of Terms: "))
def Fibonacci(num):
    fibSeries=[0, 1]    #starting value 
    for i in range(2, num):
        nextValue=fibSeries[-1]+fibSeries[-2]
        fibSeries.append(nextValue)
    return fibSeries[:num]
print("The Series is: ",Fibonacci(numTerms))