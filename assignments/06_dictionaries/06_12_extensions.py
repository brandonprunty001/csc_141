cities = {
    "paris": {
        "country": "france",
        "population": "2.1 million",
        "fact": "Paris is known as the City of Light."
    },
    "tokyo": {
        "country": "japan",
        "population": "13.9 million",
        "fact": "Tokyo has more Michelin-starred restaurants than any other city."
    },
    "new york": {
        "country": "united states",
        "population": "8.5 million",
        "fact": "New York City is home to Central Park and the Statue of Liberty."
    },
    "london": {
        "country": "england",
        "population": "9.5 million",
        "fact": "London is home to the oldest underground railway system in the world."
    },
    "sydney": {
        "country": "australia",
        "population": "5.3 million",
        "fact": "Sydney is famous for its Opera House and beautiful harbor."
    }
}

for city, info in cities.items():
    print(f"\nCity: {city.title()}")
    print(f"Country: {info['country'].title()}")
    print(f"Population: {info['population']}")
    print(f"Fact: {info['fact']}")