from stock_core.structures import Portfolio


def get_portfolio():
    """
        Very naive implementation that returns hardcoded portfolio.
        For testing purposes.
    """

    return Portfolio(1600, {
        'AAPL': 8,
        'FB': 1,
        'INTC': 9,
        'MA': 1,
        'MCD': 1,
        'MRK': 3,
        'MSFT': 1,
        'PG': 1,
        'V': 1,
        'DIS': 1
    })