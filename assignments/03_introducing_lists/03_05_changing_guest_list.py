guests = ["kendall", "cam", "jermaine"]

for guest in guests:
    print(f"Hi {guest}, you are invited to the dorm!")

    cantmakeit = "kendall"
    print(f"\nunfortunately, {cantmakeit} can't make it to the dinner.\n")

    index_to_replace = guests.index(cantmakeit)
    guests[index_to_replace] = 'kareem'

    for guest in guests:
        print(f"Hi {guest}, you are invited to the party!")