#Program 15
#Stack operations 1(vk)

def pushh(stk, e):
    stk.append(e)

def popp(stk):
    if len(stk) == 0:
        return None
    else:
        return stk.pop()

def disp(stk):
    if len(stk) == 0:
        print("Stack is empty")
    else:
        print("Stack elements are:")
        for i in range(-1, -(len(stk)+1), -1):
            print(stk[i])

def peekk(stk):
    if len(stk) == 0:
        return None
    else:
        return stk[-1]

def main():
    stack = []
    while True:
        print("\n1.Push\n2.Pop\n3.Display\n4.Peek\n5.Exit")
        ch = int(input("Enter option: "))
        if ch == 1:
            e = int(input("Enter element to insert in the stack: "))
            pushh(stack, e)
        elif ch == 2:
            a = popp(stack)
            if a is None:
                print("Underflow! Nothing to delete")
            else:
                print("The deleted item is:", a)
        elif ch == 3:
            disp(stack)
        elif ch == 4:
            a = peekk(stack)
            if a is None:
                print("Underflow! Highest index null")
            else:
                print("The top element is:", a)
        elif ch == 5:
            print("Exiting...")
            break
        else:
            print("Invalid option")

main()

Output:
1.Push
2.Pop
3.Display
4.Peek
5.Exit
Enter option: 1
Enter element to insert in the stack: 4

1.Push
2.Pop
3.Display
4.Peek
5.Exit
Enter option: 1
Enter element to insert in the stack: 5

1.Push
2.Pop
3.Display
4.Peek
5.Exit
Enter option: 1
Enter element to insert in the stack: 6

1.Push
2.Pop
3.Display
4.Peek
5.Exit
Enter option: 2
The deleted item is: 6

1.Push
2.Pop
3.Display
4.Peek
5.Exit
Enter option: 3
Stack elements are:
5
4

1.Push
2.Pop
3.Display
4.Peek
5.Exit
Enter option: 4
The top element is: 5

1.Push
2.Pop
3.Display
4.Peek
5.Exit
Enter option: 5
Exiting....
