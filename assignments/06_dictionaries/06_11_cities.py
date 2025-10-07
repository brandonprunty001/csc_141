cities = {
    "paris": {
        "country": "france",
        "population": "2.1 million",
        "fact": "Paris is known as the City of Light."
    },
    "tokyo": {
        "country": "japan",
        "population": "13.9 million",
        "fact": "Tokyo is the most populous metropolitan area in the world."
    },
    "new york": {
        "country": "united states",
        "population": "8.5 million",
        "fact": "New York City is home to the Statue of Liberty."
    }
}

for city, info in cities.items():
    print(f"\nCity: {city.title()}")
    print(f"Country: {info['country'].title()}")
    print(f"Population: {info['population']}")
    print(f"Fact: {info['fact']}")