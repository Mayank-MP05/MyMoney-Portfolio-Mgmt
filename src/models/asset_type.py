from src.configs.constants import MonthEnums
from src.configs import constants

class AssetType:
    def __init__(self, name):
        self.name = name
        self.initial_allocation_percentage = 0.0
        self.current_balance = 0.0
        self.sip_amt = 0.0
        self.month_to_closing_balance_map = {}
        self.last_re_balance_amt = None
    
    def allocate_initial_capital(self, amt, overall_amt):
        self.current_balance = amt
        # Calculate the allocation percentage based on that
        allocation_percentage = amt / overall_amt
        self.initial_allocation_percentage = allocation_percentage
        
    def set_sip_amt(self, sip_amt):
        self.sip_amt = sip_amt
        
    def get_balance_by_month(self, month_enum):
        return self.month_to_closing_balance_map[month_enum]
    
    def get_current_balance(self):
        return self.current_balance
    
    def set_current_balance(self, current_balance, month_enum):
        self.current_balance = current_balance
        self.month_to_closing_balance_map[month_enum] = current_balance
    
    def execute_re_balance_command(self, total_balance):
        # Check if minimum 6 months data is available
        if(len(self.month_to_closing_balance_map) < constants.MIN_MONTHS_FOR_RE_BALANCING):
            self.last_re_balance_amt = None
            return None
        else:
            updated_balance = int(total_balance * self.initial_allocation_percentage)
            self.current_balance = updated_balance
            self.last_re_balance_amt = updated_balance
            return updated_balance

    def get_last_re_balance_amt(self):
        return self.last_re_balance_amt
    
    def add_sip_and_monthly_change(self, monthly_change, month_enum):
        current_balance = self.get_current_balance()
        if(month_enum == MonthEnums.JANUARY):
            # Month is january then dont add sip
            sip_amt = 0
        else:
            # If month is not jan, add SIP amt first, 
            sip_amt = self.sip_amt
       
        # then make changes update the balance
        updated_balance = int((self.current_balance + sip_amt) * (1 + (monthly_change/100)))
        self.set_current_balance(updated_balance,month_enum)
        pass