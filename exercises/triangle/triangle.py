from typing import List


def equilateral(sides: List[int]) -> bool:
    return is_triangle(sides) and num_unique_sides(sides) == 1


def isosceles(sides: List[int]) -> bool:
    return is_triangle(sides) and num_unique_sides(sides) <= 2


def scalene(sides: List[int]) -> bool:
    return is_triangle(sides) and num_unique_sides(sides) == 3


def num_unique_sides(sides: List[int]) -> int:
    return len(set(sides))


def is_triangle(sides: List[int]) -> int:
    a, b, c = sorted(sides)
    return all(side > 0 for side in sides) and a + b > c
