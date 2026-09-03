#Build a simple age-based ticket-price calculator using comparisons and logic.

def calculate_ticket_price(age):
    # Standard pricing rules
    if age < 0:
        return "Invalid age entered."
    elif age <= 4:
        price = 0  # Toddlers/Infants enter free
    elif age <= 12:
        price = 10  # Child price
    elif age <= 64:
        price = 20  # Adult standard price
    else:
        price = 12  # Senior discount price

    return f"Ticket Price: ${price}"


# Example Usage:
user_age = int(input("Enter your age: "))
print(calculate_ticket_price(user_age))