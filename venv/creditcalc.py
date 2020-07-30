import math
import argparse
import sys


def annuity_payment(credit_principal, count_periods, interest):
    i = interest / (12 * 100)
    a = credit_principal * i * pow(i + 1, count_periods) / (pow(i + 1, count_periods) - 1)
    a = math.ceil(a)
    print(f"Your annuity payment = {a}!")
    overpayment = math.ceil(a * count_periods - credit_principal)
    print(f"Overpayment = {overpayment}")


def credit_principal_(monthly_payment, count_periods, interest):
    i = interest / (12 * 100)
    p = monthly_payment / (i * pow(i + 1, count_periods) / (pow(i + 1, count_periods) - 1))
    p = math.floor(p)
    print(f"Your credit principal = {p}!")
    overpayment = monthly_payment * count_periods - p
    print(f"Overpayment = {overpayment}")


def count_month(credit_principal, monthly_payment, interest):
    i = interest / (12 * 100)
    n = math.ceil(math.log(monthly_payment / (monthly_payment - i * credit_principal), 1 + i))
    years = int(n / 12)
    month = int(n % 12)
    if years == 0:
        print(f"You need {month} months to repay this credit!")
    elif month == 0:
        print(f"You need {years} years to repay this credit!")
    else:
        print(f"You need {years} years and {month} months to repay this credit!")
    overpayment = math.ceil(n * monthly_payment - credit_principal)
    print(f"Overpayment = {overpayment}")


def calculate_diff(principal, periods, interest):
    i = interest / (12 * 100)
    m = 1
    overpayment = 0
    while m <= periods:
        diff = (principal / periods) + i * (principal - ((principal * (m - 1)) / periods ))
        diff = math.ceil(diff)
        print(f"Month {m}: paid out {diff}")
        overpayment = overpayment + diff
        m += 1
    overpayment = math.ceil(overpayment - principal)
    print(f"Overpayment = {overpayment}")


parser = argparse.ArgumentParser()
parser.add_argument("--type", help="diff = differentiated payment | annuity = annuity payment", type=str)
parser.add_argument("--payment", help="payment of month", type=int)
parser.add_argument("--principal", help=" Credit principal", type=float)
parser.add_argument("--periods", help="number of months", type=int)
parser.add_argument("--interest", help="number of months", type=float)
args = parser.parse_args()

arguments = sys.argv
if len(arguments) < 5:
    print("Incorrect parameters")
elif args.type is None:
    print("Incorrect parameters" )
elif args.interest is None:
    print("Incorrect parameters")
else:
    if args.type == "diff":
        if args.payment is not None:
            print("Incorrect parameters")
        elif args.principal < 0 or args.periods < 0 or args.interest < 0:
            print("Incorrect parameters")
        else:
            calculate_diff(args.principal,args.periods,args.interest)
    elif args.type == "annuity":
        if args.principal is None:
            if args.payment < 0 or args.periods < 0 or args.interest < 0:
                print("Incorrect parameters")
            else:
                credit_principal_(args.payment, args.periods, args.interest)
        elif args.periods is None:
            if args.principal < 0 or args.payment < 0 or args.interest < 0:
                print("Incorrect parameters")
            else:
                count_month(args.principal, args.payment, args.interest)
        else:
            if args.principal < 0 or args.periods < 0 or args.interest < 0:
                print("Incorrect parameters")
            else:
                annuity_payment(args.principal, args.periods, args.interest)