"""Functions which helps the locomotive engineer to keep track of the train."""

from typing import Dict, List, Tuple


def get_list_of_wagons(*wagons: Tuple[int]) -> List:
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return list(wagons)


def fix_list_of_wagons(each_wagons_id: List[int], missing_wagons: List[int]) -> List[int]:
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """

    one, two, three, *rest = each_wagons_id
    return [three] + missing_wagons + rest + [one, two]


def add_missing_stops(route: Dict, **missing_stops: Dict):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param missing_stops: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    complete_route = dict(route)
    complete_route["stops"] = list(missing_stops.values())
    return complete_route


def extend_route_information(route: Dict, more_route_information: Dict) -> Dict:
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    return {**route, **more_route_information}


def fix_wagon_depot(wagons_rows: List[List[Tuple]]) -> List[List[Tuple]]:
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """

    [*all_rows] = zip(*wagons_rows)
    return [list(wagon_tuple) for wagon_tuple in all_rows]
