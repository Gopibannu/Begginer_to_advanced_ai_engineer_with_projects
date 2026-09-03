#Build a unit converter (km<->miles, C<->F) that casts strings to numbers safely.
def safe_cast_float(value):
    """Safely converts a string to float without crashing."""
    try:
        return float(value), True
    except ValueError:
        return None, False


def convert_distance(val, direction):
    # Direction 1: Km to Miles | Direction 2: Miles to Km
    if direction == "1":
        return val * 0.621371, "miles"
    elif direction == "2":
        return val / 0.621371, "km"
    return None, None


def convert_temperature(val, direction):
    # Direction 1: Celsius to Fahrenheit | Direction 2: Fahrenheit to Celsius
    if direction == "1":
        return (val * 9 / 5) + 32, "°F"
    elif direction == "2":
        return (val - 32) * 5 / 9, "°C"
    return None, None


def main():
    print("Select Category:")
    print("1. Distance (km <-> miles)")
    print("2. Temperature (°C <-> °F)")
    category = input("Enter 1 or 2: ").strip()

    if category == "1":
        print("\n1. Kilometers to Miles\n2. Miles to Kilometers")
        direction = input("Choose conversion (1 or 2): ").strip()
        raw_val = input("Enter value: ").strip()

        val, success = safe_cast_float(raw_val)
        if not success:
            print("Error: Invalid numeric input.")
            return

        result, unit = convert_distance(val, direction)

    elif category == "2":
        print("\n1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius")
        direction = input("Choose conversion (1 or 2): ").strip()
        raw_val = input("Enter value: ").strip()

        val, success = safe_cast_float(raw_val)
        if not success:
            print("Error: Invalid numeric input.")
            return

        result, unit = convert_temperature(val, direction)

    else:
        print("Invalid category selection.")
        return

    if result is not None:
        print(f"\nResult: {result:.2f} {unit}")
    else:
        print("Invalid conversion choice.")


if __name__ == "__main__":
    main()