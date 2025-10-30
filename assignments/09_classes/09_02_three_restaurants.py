class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

restaurant1 = Restaurant("Mama Rosa’s", "Italian")
restaurant2 = Restaurant("Tokyo Table", "Japanese")
restaurant3 = Restaurant("Smokehouse BBQ", "Barbecue")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()