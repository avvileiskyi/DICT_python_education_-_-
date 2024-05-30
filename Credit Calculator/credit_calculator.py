"""Credit Calculator class"""

from math import ceil, log, floor
from sys import exit
import argparse


class CreditCalculator:
    """Class that represents credit calculator"""

    types = ["annuity", "diff"]

    def __init__(self, payment_type=None, payment=None, principal=None, periods=None, interest=None):
        """Initialize the CreditCalculator object

        Args:
            payment_type (str): type of payment
            principal (int): loan principal
            payment (int): the amount of the monthly payment
            periods (int): the number of months required to repay the loan
            interest (float): interests
        """
        self.payment_type = payment_type
        self.payment = payment
        self.principal = principal
        self.periods = periods
        self.interest = interest

        self.check_negative_params()

    def start(self):
        """Starts calculations based on input data and outputs the result"""

        # Calculate annuity
        if self.payment_type == self.types[0] and not self.payment and self.principal and self.periods:
            annuity, overpayment = self.calculate_annuity()
            print(f"Your annuity payment = {annuity}!\n"
                  f"Overpayment = {overpayment}")

        # Calculate loan principal
        elif self.payment_type == self.types[0] and self.payment and not self.principal and self.periods:
            principal, overpayment = self.calculate_principal()
            print(f"Your loan principal = {principal}!\n"
                  f"Overpayment = {overpayment}")

        # Calculate periods
        elif self.payment_type == self.types[0] and self.payment and self.principal and not self.periods:
            years, months, overpayment = self.calculate_periods()

            if years == 0 and months > 0:
                print("It will take {} month{} to repay this loan!"
                      .format(months, "s" if months != 1 else ""))

            elif years > 0 and months == 0:
                print("It will take {} year{} to repay this loan!"
                      .format(years, "s" if years != 1 else ""))

            else:
                print("It will take {} year{} and {} month{} to repay this loan!"
                      .format(years, "s" if years != 1 else "", months, "s" if months != 1 else ""))

            print(f"Overpayment = {overpayment}")

        # Calculate diff
        elif self.payment_type == self.types[1] and not self.payment and self.principal and self.periods:
            diff, overpayment = self.calculate_diff()

            for i in range(self.periods):
                print(f"Month {i + 1}: payment is {diff[i]}")

            print(f"Overpayment = {overpayment}")

        else:
            print("Incorrect parameters")

    def check_negative_params(self):
        """Checks for negatives values and exits the program if there are any"""
        if ((self.payment and self.payment < 0) or
                (self.principal and self.principal < 0) or
                (self.periods and self.periods < 0) or
                not self.interest or self.interest < 0):

            print("Incorrect parameters")
            exit()

    def calculate_annuity(self):
        """Calculates annuity payment and overpayment

        Returns:
            tuple: annuity payment and overpayment
        """
        interest = self.get_nominal_interest()

        numerator = interest * pow(1 + interest, self.periods)
        denominator = pow(1 + interest, self.periods) - 1

        annuity = ceil(self.principal * (numerator / denominator))
        overpayment = ceil(annuity * self.periods - self.principal)

        return annuity, overpayment

    def calculate_diff(self):
        """Calculates differentiated payment and overpayment

        Returns:
            tuple: list of payments for each month and overpayment
        """
        interest = self.get_nominal_interest()
        payments = []

        for month in range(1, self.periods + 1):
            diff_payment = (self.principal / self.periods + interest *
                            (self.principal - (self.principal * (month - 1) / self.periods)))
            payments.append(ceil(diff_payment))
        overpayment = ceil(sum(payments) - self.principal)

        return payments, overpayment

    def calculate_principal(self):
        """Calculate loan principal and overpayment

        Returns:
            tuple: loan principal and overpayment
        """
        interest = self.get_nominal_interest()

        numerator = interest * pow(1 + interest, self.periods)
        denominator = pow(1 + interest, self.periods) - 1

        principal = floor(self.payment / (numerator / denominator))
        overpayment = ceil(self.payment * self.periods - principal)

        return principal, overpayment

    def calculate_periods(self):
        """Calculate number of periods and overpayment

        Returns:
            tuple: years, months, and overpayment
        """
        interest = self.get_nominal_interest()

        calculations = self.payment / (self.payment - interest * self.principal)
        base = 1 + interest
        periods = log(calculations, base)

        years = ceil(periods) // 12
        months = ceil(periods) % 12
        overpayment = ceil(self.payment * ceil(periods) - self.principal)

        return years, months, overpayment

    def get_nominal_interest(self):
        """Calculate nominal interest

        Returns:
            float: nominal interest
        """
        return self.interest / (12 * 100)


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Program for calculating credits")
    parser.add_argument("--type", type=str, help="The type of payment")
    parser.add_argument("--payment", type=int, help="The amount of the monthly payment")
    parser.add_argument("--principal", type=int, help="Loan principal")
    parser.add_argument("--periods", type=int, help="The number of months required to repay the loan")
    parser.add_argument("--interest", type=float, help="Interests")

    args = parser.parse_args()

    calculator = CreditCalculator(args.type, args.payment, args.principal, args.periods, args.interest)
    calculator.start()