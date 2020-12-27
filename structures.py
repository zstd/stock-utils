

class Portfolio:

    def __init__(self, liquidity, positions):
        self.liquidity = liquidity
        self.positions = positions

    def get_count(self, ticket):
        return self.positions.get(ticket, 0)

class Position:
    def __init__(self, ticket, index_share, target_count, portfolio_count, price):
        self.ticket = ticket
        self.index_share = index_share
        self.target_count = target_count
        self.portfolio_count = portfolio_count
        self.price = price
        self.count_delta = self.target_count - self.portfolio_count

    def __repr__(self):
        return "Ticket {0}, price {1} index share {2}, target_count {3}, in portfolio {4}, count_delta {5}". \
            format(self.ticket, self.price, self.index_share, self.target_count, self.portfolio_count, self.count_delta)

