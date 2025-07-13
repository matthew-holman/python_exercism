def is_armstrong_number(number: int) -> bool:
    digits = str(number)
    power = len(digits)
    return number == sum(int(digit) ** power for digit in digits)
