import tkinter as tk
import yfinance as yf

def get_stock_info(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info
    current_price = info['targetHighPrice']
    market_cap = info['totalCash']
    return f"Current Price: {current_price} | Market Cap: {market_cap}"



# create a tkinter window
window = tk.Tk()
window.title("Stock Market Tracker")
window.geometry("400x200")

# create a label for the stock ticker
ticker_label = tk.Label(text="Stock Ticker:")
ticker_label.pack()

# create an entry for the stock ticker
ticker_entry = tk.Entry()
ticker_entry.pack()

# create a label for the stock information
info_label = tk.Label(text="")
info_label.pack()


# create a button to get stock information
get_info_button = tk.Button(text="Get Info", command=lambda: update_info_label(ticker_entry.get()))
get_info_button.pack()

def update_info_label(ticker):
    info = get_stock_info(ticker)
    info_label.config(text=info)


# start the tkinter event loop
window.mainloop()
