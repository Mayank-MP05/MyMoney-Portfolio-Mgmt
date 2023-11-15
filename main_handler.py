
from src.models.asset_type import AssetType
from src.models.portfolio import Portfolio
from src.configs import constants

import logging
logger = logging.getLogger(__name__)

class MainHandler:
    def __init__(self):
        self._portfolio = Portfolio()
    
    def process_one_line(self, input_line):
        token_list = input_line.split(" ")
        command_enum = token_list[0]
        logger.debug(token_list)
        self.process_token_list(command_enum, token_list)
        
    def process_token_list(self, command_enum, token_list):
        if (command_enum == constants.ALLOCATE_COMMAND):
            equity_amt = float(token_list[1])
            debt_amt = float(token_list[2])
            gold_amt = float(token_list[3])
            self._portfolio.allocate_command(equity_amt, debt_amt, gold_amt)
        elif (command_enum == constants.SIP_COMMAND): 
            equity_amt = float(token_list[1])
            debt_amt = float(token_list[2])
            gold_amt = float(token_list[3])
            self._portfolio.sip_command(equity_amt, debt_amt, gold_amt)
        elif (command_enum == constants.CHANGE_COMMAND):
            equity_change = float(token_list[1].replace("%",""))
            debt_change = float(token_list[2].replace("%",""))
            gold_change = float(token_list[3].replace("%",""))
            month_enum = token_list[4]
            self._portfolio.change_command(equity_change, debt_change, gold_change, month_enum)
        elif (command_enum == constants.BALANCE_COMMAND):
            month_enum = token_list[1] 
            self._portfolio.balance_command(month_enum)
        elif (command_enum == constants.REBALANCE_COMMAND):
            self._portfolio.rebalance_command()
            