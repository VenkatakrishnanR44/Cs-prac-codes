#Text file code 1
# textfile1.py

# Step 1: Create the file with user input
with open("mainfile.txt", "w") as f:
    while True:
        line = input("Enter a line: ")
        f.write(line + "\n")
        more = input("Do you want to enter another line? (Y/N): ")
        if more.upper() != 'Y':
            break

# Step 2: Menu-driven operations
while True:
    print("\nMENU")
    print("1. Display number of lines")
    print("2. Copy words containing 'U' into another file and display")
    print("3. Convert case (lower <-> upper) and display")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        with open("mainfile.txt", "r") as f:
            lines = f.readlines()
            print("Number of lines:", len(lines))

    elif choice == '2':
        with open("mainfile.txt", "r") as f1, open("Uwords.txt", "w") as f2:
            words_with_u = []
            for line in f1:
                for word in line.split():
                    if 'u' in word or 'U' in word:
                        f2.write(word + "\n")
                        words_with_u.append(word)
            print("Words containing 'U' written to Uwords.txt:")
            print("\n".join(words_with_u) if words_with_u else "No such words found.")

    elif choice == '3':
        with open("mainfile.txt", "r") as f:
            print("\nCase converted contents:")
            for line in f:
                print(line.swapcase(), end='')

    elif choice == '4':
        print("Exiting program.")
        break

    else:
        print("Invalid choice! Please enter 1 to 4.")


Output
Enter a line: work for success
Do you want to enter another line? (Y/N): y
Enter a line: practise makes a man perfect
Do you want to enter another line? (Y/N): n

MENU
1. Display number of lines
2. Copy words containing 'U' into another file and display
3. Convert case (lower <-> upper) and display
4. Exit
Enter your choice (1-4): 1
Number of lines: 2

MENU
1. Display number of lines
2. Copy words containing 'U' into another file and display
3. Convert case (lower <-> upper) and display
4. Exit
Enter your choice (1-4): 2
Words containing 'U' written to Uwords.txt:
success

MENU
1. Display number of lines
2. Copy words containing 'U' into another file and display
3. Convert case (lower <-> upper) and display
4. Exit
Enter your choice (1-4): 3

Case converted contents:
WORK FOR SUCCESS
PRACTISE MAKES A MAN PERFECT

MENU
1. Display number of lines
2. Copy words containing 'U' into another file and display
3. Convert case (lower <-> upper) and display
4. Exit
Enter your choice (1-4): 4
Exiting program.

