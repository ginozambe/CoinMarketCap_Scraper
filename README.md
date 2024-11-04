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

## Email Configuration:

This script supports both Gmail and Hotmail (Outlook). Depending on your email provider, follow the respective setup instructions:

### For Gmail:
Recommended: Use App Passwords for enhanced security.
Go to your Google account security settings.
Enable "Two-Step Verification."
Generate an app password and use it in place of your regular password in the script.

### For Hotmail (Outlook):
Enable "Two-step verification" for your Microsoft account.
Generate an app password:
Go to your Microsoft account security settings.
Enable "Two-step verification."
Generate an app password and use it in place of your regular password in the script.
Run the Script: Execute the script in your terminal:

```bash
python your_script_name.py
```

Follow the prompt to enter the cryptocurrency symbol you want to track (e.g., RENDER, BTC).

### Usage
The script runs indefinitely, fetching and saving data every minute. You can stop it using Ctrl+C.
