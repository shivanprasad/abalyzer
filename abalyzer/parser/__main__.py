import array


# Parses an ACH number and returns information about it
def parse_aba(bank_number):
    return 0


# Parses an ACH number and returns information about it
def parse_ach(bank_number):
    return 0


# Parses a user-defined number to see if it is an ABA number
def is_aba(bank_number):
    output = False
    bank_number = str(bank_number)
    chars = [int(i) for i in bank_number]
    length = len(bank_number)
    print(bank_number)

    if length == 9:
        if ((3 * (chars[0] + chars[3] + chars[6]) +
             7 * (chars[1] + chars[4] + chars[7]) +
             (chars[2] + chars[5] + chars[8]))) % 10 == 0:
            output = True
    else:
        output = False
    return output


# Parses a user-defined number to see if it is an ACH number
def is_ach(bank_number):
    return True


print(is_aba(111000025))
