import requests
import tkinter as tk
from tkinter import ttk

# Function to fetch coin price
def get_price():
    coin = coin_var.get().lower()
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": coin, "vs_currencies": "usd"}
    try:
        response = requests.get(url, params=params)
        data = response.json()
        price = data[coin]["usd"]
        result_label.config(text=f"{coin.capitalize()} Price: ${price}")
    except Exception as e:
        result_label.config(text=f"Error: {e}")

# GUI window
root = tk.Tk()
root.title("Crypto Price Viewer")
root.geometry("300x200")

# Coin selection
coin_var = tk.StringVar()
coin_label = tk.Label(root, text="Choose Coin:")
coin_label.pack(pady=5)

coins = ["bitcoin", "ethereum", "dogecoin", "solana", "litecoin", "Sui"]
coin_dropdown = ttk.Combobox(root, textvariable=coin_var, values=coins, state="readonly")
coin_dropdown.current(0)
coin_dropdown.pack(pady=5)

# Get Price Button
get_price_btn = tk.Button(root, text="Get Price", command=get_price)
get_price_btn.pack(pady=5)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
