# Nested dictionary code for houses and scores (vk)
def create():
    scores = {}
    categories = ["SENIORS", "JUNIORS", "SUBJUNIORS"]
    houses = ["BHARATHI", "TAGORE", "SHIVAJI", "PRATAP"]

    for category in categories:
        print(f"\nEnter scores for {category} category:")
        scores[category] = {}
        for house in houses:
            while True:
                try:
                    score = int(input(f"Enter score for {house} in {category}: "))
                    if 0 <= score <= 100:
                        scores[category][house] = score
                        break
                    else:
                        print("Please enter a score between 0 and 100.")
                except ValueError:
                    print("Invalid input. Please enter a valid integer for the score.")
    return scores

def MAX_SCORE(score_dict):
    print("\nMaximum Scores Per Category")
    for category, houses in score_dict.items():
        if not houses:
            print(f"No scores available for {category}.")
            continue

        max_score = -1
        max_houses = []

        for house, score in houses.items():
            if score > max_score:
                max_score = score
                max_houses = [house]
            elif score == max_score:
                max_houses.append(house)
        
        if len(max_houses) == 1:
            print(f"In {category}: {max_houses[0]} has the maximum score of {max_score}")
        else:
            print(f"In {category}: {', '.join(max_houses)} have the maximum score of {max_score}")

final_scores = create()
MAX_SCORE(final_scores)

Output:
Output:
Enter scores for SENIORS category:
Enter score for BHARATHI in SENIORS: 60
Enter score for TAGORE in SENIORS: 70
Enter score for SHIVAJI in SENIORS: 100
Enter score for PRATAP in SENIORS: 90

Enter scores for JUNIORS category:
Enter score for BHARATHI in JUNIORS: 70
Enter score for TAGORE in JUNIORS: 70
Enter score for SHIVAJI in JUNIORS: 60
Enter score for PRATAP in JUNIORS: 20

Enter scores for SUBJUNIORS category:
Enter score for BHARATHI in SUBJUNIORS: 80
Enter score for TAGORE in SUBJUNIORS: 70
Enter score for SHIVAJI in SUBJUNIORS: 100
Enter score for PRATAP in SUBJUNIORS: 90

Maximum Scores Per Category
In SENIORS: SHIVAJI has the maximum score of 100
In JUNIORS: BHARATHI, TAGORE have the maximum score of 70
In SUBJUNIORS: SHIVAJI has the maximum score of 100





