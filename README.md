# LocalEats - Laboratório de Qualidade

Repositório criado para entregar as atividades PBL do projeto LocalEats avaliadas em processo, maturidade, metodologias ágeis, integração contínua, qualidade automatizada, métricas e gestão de defeitos.

## Integrante(s)

- Robinson Abraham

## Atividades

- [Aula 14 - Qualidade de Processo](aula-14-qualidade-processo.md)
- [Aula 15 - Modelos de Maturidade](aula-15-modelos-maturidade.md)
- [Aula 16 - Qualidade em Metodologias Ágeis](aula-16-qualidade-metodologias-ageis.md)
- [Aula 17 - Integração Contínua e Qualidade Automatizada](aula-17-integracao-continua-qualidade.md)

## Estrutura

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
├── README.md
└── requirements.txt
```

## Como executar localmente

```bash
pip install -r requirements.txt
pytest -q
```
