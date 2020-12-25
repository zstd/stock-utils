

def calc_shares_by_market_cap(stock_data):
    total = 0
    result = {}
    for item in stock_data:
        total += item.market_cap
    print(f'Total market cap {total} .')
    for item in stock_data:
        result[item.ticket] = item.market_cap/total
    return dict(sorted(result.items(), key=lambda item: item[1], reverse=True))


def calc_index_price(distributions, market_data, limit):
    """
    Very naive algorithm to calculate the minimum sum needed to buy full index
     according to the stock's distribution.
    :param distributions: dict[ticket:str, share:float] with stock shares in index
    :param market_data: list[StockData] collection of market data
    :param limit: the limit of money to spend
    :return: dict[ticker:str, amount of stocks to buy]
    """
    result = {}
    skipped = []
    ticket_prices = {}
    limit_left = limit
    for item in market_data:
        ticket_prices[item.ticket] = item.last_price
    for ticket in distributions.keys():
        share = distributions[ticket]
        price = ticket_prices[ticket]
        price_limit = share * limit
        stocks_amount = round(price_limit / price)

        if stocks_amount > 0:
            result[ticket] = stocks_amount
            limit_left = limit_left - stocks_amount * price
            print(f'Processing: {ticket}, share {share}, price {price}, '
                  f'price_limit {price_limit}, stocks_amount {stocks_amount}, limit_left {limit_left}')

        else:
            print(f'Skipping {ticket} - Not able to buy at least 1 stock')
            skipped.append(ticket)

        if limit_left < 0:
            raise RuntimeError("No limit left to buy stocks")
    print(f'limit left {limit_left}')
    print(f'skipped ticket {skipped}')
    skipped_share = 0
    for ticket in skipped:
        skipped_share = skipped_share + distributions[ticket]
    print(f'skipped share {skipped_share}')
    return result

