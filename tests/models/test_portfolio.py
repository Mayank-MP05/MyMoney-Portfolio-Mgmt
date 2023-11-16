from src.models.portfolio import Portfolio
from tests.config.constants import GOLD_AMT, DEBT_AMT, EQUITY_AMT
import unittest

class TestPortfolio(unittest.TestCase):
    def test_allocate_command(self):
        self._portfolio = Portfolio()
        overall_amt = EQUITY_AMT + DEBT_AMT + GOLD_AMT
        
        # Set the amount and initial allocation percentage will be calculated
        self._portfolio._equity.allocate_initial_capital(EQUITY_AMT, overall_amt)
        self._portfolio._debt.allocate_initial_capital(DEBT_AMT, overall_amt)
        self._portfolio._gold.allocate_initial_capital(GOLD_AMT, overall_amt)
        
        self.assertEqual( self._portfolio._equity.current_balance, EQUITY_AMT)
        self.assertEqual( self._portfolio._debt.current_balance, DEBT_AMT)
        self.assertEqual( self._portfolio._gold.current_balance, GOLD_AMT)

    def test_sip_command(self):
        self._portfolio = Portfolio()
        # Set sip amount for the Asset types
        self._portfolio._equity.set_sip_amt(EQUITY_AMT)
        self._portfolio._debt.set_sip_amt(DEBT_AMT)
        self._portfolio._gold.set_sip_amt(GOLD_AMT)
        
        self.assertEqual( self._portfolio._equity.sip_amt, EQUITY_AMT)
        self.assertEqual( self._portfolio._debt.sip_amt, DEBT_AMT)
        self.assertEqual( self._portfolio._gold.sip_amt, GOLD_AMT)
