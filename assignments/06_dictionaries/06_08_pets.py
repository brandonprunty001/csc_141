pet1 = {"animal": "dog", "owner": "jermaine"}
pet2 = {"animal": "cat", "owner": "kendall"}
pet3 = {"animal": "rabbit", "owner": "cameron"}

pets = [pet1, pet2, pet3]

for pet in pets:
    print(f"{pet['owner']} owns a {pet['animal']}.")