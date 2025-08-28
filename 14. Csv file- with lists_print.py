#Program 14
#CSV FILE - WITH LISTS (vk)

import csv

def create_csv():
    n = int(input("Enter number of items: "))
    with open("ITEMS.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ItemID", "Name", "GST_percent", "Unitprice", "Finalprice"])
        for i in range(n):
            print(f"\nItem {i+1}:")
            itemid = input("Enter Item ID: ")
            name = input("Enter Name: ")
            gst = float(input("Enter GST percent: "))
            unitprice = float(input("Enter Unit price: "))
            finalprice = unitprice + (gst * unitprice / 100)
            writer.writerow([itemid, name, gst, unitprice, finalprice])
    print("ITEMS.CSV file created successfully.")

def display_csv():
    with open("ITEMS.CSV", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

create_csv()
print("\nContents of ITEMS.CSV:")
display_csv()

Output:
Enter number of items: 3

Item 1:
Enter Item ID: 111
Enter Name: socks
Enter GST percent: 18
Enter Unit price: 200

Item 2:
Enter Item ID: 112
Enter Name: shoes
Enter GST percent: 20
Enter Unit price: 400

Item 3:
Enter Item ID: 114
Enter Name: shoe polish
Enter GST percent: 12
Enter Unit price: 150
ITEMS.CSV file created successfully.

Contents of ITEMS.CSV:
['ItemID', 'Name', 'GST_percent', 'Unitprice', 'Finalprice']
['111', 'socks', '18.0', '200.0', '236.0']
['112', 'shoes', '20.0', '400.0', '480.0']
['114', 'shoe polish', '12.0', '150.0', '168.0']


