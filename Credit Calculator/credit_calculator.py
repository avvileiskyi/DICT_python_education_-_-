"""Credit Calculator class"""

from math import ceil, log, floor
from sys import exit
import argparse


class CreditCalculator:
    """Class that represents credit calculator"""

    types = ["annuity", "diff"]

    def __init__(self, calc_type=None, monthly_payment=None, loan_principal=None, num_periods=None, annual_interest=None):
        """Initialize the CreditCalculator object

        Args:
            calc_type (str): type of payment (annuity or differentiated)
            loan_principal (int): loan principal amount
            monthly_payment (int): the amount of the monthly payment
            num_periods (int): the number of months required to repay the loan
            annual_interest (float): annual interest rate
        """
        self.calc_type = calc_type
        self.monthly_payment = monthly_payment
        self.loan_principal = loan_principal
        self.num_periods = num_periods
        self.annual_interest = annual_interest

        self.check_for_negative_values()

    def start_calculation(self):
        """Starts calculations based on input data and outputs the result"""

        # Calculate annuity payment
        if self.calc_type == self.types[0] and not self.monthly_payment and self.loan_principal and self.num_periods:
            annuity_payment, overpayment = self.calculate_annuity_payment()
            print(f"Your annuity payment = {annuity_payment}!\n"
                  f"Overpayment = {overpayment}")

        # Calculate loan principal
        elif self.calc_type == self.types[0] and self.monthly_payment and not self.loan_principal and self.num_periods:
            principal, overpayment = self.calculate_loan_principal()
            print(f"Your loan principal = {principal}!\n"
                  f"Overpayment = {overpayment}")

        # Calculate number of periods
        elif self.calc_type == self.types[0] and self.monthly_payment and self.loan_principal and not self.num_periods:
            years, months, overpayment = self.calculate_num_periods()

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

        # Calculate differentiated payments
        elif self.calc_type == self.types[1] and not self.monthly_payment and self.loan_principal and self.num_periods:
            diff_payments, overpayment = self.calculate_differentiated_payments()

            for i in range(self.num_periods):
                print(f"Month {i + 1}: payment is {diff_payments[i]}")

            print(f"Overpayment = {overpayment}")

        else:
            print("Incorrect parameters")

    def check_for_negative_values(self):
        """Checks for negative values and exits the program if any are found"""
        if ((self.monthly_payment and self.monthly_payment < 0) or
                (self.loan_principal and self.loan_principal < 0) or
                (self.num_periods and self.num_periods < 0) or
                not self.annual_interest or self.annual_interest < 0):

            print("Incorrect parameters")
            exit()

    def calculate_annuity_payment(self):
        """Calculates annuity payment and overpayment

        Returns:
            tuple: annuity payment and overpayment
        """
        interest_rate = self.calculate_nominal_interest_rate()

        numerator = interest_rate * pow(1 + interest_rate, self.num_periods)
        denominator = pow(1 + interest_rate, self.num_periods) - 1

        annuity_payment = ceil(self.loan_principal * (numerator / denominator))
        overpayment = ceil(annuity_payment * self.num_periods - self.loan_principal)

        return annuity_payment, overpayment

    def calculate_differentiated_payments(self):
        """Calculates differentiated payments and overpayment

        Returns:
            tuple: list of payments for each month and overpayment
        """
        interest_rate = self.calculate_nominal_interest_rate()
        payments = []

        for month in range(1, self.num_periods + 1):
            diff_payment = (self.loan_principal / self.num_periods + interest_rate *
                            (self.loan_principal - (self.loan_principal * (month - 1) / self.num_periods)))
            payments.append(ceil(diff_payment))
        overpayment = ceil(sum(payments) - self.loan_principal)

        return payments, overpayment

    def calculate_loan_principal(self):
        """Calculate loan principal and overpayment

        Returns:
            tuple: loan principal and overpayment
        """
        interest_rate = self.calculate_nominal_interest_rate()

        numerator = interest_rate * pow(1 + interest_rate, self.num_periods)
        denominator = pow(1 + interest_rate, self.num_periods) - 1

        principal = floor(self.monthly_payment / (numerator / denominator))
        overpayment = ceil(self.monthly_payment * self.num_periods - principal)

        return principal, overpayment

    def calculate_num_periods(self):
        """Calculate number of periods and overpayment

        Returns:
            tuple: years, months, and overpayment
        """
        interest_rate = self.calculate_nominal_interest_rate()

        calculations = self.monthly_payment / (self.monthly_payment - interest_rate * self.loan_principal)
        base = 1 + interest_rate
        periods = log(calculations, base)

        years = ceil(periods) // 12
        months = ceil(periods) % 12
        overpayment = ceil(self.monthly_payment * ceil(periods) - self.loan_principal)

        return years, months, overpayment

    def calculate_nominal_interest_rate(self):
        """Calculate nominal interest rate

        Returns:
            float: nominal interest rate
        """
        return self.annual_interest / (12 * 100)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Program for calculating credit payments")
    parser.add_argument("--type", type=str, help="The type of payment: 'annuity' or 'diff'")
    parser.add_argument("--payment", type=int, help="The amount of the monthly payment")
    parser.add_argument("--principal", type=int, help="The loan principal amount")
    parser.add_argument("--periods", type=int, help="The number of months required to repay the loan")
    parser.add_argument("--interest", type=float, help="The annual interest rate (as a percentage)")

    args = parser.parse_args()

    calculator = CreditCalculator(args.type, args.payment, args.principal, args.periods, args.interest)
    calculator.start_calculation()
