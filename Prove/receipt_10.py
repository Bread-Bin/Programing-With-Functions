import csv
import datetime
import random
import time
import sys

# Constants
SALES_TAX_RATE = 0.06
COUPONS = [
    "Free juice box with every emotional breakdown.",
    "Buy 1 slice of pizza, get absolutely nothing free!",
    "15% OFF fancy hats you will never actually wear.",
    "$3 OFF your next impulse purchase over $60.",
    "Free 'mystery item' with your next receipt longer than 3 feet."
]
LOGO_ART = r"""
 __      __        .__  .__           __      __            .__       .___
/  \    /  \_____  |  | |  | ___.__. /  \    /  \___________|  |    __| _/
\   \/\/   /\__  \ |  | |  |<   |  | \   \/\/   /  _ \_  __ \  |   / __ | 
 \        /  / __ \|  |_|  |_\___  |  \        (  <_> )  | \/  |__/ /_/ | 
  \__/\  /  (____  /____/____/ ____|   \__/\  / \____/|__|  |____/\____ | 
       \/        \/          \/             \/                         \/ 
"""
START_COLOR_HEX = "FF99AA"  # Pink/Salmon
END_COLOR_HEX   = "2DD4BF"  # Teal/Cyan
COLOR_RESET = "\033[0m"

# Gradient logo functions
def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def interpolate_color(start_rgb, end_rgb, t):
    r = int(start_rgb[0] + (end_rgb[0] - start_rgb[0]) * t)
    g = int(start_rgb[1] + (end_rgb[1] - start_rgb[1]) * t)
    b = int(start_rgb[2] + (end_rgb[2] - start_rgb[2]) * t)
    return (r, g, b)

def get_color_code(rgb):
    r, g, b = rgb
    return f"\033[38;2;{r};{g};{b}m"

def print_logo():
    start_rgb = hex_to_rgb(START_COLOR_HEX)
    end_rgb = hex_to_rgb(END_COLOR_HEX)
    visible_chars = LOGO_ART.replace(' ', '').replace('\n', '').strip()
    total_visible = len(visible_chars)
    if total_visible == 0:
        print("Error: ASCII art is empty.")
        return

    char_count = 0
    output = []
    for char in LOGO_ART:
        if char == ' ' or char == '\n':
            output.append(char)
            continue
        gradient_position = char_count / (total_visible - 1) if total_visible > 1 else 0.0
        current_rgb = interpolate_color(start_rgb, end_rgb, gradient_position)
        color_code = get_color_code(current_rgb)
        output.append(f"{color_code}{char}")
        char_count += 1
    sys.stdout.write("".join(output))
    sys.stdout.write(COLOR_RESET + "\n")
    print("-" * 76)

# Product and request functions
def read_products(filename="products.csv"):
    products = {}
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                product_code = row[0]
                name = row[1]
                price = float(row[2])
                products[product_code] = {"name": name, "price": price}
    except FileNotFoundError:
        print(f"Error: Product file '{filename}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error processing product file: {e}")
        sys.exit(1)
    return products

def process_requests(filename, products_dict):
    total_items = 0
    subtotal = 0
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                product_code = row[0]
                quantity = int(row[1])
                try:
                    item = products_dict[product_code]
                except KeyError:
                    print(f"Error: unknown product ID '{product_code}' in request.csv")
                    continue
                print(f"{item['name']}: {quantity} @ {item['price']:.2f}")
                total_items += quantity
                subtotal += item['price'] * quantity
    except FileNotFoundError:
        print(f"Error: Request file '{filename}' not found.")
        sys.exit(1)
    return total_items, subtotal

# Coupon printing
def print_coupon():
    colors = ["\033[91m", "\033[92m", "\033[93m", "\033[94m", "\033[95m", "\033[96m"]
    reset = "\033[0m"
    coupon = random.choice(COUPONS)
    color = random.choice(colors)

    print("Your Exclusive Coupon")
    print("=" * 30)
    print(f"{color}>> {coupon} <<{reset}")
    print("=" * 25)

    barcode_number = "".join(str(random.randint(0, 9)) for _ in range(16))
    print("||  |||||  | ||| | |||||| | | |||")
    print("||  |||||  | ||| | |||||| | | |||")
    print("||  |||||  | ||| | |||||| | | |||")
    print(barcode_number)

# Horoscope
def print_horoscope():
    colors = ["\033[91m", "\033[92m", "\033[93m", "\033[94m", "\033[95m", "\033[96m",
              "\033[97m", "\033[90m", "\033[31m", "\033[32m", "\033[33m", "\033[34m"]
    zodiac_horoscopes = {
        "Aries": "You will trip over your own shoelaces today. But at least you'll look stylish.",
        "Taurus": "Your coffee might be cold. Smile anyway.",
        "Gemini": "Do not trust an Aquarius, they will lie to you to get what they want.",
        "Cancer": "A mysterious sock will disappear. You may never find it.",
        "Leo": "You will be almost famous today. Almost.",
        "Virgo": "Your plans may fail, but your cat will judge you silently.",
        "Libra": "Balance is important, except when it comes to pizza.",
        "Scorpio": "Beware of pens. They may betray you.",
        "Sagittarius": "Adventure awaits, probably in your backyard.",
        "Capricorn": "Hard work is important. Nap first, work later.",
        "Aquarius": "Now is the day to confess to your crush.",
        "Pisces": "Your intuition is strong. Use it to avoid laundry."
    }

    print("Daily Zodiac Horoscope:")
    random_sign = random.choice(list(zodiac_horoscopes.keys()))
    message = zodiac_horoscopes[random_sign]
    color = random.choice(colors)
    print(f"{color}{random_sign}{COLOR_RESET}: {message}")

# Main
def main():
    print_logo()
    time.sleep(2)
    print("Your one-stop shop for all your impulsive buys!\n")
    time.sleep(2)
    print("Items Purchased Summary:")

    products_dict = read_products()
    total_items, subtotal = process_requests("request.csv", products_dict)
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax

    time.sleep(2)
    print("-" * 76)
    print(f"Number of Items: {total_items}")
    print(f"Subtotal: {subtotal:.2f}")
    print(f"Sales Tax ({SALES_TAX_RATE*100:.0f}%): {sales_tax:.2f}")
    print(f"Total: {total:.2f}")
    print("-" * 76)
    time.sleep(2)

    print("Thank you for shopping at Wally World.")
    current_time = datetime.datetime.now()
    print(current_time.strftime("%a %b %d %H:%M:%S %Y"))
    return_date = current_time + datetime.timedelta(days=7)
    print(f"Returns accepted by: {return_date.strftime('%a %b %d %Y')}")
    print("-" * 76)
    time.sleep(2)

    print("Thank you for helping the planet!")
    print("♻ " * 10)
    print("-" * 76)
    time.sleep(2)

    # Lottery
    lottery_numbers = sorted(random.sample(range(1, 50), 6))
    print(f"Your lucky lottery numbers: {lottery_numbers}")
    print("-" * 76)
    time.sleep(2)

    # Horoscope
    print_horoscope()
    print("-" * 76)
    print("♻ " * 10)
    time.sleep(2)

    # Extra coupons
    for _ in range(5):
        time.sleep(2)
        print_coupon()
        print("-" * 76)

    print("Signature: __________________________")
    print("\nHave a great day!")

if __name__ == "__main__":
    main()
