#program 4
#Menu driven 2(vk)
def binary_search(lst, target):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

def main():
    while True:
        print("1. Binary Search\n2. Reverse String\n3. Exit")
        ch = input("Enter choice: ")
        
        if ch == "1":
            lst = []
            n = int(input("Enter the number of elements: "))  # Input for the number of elements
            for i in range(n):
                num = int(input(f"Enter element {i+1}: "))
                lst.append(num)  # Adding each element one by one
            lst.sort()
            print("Sorted list:", lst)
            target = int(input("Enter the number to search: "))
            result = binary_search(lst, target)
            if result != -1:
                print(f"{target} found at index {result}")
            else:
                print("No integer matched")
        
        elif ch == "2":
            string_input = input("Enter word to reverse: ")
            reversed_output = reverse_string(string_input)
            print("Reversed string is:", reversed_output)
        
        elif ch == "3":
            print("Exiting program....")
            break
        
        else:
            print("Invalid option")

main()


Output
1. Binary Search
2. Reverse String
3. Exit
Enter choice: 1
Enter the number of elements: 4
Enter element 1: 1
Enter element 2: 2
Enter element 3: 3
Enter element 4: 4
Sorted list: [1, 2, 3, 4]

Enter the number to search: 2
2 found at index 1
1. Binary Search
2. Reverse String
3. Exit
Enter choice: 2
Enter word to reverse: encyclopedia
Reversed string is: aidepolcycne

1. Binary Search
2. Reverse String
3. Exit
Enter choice: 3
Exiting program....

