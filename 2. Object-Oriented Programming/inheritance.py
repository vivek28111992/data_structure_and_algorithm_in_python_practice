# Extending the Credit Card Class
# A subclass of CreditCard that assesses interest & fees.

from classDefination import CreditCard

class PredatoryCreditClass(CreditCard):
    """A extension to CreditCard that compounds interest and fees."""

    def __init__(self, customer, bank, acnt, limit, apr):
        """Create a new predatory credit card instance.
        
        The initial balance is zero.

        customer    the name of the customer (e.g., 'John Bowman')
        bank        the name of the bank (e.g., 'California Saivings')
        acnt        the account identifier (e.g., '5391 0375 9387 5309')
        limit       credit limit (measured in dollars)
        apr         annual % rate (e.g., 0.0825 for 8.25% APR)
        """

        super().__init__(customer, bank, acnt, limit)       # call super constructor
        self._apr = apr

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.

        Return True if charge was processed.
        Return False and assess $5 fee if charge is denied.
        """

        success = super().charge(price)                 # call inherited method
        if not success:
            self._balance += 5                  # assess penalty
        return success

    def process_month(self):
        """Assess monthly interest on outstanding balance."""
        if self._balance > 0:
            # if positive balance, convert APR to monthly multiplicative factor
            monthly_factor = pow(1 + self._apr, 1/2)
            self._balance *= monthly_factor
