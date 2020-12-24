

def calc_shares_by_market_cap(stock_data):
    total = 0
    result = {}
    for item in stock_data:
        total += item.market_cap
    print(f'Total market cap {total} .')
    for item in stock_data:
        result[item.ticket] = item.market_cap/total
    return dict(sorted(result.items(), key=lambda item: item[1], reverse=True))
