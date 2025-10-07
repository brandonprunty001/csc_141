favorite_places = {
    "jermaine": ["Paris", "New York", "Tokyo"],
    "kendall": ["London", "Rome", "Berlin"],
    "Cameron": ["Sydney", "Toronto", "Dubai"]
}

for name, places in favorite_places.items():
    print(f"\n{name}'s favorite places are:")
    for place in places:
        print(f"- {place}")