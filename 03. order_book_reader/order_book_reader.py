import requests
import tkinter as tk
from tkinter import ttk
import time

root = tk.Tk()
root.title("Order book statistics")
root.geometry("400x200")

# Replace YOUR_API_KEY with your Binance API key
headers = {'X-MBX-APIKEY': 'YOUR_API_KEY'}

# Define the symbol you want to access
symbol = 'BTCUSDT'

# Create labels to display the results
buy_count_label = ttk.Label(root, text="Total buy count: ")
buy_count_label.pack()

sell_count_label = ttk.Label(root, text="Total sell count: ")
sell_count_label.pack()

buy_value_label = ttk.Label(root, text="Total buy value: ")
buy_value_label.pack()

sell_value_label = ttk.Label(root, text="Total sell value: ")
sell_value_label.pack()


def update():
    response = requests.get(f'https://api.binance.com/api/v3/depth?symbol={symbol}&limit=100', headers=headers)
    if response.status_code == 200:
        # Parse the response into a dictionary
        data = response.json()
        # Counting the number of buy and sell orders
        buy_count = 0
        sell_count = 0
        # Calculating the total value of buy and sell orders
        buy_value = 0
        sell_value = 0
        for bid in data['bids']:
            buy_count += float(bid[1])
            buy_value += float(bid[1]) * float(bid[0])
        for ask in data['asks']:
            sell_count += float(ask[1])
            sell_value += float(ask[1]) * float(ask[0])
        # Update the labels with the new values
        buy_count_label.config(text=f"Total buy count: {buy_count:.3f} BTC")
        sell_count_label.config(text=f"Total sell count: {sell_count:.3f} BTC")
        buy_value_label.config(text=f"Total buy value: {buy_value:.3f} USDT")
        sell_value_label.config(text=f"Total sell value: {sell_value:.3f} USDT")
    else:
        print(f'Error: {response.status_code}')
    # Schedule the next update
    root.after(3000, update)


# Schedule the first update
root.after(3000, update)

root.mainloop()
