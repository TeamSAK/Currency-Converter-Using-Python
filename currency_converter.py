CONVERSION_RATES = {
    'USD': 1.0,    # Base currency
    'PKR': 280.0,
    'EUR': 0.85,
    'GBP': 0.75,
    'JPY': 110.0,
    'AUD': 1.35,
    'CAD': 1.34,
    'CHF': 0.92,
    'CNY': 6.90,
    'INR': 83.0,
    'MXN': 18.0,
    'NZD': 1.42,
    'SGD': 1.36,
    'HKD': 7.85,
    'KRW': 1330.0,
    'BRL': 5.30,
    'RUB': 75.0,
    'SEK': 9.0,
    'TRY': 27.0,
    'ZAR': 19.0
}

# Function to convert between any two currencies
def convert_currency(amount, from_currency, to_currency):
    if from_currency not in CONVERSION_RATES or to_currency not in CONVERSION_RATES:
         return None
    # Convert amount to USD, then to target currency
    amount_in_usd = amount / CONVERSION_RATES[from_currency]
    return amount_in_usd * CONVERSION_RATES[to_currency]

# Main function
def main():
    while True:
        print("\nCurrency Converter")
        print("Available currencies:", ', '.join(CONVERSION_RATES.keys()))
        
        try:
            amount = float(input("Enter the amount: "))
            from_currency = input("Enter the currency to convert from: ").upper()
            to_currency = input("Enter the currency to convert to: ").upper()
            
            if from_currency in CONVERSION_RATES and to_currency in CONVERSION_RATES:
                converted_amount = convert_currency(amount, from_currency, to_currency)
                print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
            else:
                print("Invalid currency. Please enter a valid currency from the list.")
        except ValueError:
            print("Invalid input. Please enter a valid number for the amount.")
        
        # Ask if the user wants to continue or exit
        continue_choice = input("\nDo you want to perform another conversion? (yes/no): ").strip().lower()
        if continue_choice != 'yes':
            print("Exiting the program. Goodbye!")
            break

if __name__ == "__main__":
    main()
