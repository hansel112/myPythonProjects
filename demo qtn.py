import datetime
x=++11%2
print(x)
list = [1,6,5,3,4]
list.sort()
print(list)
list.reverse()
print(list)

def sum_list(n):
    sum = 0
    for i in list:
        sum +=i
    print(sum)
sum_list(list)
x=datetime.datetime.now()
print(x)

def prime(n):
    for i in range(2,n-1):
        if n/i== 0:
            print("composite")
        else:
            print("prime")
prime(5)

# Prime determination method
def Prime_series(number):
    for iter in range(2,number):
        if is_prime(iter) == True:
            print(iter,end = " ")
        else:
            pass


number = int(input("Enter the input Range : "))
is_prime = lambda number: all( number%i != 0 for i in range(2, int(number**0.5)+1) )
Prime_series(number)
