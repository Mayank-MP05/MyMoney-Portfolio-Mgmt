from src.models.asset_type import AssetType
from src.configs.constants import MonthEnums
import logging
logger = logging.getLogger(__name__)


class Portfolio:
    """Portfolio Class
    - Class will be used to represent one portfolio
    - It can have mulitple asset classes
    - All centralized commands like rebalance, get and print balance will be here
    """
    
    def __init__(self):
        # Initialization of the asset classes in a portfolio
        self._equity = AssetType("equity")
        self._debt = AssetType("debt")
        self._gold = AssetType("gold")
      
    def allocate_command(self, equity_amt, debt_amt, gold_amt):
        # Calculate the overall amt 
        overall_amt = equity_amt + debt_amt + gold_amt
        
        # Calculate the allocation percentage based on that
        equity_initial_allocation =  equity_amt/overall_amt
        debt_initial_allocation =  debt_amt/overall_amt
        gold_initial_allocation =  gold_amt/overall_amt
        
        # Set the amount and initial allocation percentage
        self._equity.allocate_initial_capital(equity_amt, equity_initial_allocation)
        self._debt.allocate_initial_capital(debt_amt, debt_initial_allocation)
        self._gold.allocate_initial_capital(gold_amt, gold_initial_allocation)

    def sip_command(self, equity_amt, debt_amt, gold_amt):
        # Set sip amount for the Asset types
        self._equity.set_sip_amt(equity_amt)
        self._debt.set_sip_amt(debt_amt)
        self._gold.set_sip_amt(gold_amt)
        pass
    
    def change_command(self, equity_change, debt_change, gold_change, month_enum):
        self._equity.add_sip_and_monthly_change(equity_change, month_enum)
        self._debt.add_sip_and_monthly_change(debt_change, month_enum)
        self._gold.add_sip_and_monthly_change(gold_change, month_enum)
        
        # For June and December, we have to rebalance the portfolio
        if month_enum in [MonthEnums.JUNE ,MonthEnums.DECEMBER]:
            logger.debug(f"Trigger re_balance -> {month_enum}")
            self.execute_re_balance_command()
        

    def balance_command(self, month_enum):
        """prints the balance of different asset classes in the portfolio
        """
        # Calculate the allocation percentage based on that
        equity_balance = self._equity.get_balance_by_month(month_enum)
        debt_balance = self._debt.get_balance_by_month(month_enum)
        gold_balance = self._gold.get_balance_by_month(month_enum)
        
        print(f'{int(equity_balance)} {int(debt_balance)} {int(gold_balance)}')
    
    def execute_re_balance_command(self):
        # Get the current balance of each fund
        equity_balance = self._equity.get_current_balance()
        debt_balance = self._debt.get_current_balance()
        gold_balance = self._gold.get_current_balance()
        
        # Calculate total fund size
        total_balance = equity_balance + debt_balance + gold_balance
        
        equity_re_balance_amt = self._equity.execute_re_balance_command(total_balance)
        if(equity_re_balance_amt == None):
            return
        
        debt_re_balance_amt = self._debt.execute_re_balance_command(total_balance)
        gold_re_balance_amt = self._gold.execute_re_balance_command(total_balance)
        
        logger.debug(f"re_balance -> {equity_re_balance_amt} {debt_re_balance_amt} {gold_re_balance_amt}")

    def print_last_re_balance_amt_command(self):
        equity_re_balance_amt = self._equity.get_last_re_balance_amt()
        if(equity_re_balance_amt == None):
            print("CANNOT_REBALANCE")
            return
        debt_re_balance_amt = self._debt.get_last_re_balance_amt()
        gold_re_balance_amt = self._gold.get_last_re_balance_amt()
        print(f'{int(equity_re_balance_amt)} {int(debt_re_balance_amt)} {int(gold_re_balance_amt)}')
        