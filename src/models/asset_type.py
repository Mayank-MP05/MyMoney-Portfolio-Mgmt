class AssetType:
    def __init__(self, name):
        self.name = name
        self.initial_allocation_percentage = 0.0
        self.current_balance = 0
        self.month_to_closing_balance_map = {}
        pass
    
    def allocate_initial_capital(self, amt, allocation_percentage):
        self.current_balance = amt
        self.initial_allocation_percentage = allocation_percentage
        
    
    def monthly_change(self, change, month_enum):
        pass