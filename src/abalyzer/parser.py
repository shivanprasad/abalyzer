import pandas as pd
import os

script_dir = os.path.dirname(__file__)  # Script directory
aba_lookup_table_path = os.path.join(script_dir, 'data/aba_lookup_table.csv')


# Parses an ACH number and returns information about it
def parse_aba(bank_number):
    bank_number = str(bank_number)
    aba_lookup_table = pd.read_csv(aba_lookup_table_path)

    if is_aba(bank_number):
        for i in range(len(aba_lookup_table)):
            if aba_lookup_table.aba_number[i] == bank_number:
                return (list(aba_lookup_table.iloc[i]))

# Parses a user-defined number to see if it is an ABA number
# https://en.wikipedia.org/wiki/ABA_routing_transit_number
def is_aba(bank_number):
    output = False
    bank_number = str(bank_number)
    digits = [int(i) for i in bank_number]
    length = len(bank_number)

    if length == 9:
        if((3 * (digits[0] + digits[3] + digits[6]) +
             7 * (digits[1] + digits[4] + digits[7]) +
             (digits[2] + digits[5] + digits[8]))) % 10 == 0:
            output = True
    else:
        output = False
    return output


# Parses a user-defined number to see if it is an ACH number
def is_eti(bank_number):
    output = False
    bank_number = str(bank_number)
    digits = [int(i) for i in bank_number]
    length = len(bank_number)
    first_two_digits = digits[0] + digits[1]
    first_two_digits = int(first_two_digits)

    if is_aba(bank_number):
        if first_two_digits >= 61 | first_two_digits <= 72:
            output = True
    else:
        output = False

    return output
