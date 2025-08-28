#program 9
# NUMBER.py
def PALINDROME(n):
    """Returns 1 if n is a palindrome number, else -1"""
    rev = 0
    temp = n
    while n > 0:
        d = n % 10
        rev = rev * 10 + d
        n //= 10
    return 1 if rev == temp else -1

def SPECIAL(n):
    """Returns 1 if n is a special number, else -1"""
    temp = n
    s = 0
    while n > 0:
        d = n % 10
        f = 1
        for i in range(1, d + 1):
            f *= i
        s += f
        n //= 10
    return 1 if s == temp else -1
# main.py

from NUMBER import PALINDROME, SPECIAL

# Testing PALINDROME with user input
t = ()
n = int(input("Enter number of values for palindrome check: "))
for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    t += (num,)

found = False
print("\nPalindrome numbers:")
for i in t:
    if PALINDROME(i) == 1:
        print(i, end=' ')
        found = True
if not found:
    print("No palindrome numbers found.")

# Testing SPECIAL numbers between two limits
print("\n\nSpecial numbers between two limits:")
a = int(input("Enter lower limit: "))
b = int(input("Enter upper limit: "))
found = False
for i in range(a, b + 1):
    if SPECIAL(i) == 1:
        print(i, end=' ')
        found = True
if not found:
    print("No special numbers found.")


Output
1)
Enter number of values for palindrome check: 5
Enter number 1: 121
Enter number 2: 232
Enter number 3: 123
Enter number 4: 444
Enter number 5: 789

Palindrome numbers:
121 232 444

Special numbers between two limits:
1 2 145


2)
Enter number of values for palindrome check: 6
Enter number 1: 101
Enter number 2: 453
Enter number 3: 989
Enter number 4: 0
Enter number 5: 45654
Enter number 6: 13231

Enter lower limit: 100
Enter upper limit: 300

Palindrome numbers:
101 989 0 45654 13231

Special numbers between two limits:
145




