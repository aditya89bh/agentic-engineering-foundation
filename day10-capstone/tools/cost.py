def calculate_landed_cost(unit_price: float, quantity: int, shipping: float = 0):
    return unit_price * quantity + shipping
