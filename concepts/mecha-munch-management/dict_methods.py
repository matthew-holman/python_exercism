"""Functions to manage a users shopping cart items."""

from typing import Dict, List


def add_item(current_cart: Dict, items_to_add: List) -> Dict:
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """

    for item in items_to_add:
        if item in current_cart:
            current_cart[item] = current_cart[item] + 1
        else:
            current_cart[item] = 1

    return current_cart


def read_notes(notes: List) -> Dict:
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """

    return dict.fromkeys(notes, 1)


def update_recipes(ideas: Dict, recipe_updates: Dict) -> Dict:
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: dict - dictionary with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """

    ideas.update(recipe_updates)
    return ideas


def sort_entries(cart: Dict) -> Dict:
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """

    return dict(sorted(cart.items()))


def send_to_store(cart: Dict[str, int], aisle_mapping: Dict[str, List]) -> Dict[str, List]:
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """

    fulfillment_map = {item: [cart[item]] + aisle_mapping[item][:] for item in cart}
    return dict(sorted(fulfillment_map.items(), reverse=True))


def update_store_inventory(fulfillment_cart: Dict[str, List], store_inventory: Dict[str, List]):
    """Update store inventory levels with user order.

    :param fulfillment_cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """

    for item, (qty, *_rest) in fulfillment_cart.items():
        store_item = store_inventory[item]
        in_stock_qty = store_item[0]
        if isinstance(in_stock_qty, int):
            updated_qty = store_item[0] - qty
            store_item[0] = updated_qty if updated_qty > 0 else "Out of Stock"

    return store_inventory
