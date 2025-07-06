"""Functions to automate Conda airlines ticketing system."""

import math
from collections.abc import Generator
from string import ascii_lowercase
from typing import Dict, List


def generate_seat_letters(number: int) -> Generator[str]:
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    counter = 0
    seat_letter = 0

    while counter < number:
        yield ascii_lowercase[seat_letter].upper()
        counter += 1
        seat_letter += 1
        if seat_letter > 3:
            seat_letter = 0


def generate_seats(number: int) -> Generator[str]:
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """

    counter = 1
    while counter <= number:
        for letter in generate_seat_letters(number):
            row = math.ceil(counter / 4)
            if row >= 13:
                row += 1
            yield str(row) + letter
            counter += 1


def assign_seats(passengers: List[str]) -> Dict[str, str]:
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """

    seat_list = zip(passengers, generate_seats(len(passengers)))
    return dict(seat_list)


def generate_codes(seat_numbers: List[str], flight_id: str):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """

    for seat_number in seat_numbers:
        ticket_code = seat_number + flight_id
        ticket_code = ticket_code + ("0" * (12 - len(ticket_code)))
        yield ticket_code
