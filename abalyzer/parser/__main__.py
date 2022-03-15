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


def aba_state(bank_number):
    output = "null"
    bank_number = str(bank_number)
    digits = [int(i) for i in bank_number]
    first_two_digits = digits[0] + digits[1]
    first_two_digits = int(first_two_digits)

    if first_two_digits == (int("00")): output = "United States Government"
    if first_two_digits == (int("01") or int("21") or int("61")): output = "Massachusetts"
    if first_two_digits == (int("02") or int("22") or int("62")): output = "New York"
    if first_two_digits == (int("03") or int("23") or int("63")): output = "Pennsylvania"
    if first_two_digits == (int("04") or int("24") or int("64")): output = "Ohio"
    if first_two_digits == (int("05") or int("25") or int("65")): output = "Virginia"
    if first_two_digits == (int("06") or int("26") or int("66")): output = "Georgia"
    if first_two_digits == (int("07") or int("27") or int("67")): output = "Illinois"
    if first_two_digits == (int("08") or int("28") or int("68")): output = "Missouri"
    if first_two_digits == (int("09") or int("29") or int("69")): output = "Minnesota"
    if first_two_digits == (int("10") or int("30") or int("70")): output = "Kansas"
    if first_two_digits == (int("11") or int("31") or int("71")): output = "Texas"
    if first_two_digits == (int("12") or int("32") or int("72")): output = "California"

    return output



number = "026009593"
print(aba_state(number))
print(is_aba(number))
print(is_eti(number))
