
import time
import random

"""
    Welcome to Elite 101 this program is a starter for your chatbot project.
    The starter prompts the user to enter their name and then greets them with a personalized message.

    Functions:
        get_user_name(): Prompts the user to enter their name and returns it.
        greet_user(name): Prints a greeting message using the provided name.
        main(): Main function that orchestrates the user input and greeting process.

    Execution:
        When the script is run directly (not imported as a module), it will execute the main() function.
"""


def get_user_name():
    return input("Please enter your name: ")

def greet_user(name):
    print(f"Hello, {name}!")



def get_order_status(order_id):
    statuses = ["received", "preparing", "on the way", "delivered", "cancelled"]
    status = random.choice(statuses)
    if status == "cancelled":
        return {
            "order_id": order_id,
            "status": status,
            "estimated_arrival": "N/A"
        }
    elif status == "delivered":
        return {
            "order_id": order_id,
            "status": status,
            "estimated_arrival": "Delivered"
        }
    else:
        estimated_arrival = random.randint(10, 60)
          # Random time between 10 and 60 minutes
        return {
        "order_id": order_id,
        "status": status,
        "estimated_arrival": f"{estimated_arrival} minutes"
    }

def main():
    while True:
        choice = input("Please choose an option (Get order status or Exit): ")

        if choice == "Get order status":
            order_id = input("Please enter your 6 digit order ID: ")
            if len(order_id) != 6:
                print("Invalid order ID. Please try again.")
                continue
            order_status = get_order_status(order_id)
            print(f"Order ID: {order_status['order_id']}")
            print(f"Status: {order_status['status']}")
            print(f"Estimated Arrival: {order_status['estimated_arrival']}")
        elif choice == "Exit":
            print("Thank you for using Elite 101!")
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
