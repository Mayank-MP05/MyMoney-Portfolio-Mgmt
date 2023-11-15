from src.utils import constants

class AssetType:
    def __init__(self, name):
        self.name = name
        self.initial_allocation_percentage = 0.0
        self.current_balance = 0.0
        self.sip_amt = 0.0
        self.month_to_closing_balance_map = {}
    
    def allocate_initial_capital(self, amt, allocation_percentage):
        self.current_balance = amt
        self.initial_allocation_percentage = allocation_percentage
        
    def set_sip_amt(self, sip_amt):
        self.sip_amt = sip_amt
        
    def get_balance_by_month(self, month_enum):
        return self.month_to_closing_balance_map[month_enum]
    
    def set_balance_by_month(self, month_enum, balance):
        self.month_to_closing_balance_map[month_enum] = balance
    
    def get_current_balance(self):
        return self.current_balance
    
    def set_current_balance(self, current_balance):
        self.current_balance = current_balance
    
    def get_rebalance_amt(self, total_balance):
        # Check if minimum 6 months data is available
        if(len(self.month_to_closing_balance_map) < constants.MIN_MONTHS_FOR_RE_BALANCING):
            print("CANNOT_REBALANCE")
            return None
        else:
            updated_balance = total_balance * self.initial_allocation_percentage
            self.current_balance = updated_balance
            return updated_balance
