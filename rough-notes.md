- Portfolio Class has 3 AssetType objects
    - Gold
    - Equity
    - Debt

- Portfolio Class
    - initialGoldPercentage: 0.0
    - initialEquityPercentage: 0.0
    - initialDebtPercentage: 0.0
    methods:
    - allocateCommand(a,b,c)
        - Calculate initial portfolio percentages 
        - Initialization of AssetType objects, Allocate the initial capital
        - Add the balance in monthToClosingBalanceMap for january

    - sipCommand(a,b,c) - parent class
        - set sip numbers and store them at portfolio class level

    - changeCommand(month, change) - On child class
        - first add the SIP value in the portfolio - Parent class
        - then calculate the change in the portfolio - Child class
        - update the current value - Child class

    - rebalanceCommand(a,b,c) - Parent class
        - rebalanceChild(amt) - Child class
            - calculate the change in the portfolio
            - update the current value

    - balanceCommand(month) - Parent
        - balanceChild(month) - Child
            - return the balance for the month

- AssetType Class
    - name: "GOLD | EQUITY | DEBT"
    - currentValue: 0.0

    - monthToClosingBalanceMap: {
        "JANUARY": 0.0,
    }

    - allocateInitialCapital(amt)
    - 


    - monthlyChange()