from src.models.asset_type import AssetType
import unittest

from tests.config.constants import BALANCE_TO_SET,OVERALL_BALANCE,MONTHLY_CHANGE,MONTH_ENUM,SIP_AMT

class TestAssetType(unittest.TestCase):
   
    def test_allocate_initial_capital(self):

        self._asset_type = AssetType("Test")
        self._asset_type.allocate_initial_capital(BALANCE_TO_SET,OVERALL_BALANCE)
        
        self.assertEqual(self._asset_type.current_balance,BALANCE_TO_SET)
        self.assertEqual(self._asset_type.initial_allocation_percentage,BALANCE_TO_SET/OVERALL_BALANCE )
    

    def test_execute_re_balance_command(self):
        self._asset_type = AssetType("Test")
        re_balance_output = self._asset_type.execute_re_balance_command(OVERALL_BALANCE)
        
        self.assertEqual(re_balance_output,None)
    

    def test_add_sip_and_monthly_change(self):
        self._asset_type = AssetType("Test")
        self._asset_type.current_balance = BALANCE_TO_SET
        self._asset_type.sip_amt = SIP_AMT
        self._asset_type.add_sip_and_monthly_change(MONTHLY_CHANGE, MONTH_ENUM)
        
        expected_balance = int((BALANCE_TO_SET + SIP_AMT)*(1+(MONTHLY_CHANGE/100)))
        self.assertEqual(self._asset_type.current_balance, expected_balance)
        