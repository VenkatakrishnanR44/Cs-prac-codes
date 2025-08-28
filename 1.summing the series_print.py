#Program 1
#Summing the series(vk)
def factorial(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f
def compute_series(x,n):
    sum=0
    power=1
    denom=2
    sign=1
    for i in range(n):
        term=(x**power)/factorial(denom)
        sum+=sign*term
        power+=2
        denom+=2
        sign*=-1
    return sum
x=int(input("Enter value for x:"))
n=int(input("Enter value for n:"))
series_sum = compute_series(x, n)
print("Sum of the series:", series_sum)


Enter value for x:2
Enter value for n:3
Sum of the series: 0.7111111111111111

Enter value for x:4
Enter value for n:6
Sum of the series: 0.41268986157875065

