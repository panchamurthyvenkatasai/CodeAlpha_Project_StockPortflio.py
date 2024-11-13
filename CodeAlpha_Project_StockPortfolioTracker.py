
class Stock:
    def __init__(self, symbol, quantity, purchase_price):
        self.symbol = symbol
        self.quantity = quantity
        self.purchase_price = purchase_price
        self.current_price = purchase_price  # Initialize current price as purchase price

    def update_current_price(self, new_price):
        self.current_price = new_price

    def total_value(self):
        return self.quantity * self.current_price

    def gain_loss(self):
        return (self.current_price - self.purchase_price) * self.quantity


class Portfolio:
    def __init__(self, holder_name):
        self.holder_name = holder_name
        self.stocks = []

    def add_stock(self, symbol, quantity, purchase_price):
        self.stocks.append(Stock(symbol, quantity, purchase_price))

    def update_stock_price(self, symbol, new_price):
        for stock in self.stocks:
            if stock.symbol == symbol:
                stock.update_current_price(new_price)
                break

    def calculate_total_value(self):
        return sum(stock.total_value() for stock in self.stocks)

    def display_portfolio(self):
        print(f"Portfolio Holder: {self.holder_name}")
        print("Stock Portfolio:")
        for stock in self.stocks:
            print(f"{stock.symbol}: {stock.quantity} shares @ ${stock.purchase_price:.2f} (Current: ${stock.current_price:.2f})")
            print(f"Total Value: ${stock.total_value():.2f}, Gain/Loss: ${stock.gain_loss():.2f}")
        print(f"Total Portfolio Value: ${self.calculate_total_value():.2f}")


def main():
    # Create a portfolio for a holder
    portfolio = Portfolio("John Doe")

    # Add stocks to the portfolio
    portfolio.add_stock("AAPL", 10, 150.0)
    portfolio.add_stock("GOOG", 5, 2500.0)
    portfolio.add_stock("MSFT", 20, 200.0)

    # Display the initial portfolio
    print("Initial Portfolio:")
    portfolio.display_portfolio()

    # Update the price of a stock
    portfolio.update_stock_price("AAPL", 160.0)

    # Display the updated portfolio
    print("\nUpdated Portfolio:")
    portfolio.display_portfolio()


if __name__ == "__main__":
    main()
