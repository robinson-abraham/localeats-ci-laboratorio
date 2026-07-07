from decimal import Decimal

import pytest

from order import OrderItem, OrderValidationError, calculate_order_total


def test_calcula_total_do_pedido_com_taxa_e_desconto():
    items = [
        OrderItem("Xis salada", Decimal("20.00"), 2),
        OrderItem("Suco natural", Decimal("7.50"), 1),
    ]

    total = calculate_order_total(items, delivery_fee=Decimal("5.00"), discount_percent=10)

    assert total == Decimal("47.75")


def test_rejeita_pedido_sem_itens():
    with pytest.raises(OrderValidationError, match="pelo menos um item"):
        calculate_order_total([])


def test_rejeita_quantidade_negativa_ou_zero():
    items = [OrderItem("Hambúrguer", Decimal("25.00"), 0)]

    with pytest.raises(OrderValidationError, match="maior que zero"):
        calculate_order_total(items)


def test_rejeita_desconto_fora_do_intervalo():
    items = [OrderItem("Pizza", Decimal("40.00"), 1)]

    with pytest.raises(OrderValidationError, match="entre 0% e 100%"):
        calculate_order_total(items, discount_percent=120)


def test_rejeita_taxa_de_entrega_negativa():
    items = [OrderItem("Marmita", Decimal("18.90"), 1)]

    with pytest.raises(OrderValidationError, match="não pode ser negativa"):
        calculate_order_total(items, delivery_fee=Decimal("-3.00"))

