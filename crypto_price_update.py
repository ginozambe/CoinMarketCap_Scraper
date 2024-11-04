import requests
import pandas as pd
from datetime import datetime
import yagmail
import time

# Define your CoinMarketCap API key (replace 'your_api_key' with your actual key)
# Replace with your actual API key
CMC_API_KEY = 'your_api_key'
URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
EMAIL = "your_email_address"  # Use your actual email

# Get asset symbol from user input
ASSET_SYMBOL = input(
    "Enter the cryptocurrency symbol you want to track (e.g., RENDER, BTC): ").upper()


def get_asset_data(asset_symbol):
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': CMC_API_KEY,
    }
    parameters = {
        'symbol': asset_symbol,
        'convert': 'USD'
    }

    response = requests.get(URL, headers=headers, params=parameters)
    data = response.json()

    if 'data' in data and asset_symbol in data['data']:
        price = data['data'][asset_symbol]['quote']['USD']['price']
        market_cap = data['data'][asset_symbol]['quote']['USD']['market_cap']
        return round(price, 2), round(market_cap, 2)
    else:
        raise Exception("Error fetching data from CoinMarketCap")


def save_to_excel(price, market_cap, asset_symbol):
    # Record current date and time
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    df = pd.DataFrame([[timestamp, price, market_cap]], columns=[
                      'Timestamp', 'Price (USD)', 'Market Cap (USD)'])

    # Append or create new file
    # Filename includes the asset symbol
    file_name = f'{ASSET_SYMBOL}_Price_Updates.xlsx'
    try:
        existing_df = pd.read_excel(file_name)
        # Check if the last entry in the existing file is from the current minute
        last_entry_time = existing_df['Timestamp'].iloc[-1]
        if datetime.strptime(last_entry_time, '%Y-%m-%d %H:%M:%S').minute == datetime.now().minute:
            print("An entry for this minute already exists. Skipping this update.")
            return None  # Skip saving if already exists
        df = pd.concat([existing_df, df], ignore_index=True)
    except FileNotFoundError:
        pass  # File will be created if it does not exist

    df.to_excel(file_name, index=False)
    return file_name


def send_email(file_name, asset_symbol):
    yag = yagmail.SMTP("your_email_address",
                       "your_app_password")  # Use App Password
    subject = f"Minute-Level {asset_symbol} Price and Market Cap Update"
    contents = [
        f"Attached is the minute-level price and market cap update for {
            asset_symbol}.",
        file_name
    ]
    yag.send(to=EMAIL, subject=subject, contents=contents)


def main():
    while True:
        try:
            price, market_cap = get_asset_data(ASSET_SYMBOL)
            file_name = save_to_excel(price, market_cap, ASSET_SYMBOL)
            if file_name:
                send_email(file_name, ASSET_SYMBOL)
                print(f"Minute-level price and market cap update sent successfully for {
                      ASSET_SYMBOL} at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}!")
        except Exception as e:
            print(f"An error occurred: {e}")

        # Wait for 1 minute before the next iteration
        time.sleep(60)  # Sleep for 60 seconds (1 minute)


if __name__ == '__main__':
    main()
