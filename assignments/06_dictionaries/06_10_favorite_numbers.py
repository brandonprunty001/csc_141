favorite_numbers = {
    "jermaine": [3, 7, 12],
    "kendall": [5, 10],
    "Cameron": [2, 8, 14],
    "brandon": [9],
    "dave kaul": [4, 11, 13]
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name}'s favorite numbers are:")
    for number in numbers:
        print(f"- {number}")