import requests

class Stock:
    def __init__(self, symbol, quantity, purchase_price):
        self.symbol = symbol
        self.quantity = quantity
        self.purchase_price = purchase_price

class Portfolio:
    def __init__(self):
        self.stocks = []

    def add_stock(self, stock):
        self.stocks.append(stock)

    def remove_stock(self, symbol):
        self.stocks = [s for s in self.stocks if s.symbol != symbol]

    def get_portfolio_value(self):
        total_value = 0
        for stock in self.stocks:
            data = self.get_stock_data(stock.symbol)
            if data:
                current_price = float(data['Global Quote']['05. price'])
                total_value += current_price * stock.quantity
        return total_value

    def get_stock_data(self, symbol):
        url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey=YOUR_API_KEY"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print("Error fetching data")
            return None

# Example usage:
if __name__ == "__main__":
    portfolio = Portfolio()

    # Adding stocks to the portfolio
    portfolio.add_stock(Stock("AAPL", 10, 150.25))
    portfolio.add_stock(Stock("GOOGL", 5, 2500.75))
    portfolio.add_stock(Stock("MSFT", 8, 300.50))

    # Removing a stock from the portfolio
    portfolio.remove_stock("GOOGL")

    # Getting the total portfolio value
    portfolio_value = portfolio.get_portfolio_value()
    print("Total Portfolio Value:", portfolio_value)
