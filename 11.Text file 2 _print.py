#Program no 11
#Text file 2

def create_file():
    n = int(input("Enter number of lines: "))
    with open("mainfile2.txt", "w") as f:
        for i in range(n):
            line = input(f"Enter line {i+1}: ")
            f.write(line + "\n")

def count_words():
    with open("mainfile2.txt", "r") as f:
        words = f.read().split()
        print("Total number of words:", len(words))

def is_palindrome(word):
    word = word.lower()
    rev = ""
    for ch in word:
        rev = ch + rev
    return word == rev

def display_vowel_words():
    vowels = "aeiouAEIOU"
    with open("mainfile2.txt", "r") as f:
        words = f.read().split()
        result = [w for w in words if w[0] in vowels and w[-1] in vowels]
        if result:
            print("Words starting and ending with a vowel:")
            for w in result:
                print(w)
        else:
            print("No such words found.")

# Main Program
create_file()

with open("mainfile2.txt", "r") as f:
    word_list = f.read().split()

while True:
    print("\nMENU")
    print("1. Count the number of words")
    print("2. Display Palindrome words")
    print("3. Display words starting and ending with a vowel")
    print("4. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        count_words()

    elif ch == 2:
        found = False
        print("Palindrome words:")
        for w in word_list:
            if is_palindrome(w):
                print(w)
                found = True
        if not found:
            print("None found.")

    elif ch == 3:
        display_vowel_words()

    elif ch == 4:
        print("Exiting...")
        break

    else:
        print("Invalid choice!")

Output
Enter number of lines: 2
Enter line 1: mom and dad are my world
Enter line 2: thrive for success

MENU
1. Count the number of words
2. Display Palindrome words
3. Display words starting and ending with a vowel
4. Exit
Enter your choice: 1
Total number of words: 9

MENU
1. Count the number of words
2. Display Palindrome words
3. Display words starting and ending with a vowel
4. Exit
Enter your choice: 2
Palindrome words:
mom
dad

MENU
1. Count the number of words
2. Display Palindrome words
3. Display words starting and ending with a vowel
4. Exit
Enter your choice: 3
Words starting and ending with a vowel:
are

MENU
1. Count the number of words
2. Display Palindrome words
3. Display words starting and ending with a vowel
4. Exit
Enter your choice: 4
Exiting...
