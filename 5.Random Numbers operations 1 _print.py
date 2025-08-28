#program 5
#Random number generations (vk)
import random

def generate():
    l = []
    lm = int(input("Enter starting range: "))
    hm = int(input("Enter ending range: "))
    for i in range(lm, hm):
        r = random.randint(lm, hm)
        l.append(r)
    print("Random list:", l)
    return l

lst = generate()

def Max_num(lst):
    p = []
    for i in lst:
        if i not in p:
            p.append(i)
    n = len(p)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if p[j] > p[j + 1]:
                p[j], p[j + 1] = p[j + 1], p[j]

    if len(p) >= 2:
        print("Highest number:", p[-1])
        print("Second highest number:", p[-2])
    else:
        print("Minimum 2 numbers required to print Highest and Second Highest")

Max_num(lst)

def Prime(lst):
    primes = []
    for num in lst:
        if num > 1:
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    break
            else:
                if num not in primes: 
                    primes.append(num)
    if primes:
        print("Prime numbers in the list:", sorted(primes))
    else:
        print("No prime numbers in the generated list.")

Prime(lst)

Output
1)
Enter starting range: 1
Enter ending range: 10
Random list: [10, 7, 8, 8, 1, 1, 2, 6, 2]
Highest number: 10
Second highest number: 8
Prime numbers in the list: [2, 7]

2)
Enter starting range: 2
Enter ending range: 12
Random list: [12, 9, 8, 6, 3, 10, 3, 12, 3, 2]
Highest number: 12
Second highest number: 10
Prime numbers in the list: [2, 3]

