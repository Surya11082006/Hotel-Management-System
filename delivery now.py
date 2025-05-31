 # DeliverNow: Real-Time Food Delivery Platform (With User Input)

class Restaurant:
    def __init__(self, name):
        self.name = name

    def receive_order(self, order):
        print(f"\nRestaurant '{self.name}' received the order for {order.food_item}.")
        order.status = "Preparing"
        print(f"{order.food_item} is being prepared...")

class Customer:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def place_order(self, food_item, restaurant):
        order = Order(self, food_item, restaurant)
        print(f"\n{self.name} placed an order for '{food_item}'.")
        restaurant.receive_order(order)
        return order

class DeliveryAgent:
    def __init__(self, name):
        self.name = name
        self.available = True

    def deliver(self, order):
        self.available = False
        print(f"\n{self.name} picked up the order from {order.restaurant.name}.")
        order.status = "Out for Delivery"
        print(f"Delivering {order.food_item} to {order.customer.name}...")
        order.status = "Delivered"
        self.available = True
        print(f"{order.food_item} delivered to {order.customer.name} by {self.name}.")

class Order:
    def __init__(self, customer, food_item, restaurant):
        self.customer = customer
        self.food_item = food_item
        self.restaurant = restaurant
        self.status = "Pending"

# --- Main Program ---
print("Welcome to DeliverNow: Real-Time Food Delivery\n")

customer_name = input("Enter your name: ")
customer_location = input("Enter your location: ")
food_item = input("Enter the food item you want to order: ")
restaurant_name = input("Enter the restaurant name: ")

# Create objects based on input
restaurant = Restaurant(restaurant_name)
customer = Customer(customer_name, customer_location)
agent = DeliveryAgent("Tom")

# Simulate the process
order = customer.place_order(food_item, restaurant)
agent.deliver(order)
