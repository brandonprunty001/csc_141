favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python"
}

people_to_poll = ["jen", "sarah", "mike", "phil", "lisa"]

for person in people_to_poll:
    if person in favorite_languages:
        print(f"Thank you for taking the poll, {person.title()}!")
    else:
        print(f"{person.title()}, please take our poll!")