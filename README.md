# CoinMarketCap Web Scraper

This script fetches cryptocurrency price and market cap data from the CoinMarketCap API at minute intervals and sends the data via email. It allows you to track the price of any cryptocurrency symbol of your choice.

## Features
- Fetches cryptocurrency price and market cap data.
- Saves the data to an Excel file with timestamps.
- Sends an email with the Excel file attached.
- Supports tracking any cryptocurrency symbol.

## Requirements
- Python 3.x
- Required libraries:
  - `requests`
  - `pandas`
  - `yagmail`
  - `openpyxl` (for Excel file support)

You can install the required libraries using pip:

```bash
pip install requests pandas yagmail openpyxl
```

## Setup
API Key: Obtain your CoinMarketCap API key and replace 'your_api_key' in the script with your actual key.

### Email Configuration:

By default, the yagmail library is configured to work with Gmail's SMTP server. Follow the respective setup instructions below:

- Enable "Two-Step Verification" in your Google account security settings.
- Generate an app password.
- Use the app password in place of your regular password in the script.

### Run the Script: 

Make sure you are in the directory where your script is located. Then, execute the script in your terminal:

```bash
python crypto_price_update.py
```

Follow the prompt to enter the cryptocurrency symbol you want to track (e.g., RENDER, BTC).

## Usage
The script runs indefinitely, fetching and saving data every minute. You can stop it by pressing **Ctrl+C** or by closing the command line interface.


## Final Result

 ![Analysis](<examples/RENDER_EMAIL.png>)
  ![Analysis](<examples/RENDER_SPREADSHEET.png>)