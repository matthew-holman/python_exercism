"""Solution to Ellen's Alien Game exercise."""

from pickle import TUPLE
from typing import List, Tuple


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """

    total_aliens_created: int = 0

    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health: int = 3
        Alien.total_aliens_created = Alien.total_aliens_created + 1

    def hit(self) -> None:
        self.health = self.health - 1 if self.health > 0 else 0

    def is_alive(self) -> bool:
        return self.health > 0

    def teleport(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def collision_detection(self, other: object) -> None:
        pass


# TODO:  create the new_aliens_collection() function below to call your Alien class with a list of coordinates.


def new_aliens_collection(alien_positions: List[Tuple[int, int]]):
    return [Alien(x, y) for x, y in alien_positions]
