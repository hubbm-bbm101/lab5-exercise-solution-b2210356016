N=int(input("enter a number:"))
sum_odd=0
sum_even=0

for x in range(1,N+1):
    if x % 2 ==0:
        sum_even=sum_even+x
    else:
        sum_odd=sum_odd+x


print("sum of odd numbers are",sum_odd)
print("average of even numbers are",sum_even/N)