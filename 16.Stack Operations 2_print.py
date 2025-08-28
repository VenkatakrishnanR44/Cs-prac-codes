#Program 16
#Stack operation 2 (vk)
# Program: Stack with Country and Capital

def pushh(stk, country, capital):
    stk.append([country, capital])

def popp(stk):
    if len(stk) == 0:
        print("Underflow! Nothing to delete")
    else:
        a = stk.pop()
        print("Deleted element:", a)

def peekk(stk):
    if len(stk) == 0:
        print("Stack Empty! No top element")
    else:
        print("Top element:", stk[-1])

def disp(stk):
    if len(stk) == 0:
        print("Stack Empty!")
    else:
        print("Stack contents are (Top to Bottom):")
        for i in range(-1, -(len(stk)+1), -1):
            print(stk[i])

def main():
    stack = []
    while True:
        print("\n1. Insert (Push)\n2.Delete(Pop)\n3.Peek\n4.Display Stack\n5.Exit")
        ch = int(input("Enter option: "))
        
        if ch == 1:
            country = input("Enter Country: ")
            capital = input("Enter Capital: ")
            pushh(stack, country, capital)
        elif ch == 2:
            popp(stack)
        elif ch == 3:
            peekk(stack)
        elif ch == 4:
            disp(stack)
        elif ch == 5:
            print("Exiting...")
            break
        else:
            print("Invalid option!")

main()


Output:
1. Insert (Push)
2.Delete(Pop)
3.Peek
4.Display Stack
5.Exit
Enter option: 1
Enter Country: india
Enter Capital: delhi

1. Insert (Push)
2.Delete(Pop)
3.Peek
4.Display Stack
5.Exit
Enter option: 1
Enter Country: japan
Enter Capital: tokyo

1. Insert (Push)
2.Delete(Pop)
3.Peek
4.Display Stack
5.Exit
Enter option: 1
Enter Country: germany
Enter Capital: berlin

1. Insert (Push)
2.Delete(Pop)
3.Peek
4.Display Stack
5.Exit
Enter option: 2
Deleted element: ['germany', 'berlin']

1. Insert (Push)
2.Delete(Pop)
3.Peek
4.Display Stack
5.Exit
Enter option: 3
Top element: ['japan', 'tokyo']

1. Insert (Push)
2.Delete(Pop)
3.Peek
4.Display Stack
5.Exit
Enter option: 4
Stack contents are (Top to Bottom):
['japan', 'tokyo']
['india', 'delhi']

1. Insert (Push)
2.Delete(Pop)
3.Peek
4.Display Stack
5.Exit
Enter option: 5
Exiting...
