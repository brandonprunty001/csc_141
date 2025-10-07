person1 = {
    "first_name": "jermaine",
    "last_name": "armstrong",
    "age": 18,
    "city": "baltimore "
}

person2 = {
    "first_name": "kendall",
    "last_name": "hazzard",
    "age": 18,
    "city": "baltimore"
}

person3 = {
    "first_name": "cameron",
    "last_name": "benjamin",
    "age": 18,
    "city": "baltimore"
}

people = [person1, person2, person3]

for person in people:
    print(f"Name: {person['first_name']} {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}\n")