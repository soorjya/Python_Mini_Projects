import requests

# Function to convert currency
def convert_currency(amount, from_currency, to_currency):
    # API Endpoint
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"

    try:
        # Fetch exchange rates
        response = requests.get(url)
        data = response.json()

        # Calculate converted amount
        converted_amount = amount * data['rates'][to_currency]

        # Return converted amount
        return converted_amount

    except requests.exceptions.RequestException as e:
        print("Error occurred:", e)
        return None

# Example usage
amount = 100
from_currency = 'USD'
to_currency = 'EUR'

converted_amount = convert_currency(amount, from_currency, to_currency)
if converted_amount is not None:
    print(f"{amount} {from_currency} = {converted_amount} {to_currency}")
