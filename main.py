from stock_core.calculations import calc_shares_by_market_cap, calc_index_price, calc_buying_sequence
from stock_core.indexes import get_sp100
from stock_core.stock_providers import read_stock_data_from_csv
from stock_core.portfolios import get_portfolio


def main():
    symbols = get_sp100()
    print(f'S&P100 tickets: {symbols}.')

    # Get the stock data
    stkdata = read_stock_data_from_csv('example_data/sp100_stock_data.csv')

    # Calc the distribution based on stock's market cap
    shares_distribution = calc_shares_by_market_cap(stkdata)
    print(shares_distribution)
    index_distribution = calc_index_price(shares_distribution, stkdata, 45000)
    portfolio = get_portfolio()
    buying_sequence = calc_buying_sequence(shares_distribution, index_distribution, portfolio, stkdata)
    for item in buying_sequence:
        print(item)


if __name__ == '__main__':
    main()
