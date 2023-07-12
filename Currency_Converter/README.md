# Currency Converter

This is a simple Currency Converter program implemented in Python. It allows users to convert amounts between different currencies based on the current exchange rates.

## Features

- Convert currency from one currency to another
- Fetches real-time exchange rates using an API
- Supports a wide range of currencies

## Prerequisites

Before running the Currency Converter program, make sure you have the following prerequisites:

- Python 3.x installed on your system
- Internet connectivity to fetch the exchange rates from an API

## Getting Started

1. Clone the repository to your local machine:

```shell
git clone https://github.com/soorjya/currency-converter.git
```
2. Navigate to the project directory:
```shell


cd currency-converter
```
3. Install the required dependencies:
```shell


pip install requests
```
4. Run the Currency Converter program:
```shell


python converter.py
```


## Usage
- Enter the amount you want to convert.
- Select the source currency (the currency you have).
- Select the target currency (the currency you want to convert to).
- The program will display the converted amount based on the current exchange rate.


## Example

Example Input:

```mathematica

Enter amount: 100
Enter source currency: USD
Enter target currency: EUR
```

```yaml
Converted amount: 86.76 EUR
```


## Customize
You can customize the Currency Converter program by modifying the following:

- Add or remove currencies in the `currencies` list in the `converter.py` file.
- Implement additional features or enhancements based on your requirements.


## Credits
Exchange rates are fetched from the ExchangeRate-API service
