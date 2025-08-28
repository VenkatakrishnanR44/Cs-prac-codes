#Program 2
# Statistical functions (vk)
def find_mean(numbers):
    return sum(numbers) / len(numbers)

def find_median(numbers):
    sorted_numbers = sorted(numbers)  
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]

def find_mode(numbers):
    freq = {}
    for num in numbers:
        freq[num] = freq.get(num, 0) + 1

    max_count = max(freq.values())
    modes = [num for num, count in freq.items() if count == max_count]

    if len(modes) == 1:
        return str(modes[0])
    else:
        return ', '.join(str(m) for m in sorted(modes))


L = []
k = int(input("Enter number of terms: "))
for i in range(k):
    w = int(input(f"Enter element {i+1}: "))
    L.append(w)


print("Mean:", find_mean(L))
print("Median:", find_median(L))
print("Mode:", find_mode(L))

Output
1)
Enter number of terms: 4
Enter element 1: 1
Enter element 2: 2
Enter element 3: 3
Enter element 4: 4
Mean: 2.5
Median: 2.5
Mode: 1, 2, 3, 4

2)
Enter number of terms: 6
Enter element 1: 1
Enter element 2: 2
Enter element 3: 3
Enter element 4: 4
Enter element 5: 5
Enter element 6: 6
Mean: 3.5
Median: 3.5
Mode: 1, 2, 3, 4, 5, 6

