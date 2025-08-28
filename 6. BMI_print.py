#program 6
#bmi code (vk)
def bmi():
    n = int(input("Enter number of persons: "))
    data = () # for nested tuple

    for i in range(n):
        print(f"\nFor person {i+1}")
        height = float(input("Enter height in metres: "))
        weight = float(input("Enter weight in kgs: "))
        data += ((height, weight),)

    for i in range(n):
        height, weight = data[i] #unpacks elements
        b = weight / (height ** 2)

        print(f"\nFor Person {i+1} BMI is:", b)

        if b >= 30:
            print("Obese")
        elif b > 25:
            print("Overweight")
        elif 18.5 < b <= 25:
            print("Normal")
        else:
            print("Underweight")

bmi()

Output
Enter number of persons: 2

For person 1
Enter height in metres: 1.7
Enter weight in kgs: 80

For person 2
Enter height in metres: 2.5
Enter weight in kgs: 90

For Person 1 BMI is: 27.68166089965398
Overweight

For Person 2 BMI is: 14.4
Underweight
