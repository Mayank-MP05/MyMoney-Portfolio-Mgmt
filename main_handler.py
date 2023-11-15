import logging
logger = logging.getLogger(__name__)

class MainHandler:
    def __init__(self):
        pass
    
    def process_one_line(self, input_line):
        token_list = input_line.split(" ")
        command_enum = token_list[0]
        logger.debug(token_list)
        process_token_list(command_enum, token_list)
        
    def process_token_list(self, command_enum, token_list):
        if (command_enum == 'ALLOCATE'):
            equity_amt = float(token_list[1])
            debt_amt = float(token_list[2])
            gold_amt = float(token_list[3])
            allocate_command(equity_amt, debt_amt, gold_amt)
        elif (command_enum == 'SIP'): 
            equity_amt = float(token_list[1])
            debt_amt = float(token_list[2])
            gold_amt = float(token_list[3])
            sip_command(equity_amt, debt_amt, gold_amt)
        elif (command_enum == 'CHANGE'):
            equity_change = float(token_list[1].replace("%",""))
            debt_change = float(token_list[2].replace("%",""))
            gold_change = float(token_list[3].replace("%",""))
            month_enum = token_list[4]
            change_command(equity_change, debt_change, gold_change, month_enum)
        elif (command_enum == 'BALANCE'):
            month_enum = token_list[1] 
            balance_command(month_enum)
        elif (command_enum == 'REBALANCE'):
            rebalance_command()
            
    def allocate_command(equity_amt, debt_amt, gold_amt):
        pass
    
    def sip_command(equity_amt, debt_amt, gold_amt):
        pass
    
    def change_command(equity_change, debt_change, gold_change, month_enum):
        pass
    
    def balance_command(month_enum):
        pass
    
    def rebalance_command():
        pass
