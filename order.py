from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_UP
from typing import Iterable


MONEY = Decimal("0.01")


class OrderValidationError(ValueError):
    """Erro de validação para pedidos do LocalEats."""


@dataclass(frozen=True)
class OrderItem:
    name: str
    unit_price: Decimal
    quantity: int


def _to_money(value: Decimal | int | float | str) -> Decimal:
    return Decimal(str(value)).quantize(MONEY, rounding=ROUND_HALF_UP)


def calculate_order_total(
    items: Iterable[OrderItem],
    delivery_fee: Decimal | int | float | str = Decimal("0.00"),
    discount_percent: Decimal | int | float | str = Decimal("0"),
) -> Decimal:
    item_list = list(items)
    if not item_list:
        raise OrderValidationError("O pedido deve possuir pelo menos um item.")

    discount = Decimal(str(discount_percent))
    if discount < 0 or discount > 100:
        raise OrderValidationError("O desconto deve estar entre 0% e 100%.")

    fee = _to_money(delivery_fee)
    if fee < 0:
        raise OrderValidationError("A taxa de entrega não pode ser negativa.")

    subtotal = Decimal("0.00")
    for item in item_list:
        if item.quantity <= 0:
            raise OrderValidationError("A quantidade do item deve ser maior que zero.")
        unit_price = _to_money(item.unit_price)
        if unit_price < 0:
            raise OrderValidationError("O preço unitário não pode ser negativo.")
        subtotal += unit_price * item.quantity

    discount_value = (subtotal * discount / Decimal("100")).quantize(
        MONEY, rounding=ROUND_HALF_UP
    )
    return (subtotal - discount_value + fee).quantize(MONEY, rounding=ROUND_HALF_UP)

