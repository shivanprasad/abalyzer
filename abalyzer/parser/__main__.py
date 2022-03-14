import array


# Parses an ACH number and returns information about it
def parse_aba(bank_number):
    return 0


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
def is_ach(bank_number):
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

number = "026009593"

print(is_aba(number))
print(is_ach(number))
