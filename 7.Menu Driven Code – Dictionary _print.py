#program 7
#Dictionary Operations(vk)
def add(pb):
    n = int(input("Enter number of subscribers to add: "))
    for i in range(n):
        print(f"\nSubscriber {i+1}:")
        name = input("Enter name: ")
        phno =input("Enter phone number: ")
        if len(phno)==10 and phno.isdigit():
            if phno in pb:
                print("Phone number already exists")
            else:
                pb[phno] = name
                print("Subscriber added successfully")
        else:
            print("Phone number must be of 10 numbers")

def view(pb):
    if not pb:  #checks if the dictionary pb is empty.
        print("No subscribers found.")
    else:
        print("Subscriber List:")
        for phno, name in pb.items():
            print(f"Phone: {phno}, Name: {name}")

def modify(pb):
    phno = input("Enter phone number to modify: ")
    if phno in pb:
        new_name = input("Enter new name: ")
        pb[phno] = new_name
        print("Subscriber name updated")
    else:
        print("Subscriber not found to be modified")

def delete(pb):
    phno = input("Enter phone number to delete: ")
    if phno in pb:
        del pb[phno]
        print("Subscriber deleted")
    else:
        print("Subscriber not found to be deleted")

def main():
    pb = {}
    while True:
        print("\nMenu\n1. Add details of Subscriber\n2. View details of Subscribers\n3. Modify Subscriber's Name\n4. Delete Subscriber's details\n5. Exit")
        ch = int(input("Enter 1 to 5 for choices: "))
        if ch == 1:
            add(pb)
        elif ch == 2:
            view(pb)
        elif ch == 3:
            modify(pb)
        elif ch == 4:
            delete(pb)
        elif ch == 5:
            print("Exiting....")
            break
        else:
            print("Invalid option, enter 1 to 5 for choices")

main()

Output
Menu
1. Add details of Subscriber
2. View details of Subscribers
3. Modify Subscriber's Name
4. Delete Subscriber's details
5. Exit
Enter 1 to 5 for choices: 1
Enter number of subscribers to add: 3

Subscriber 1:
Enter name: Ram
Enter phone number: 9876543210
Subscriber added successfully

Subscriber 2:
Enter name: Krishna
Enter phone number: 9988776655
Subscriber added successfully

Subscriber 3:
Enter name: Mukesh
Enter phone number: 7766554433
Subscriber added successfully

Menu
1. Add details of Subscriber
2. View details of Subscribers
3. Modify Subscriber's Name
4. Delete Subscriber's details
5. Exit
Enter 1 to 5 for choices: 2
Subscriber List:
Phone: 9876543210, Name: Ram
Phone: 9988776655, Name: Krishna
Phone: 7766554433, Name: Mukesh

Menu
1. Add details of Subscriber
2. View details of Subscribers
3. Modify Subscriber's Name
4. Delete Subscriber's details
5. Exit
Enter 1 to 5 for choices: 3
Enter phone number to modify: 7766554433
Enter new name: Magesh
Subscriber name updated

Menu
1. Add details of Subscriber
2. View details of Subscribers
3. Modify Subscriber's Name
4. Delete Subscriber's details
5. Exit
Enter 1 to 5 for choices: 4
Enter phone number to delete: 7766554433
Subscriber deleted

Menu
1. Add details of Subscriber
2. View details of Subscribers
3. Modify Subscriber's Name
4. Delete Subscriber's details
5. Exit
Enter 1 to 5 for choices: 5
Exiting....



            
            
    
            
    
