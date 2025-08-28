#Program 3
#Menu driven code-numeric(vk)
def fibonacci(n):
            a, b = 0, 1
            print("Fiboseries is:")
            for i in range(n):
                print(a, end=' ')
                a, b = b, a + b
            print()
            
def factorial(n):
            f=1
            for i in range(1,n+1):
                f*=i
            print("factorial is:",f)
while True:
    print("Enter 1 for factorial\nEnter 2 for fibonacii series\nEnter 3 to exit")
    ch=int(input("Enter the option u want:"))
    if ch==1:
        n=int(input("Enter number:"))
        factorial(n)
    elif ch==2:    
        n=int(input("Enter number:"))    
        fibonacci(n)
    elif ch==3:
        print("Exiting...")
        break
    
    else:
        print("Invalid option")
            

Output
Enter 1 for factorial
Enter 2 for fibonacii series
Enter 3 to exit
Enter the option u want:1
Enter number:5
factorial is: 120
Enter 1 for factorial
Enter 2 for fibonacii series
Enter 3 to exit
Enter the option u want:2
Enter number:6
Fiboseries is:
0 1 1 2 3 5 
Enter 1 for factorial
Enter 2 for fibonacii series
Enter 3 to exit
Enter the option u want:3
Exiting...

            
            

