def steps(number: int):
    if number < 1:
        raise ValueError("Only positive integers are allowed")

    working_number = number
    iteration_count = 0

    while working_number != 1:
        working_number = step(working_number)
        iteration_count += 1

    return iteration_count


def step(number: int) -> int:
    if number % 2 == 0:
        return int(number / 2)
    return (number * 3) + 1
