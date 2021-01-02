from stock_core.calculations import calc_shares_by_market_cap
from stock_core.stock_providers import StockData
import pytest


class TestCalculations:

    @pytest.fixture
    def tickets_with_prices(self):
        return [
            StockData('A1', 40, 100),
            StockData('A2', 20, 100),
            StockData('A3', 20, 100)
        ]

    def test_shares_by_market_cap(self, tickets_with_prices):
        result = calc_shares_by_market_cap(tickets_with_prices)
        expected = {
            'A1': 0.5,
            'A2': 0.25,
            'A3': 0.25
        }
        assert result == expected

