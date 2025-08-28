#program 12
#Binary file 1(vk)

import pickle

def create():
    n = int(input("Enter number of students: "))
    with open("Student.dat", "ab") as f:
        for i in range(n):
            rollno = int(input("Enter roll no: "))
            name = input("Enter name: ")
            total = int(input("Enter total marks: "))
            record = [rollno, name, total]
            pickle.dump(record, f)
create()

def topper():
    top = None
    with open("Student.dat", "rb") as f:
        while True:
            try:
                record = pickle.load(f)
                if top is None or record[2] > top[2]:
                    top = record
            except EOFError:
                break
    if top:
        print("Topper details:")
        print("Roll No:", top[0])
        print("Name   :", top[1])
        print("Total  :", top[2])
    else:
        print("No records found.")


def increment():
    roll = int(input("Enter roll number to increment marks: "))
    records = []
    found = False


    with open("Student.dat", "rb") as f:
        while True:
            try:
                record = pickle.load(f)
                if record[0] == roll:
                    record[2] += 3
                    found = True
                records.append(record)
            except EOFError:
                break


    with open("Student.dat", "wb") as f:
        for r in records:
            pickle.dump(r, f)

    if found:
        print("Marks incremented successfully!")
    else:
        print("Roll number not found.")


while True:
    print("\nMENU")
    print("1. Display topper detail")
    print("2. Increment marks by 3 (for given roll no.)")
    print("3. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        topper()
    elif choice == 2:
        increment()
    elif choice == 3:
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try again.")


Output:
Enter number of students: 2
Enter roll no: 11
Enter name: nischal
Enter total marks: 450
Enter roll no: 12
Enter name: venkatakrishnan
Enter total marks: 470

MENU
1. Display topper detail
2. Increment marks by 3 (for given roll no.)
3. Exit
Enter your choice: 1
Topper details:
Roll No: 12
Name   : venkatakrishnan
Total  : 470

MENU
1. Display topper detail
2. Increment marks by 3 (for given roll no.)
3. Exit
Enter your choice: 2
Enter roll number to increment marks: 11
Marks incremented successfully!

MENU
1. Display topper detail
2. Increment marks by 3 (for given roll no.)
3. Exit
Enter your choice: 3
Exiting...

