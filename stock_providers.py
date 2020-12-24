import csv


class StockData:
    def __init__(self, ticket, market_cap,  last_price):
        self.ticket = ticket
        self.market_cap = market_cap
        self.last_price = last_price

    def __repr__(self):
        return "Ticket: {0}, Market Capitalization: {1}, Last Price: {2}"\
            .format(self.ticket, self.market_cap, self.last_price)


def read_stock_data_from_csv(filename):
    """
    Read StockData from CSV file
    :param filename: path to source CSV, i.e. sp100_stock_data.csv
    :return: list[StockData]
    """
    result = list()
    with open(filename, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                stock_data = StockData(row[0], int(row[1]), float(row[2]))
                print(f'Successfully Read [{stock_data}]')
                line_count += 1
                result.append(stock_data)
        print(f'Processed {line_count} lines.')
    return result

