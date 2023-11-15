import logging
logger = logging.getLogger(__name__)
from src.models.asset_type import AssetType

class MainHandler:
    def __init__(self):
        self._equity = AssetType("equity")
        self._debt = AssetType("debt")
        self._gold = AssetType("gold")
        
        pass
    
    def process_one_line(self, input_line):
        token_list = input_line.split(" ")
        command_enum = token_list[0]
        logger.debug(token_list)
        self.process_token_list(command_enum, token_list)
        
    def process_token_list(self, command_enum, token_list):
        if (command_enum == 'ALLOCATE'):
            equity_amt = float(token_list[1])
            debt_amt = float(token_list[2])
            gold_amt = float(token_list[3])
            self.allocate_command(equity_amt, debt_amt, gold_amt)
        elif (command_enum == 'SIP'): 
            equity_amt = float(token_list[1])
            debt_amt = float(token_list[2])
            gold_amt = float(token_list[3])
            self.sip_command(equity_amt, debt_amt, gold_amt)
        elif (command_enum == 'CHANGE'):
            equity_change = float(token_list[1].replace("%",""))
            debt_change = float(token_list[2].replace("%",""))
            gold_change = float(token_list[3].replace("%",""))
            month_enum = token_list[4]
            self.change_command(equity_change, debt_change, gold_change, month_enum)
        elif (command_enum == 'BALANCE'):
            month_enum = token_list[1] 
            self.balance_command(month_enum)
        elif (command_enum == 'REBALANCE'):
            self.rebalance_command()
            
    def allocate_command(self, equity_amt, debt_amt, gold_amt):
        # Calculate the overall amt 
        overall_amt = equity_amt + debt_amt + gold_amt
        
        # Calculate the allocation percentage based on that
        equity_initial_allocation =  equity_amt/overall_amt
        debt_initial_allocation =  debt_amt/overall_amt
        gold_initial_allocation =  gold_amt/overall_amt
        
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
        equity_sip_amt = 0
        debt_sip_amt = 0
        gold_sip_amt = 0
        
        # Month is january then dont add sip
        if(month_enum == 'JANUARY'):
            equity_sip_amt = 0    
            debt_sip_amt = 0
            gold_sip_amt = 0
        
        # If month is not jan, 
        # add SIP amt first, 
        # then make changes update the balance
        # update the mapping
        else:
            # Get the current balance of each fund
            equity_sip_amt = self._equity.sip_amt
            debt_sip_amt = self._debt.sip_amt
            gold_sip_amt = self._gold.sip_amt
            
        equity_balance = self._equity.get_current_balance()
        debt_balance = self._debt.get_current_balance()
        gold_balance = self._gold.get_current_balance()

        updated_equity_balance = (equity_balance + equity_sip_amt) * (1 + (equity_change/100))
        updated_debt_balance = (debt_balance + debt_sip_amt) * (1 + (debt_change/100))
        updated_gold_balance = (gold_balance + gold_sip_amt) * (1 + (gold_change/100))
        logger.debug(f'change {month_enum} {int(updated_equity_balance)} {int(updated_debt_balance)} {int(updated_gold_balance)}')

        self._equity.set_current_balance(updated_equity_balance)
        self._debt.set_current_balance(updated_debt_balance)
        self._gold.set_current_balance(updated_gold_balance)
        pass
    
    def balance_command(self, month_enum):
        # Calculate the allocation percentage based on that
        equity_balance = self._equity.get_balance_by_month(month_enum)
        debt_balance = self._debt.get_balance_by_month(month_enum)
        gold_balance = self._gold.get_balance_by_month(month_enum)
        
        print(f'{int(equity_balance)} {int(debt_balance)} ${int(gold_balance)}')
        pass
    
    def rebalance_command():
        # Get the current balance of each fund
        equity_balance = self._equity.get_current_balance()
        debt_balance = self._debt.get_current_balance()
        gold_balance = self._gold.get_current_balance()
        
        # Calculate total fund size
        total_balance = equity_balance + debt_balance + gold_balance
        
        equity_rebalance_amt = self._equity.get_rebalance_amt(total_balance)
        if(equity_rebalance_amt == None):
            return
        
        debt_rebalance_amt = self._debt.get_rebalance_amt(total_balance)
        gold_rebalance_amt = self._gold.get_rebalance_amt(total_balance)
        
        print(f'{int(equity_rebalance_amt)} {int(debt_rebalance_amt)} ${int(gold_rebalance_amt)}')
        
