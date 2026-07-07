# Aula 17 - Integração Contínua, Qualidade Automatizada, Métricas e Gestão de Defeitos

Projeto: LocalEats  
Sistema: <https://local-eats-unisenac.vercel.app/>  
Integrante(s): Robinson Abraham

## 1. Repositório da Atividade

| Item | Descrição |
|---|---|
| Nome do repositório | `localeats-ci-laboratorio` |
| Link do repositório | <https://github.com/robinson-abraham/localeats-ci-laboratorio> |

Estrutura de diretórios utilizada:

```text
localeats-ci-laboratorio/
├── .github/
│   └── workflows/
│       └── quality.yml
├── tests/
│   └── test_order.py
├── aula-14-qualidade-processo.md
├── aula-15-modelos-maturidade.md
├── aula-16-qualidade-metodologias-ageis.md
├── aula-17-integracao-continua-qualidade.md
├── order.py
├── pytest.ini
├── README.md
└── requirements.txt
```

## 2. Planejamento da Funcionalidade

| Item | Descrição |
|---|---|
| Título da Issue | Implementar cálculo do total do pedido |
| Objetivo da funcionalidade | Calcular o total de um pedido do LocalEats considerando itens, quantidade, taxa de entrega e desconto percentual |
| Link da Issue | <https://github.com/robinson-abraham/localeats-ci-laboratorio/issues/1> |

## 3. Teste Automatizado

| Item | Descrição |
|---|---|
| Tipo de teste | Unitário |
| Objetivo do teste | Validar o cálculo do total do pedido e regras de validação para entradas inválidas |
| Link para o arquivo do teste | <https://github.com/robinson-abraham/localeats-ci-laboratorio/blob/main/tests/test_order.py> |

Código principal do teste criado:

```python
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
```

## 4. Pipeline de Integração Contínua

| Item | Descrição |
|---|---|
| Nome do workflow | Quality |
| Evento que dispara a execução | `push`, `pull_request` e `workflow_dispatch` |
| Link para o arquivo do workflow | <https://github.com/robinson-abraham/localeats-ci-laboratorio/blob/main/.github/workflows/quality.yml> |
| Link de uma execução do workflow | <https://github.com/robinson-abraham/localeats-ci-laboratorio/actions/runs/28837483825> |

Código do workflow:

```yaml
name: Quality

on:
  push:
    paths:
      - "order.py"
      - "tests/**"
      - "requirements.txt"
      - ".github/workflows/quality.yml"
  pull_request:
    paths:
      - "order.py"
      - "tests/**"
      - "requirements.txt"
      - ".github/workflows/quality.yml"
  workflow_dispatch:

jobs:
  tests:
    name: Testes automatizados
    runs-on: ubuntu-latest

    steps:
      - name: Baixar código
        uses: actions/checkout@v4

      - name: Configurar Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Instalar dependências
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Executar testes
        run: pytest -q
```

## 5. Indicadores de Qualidade

| Indicador | Valor |
|---|---|
| Quantidade de testes executados | 5 |
| Quantidade de testes aprovados | 5 |
| Quantidade de testes com falha | 0 |
| Status final do pipeline | Aprovado (`success`) |

## 6. Registro de Defeito

| Item | Descrição |
|---|---|
| Título do defeito | Validar quantidade negativa ou zero no cálculo do pedido |
| Severidade | Média |
| Link da Issue | <https://github.com/robinson-abraham/localeats-ci-laboratorio/issues/2> |

O defeito simulado foi a possibilidade de calcular pedidos com quantidade inválida. Ele foi identificado ao criar um teste unitário cobrindo quantidade igual a zero. A correção foi adicionar validação na função `calculate_order_total`, impedindo quantidade menor ou igual a zero. Após a correção, todos os testes passaram localmente e no pipeline.
