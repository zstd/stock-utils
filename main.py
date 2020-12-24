from calculations import calc_shares_by_market_cap
from indexes import get_sp100
from stock_providers import read_stock_data_from_csv


def main():
    symbols = get_sp100()
    print(f'S&P100 tickets: {symbols}.')

    # Get the stock data
    stkdata = read_stock_data_from_csv('example_data/sp100_stock_data.csv')

    # Calc the distribution based on stock's market cap
    result = calc_shares_by_market_cap(stkdata)
    print(result)


if __name__ == '__main__':
    main()