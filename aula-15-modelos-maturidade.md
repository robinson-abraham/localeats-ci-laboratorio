# Aula 15 - Modelos de Maturidade

Projeto: LocalEats  
Sistema: <https://local-eats-unisenac.vercel.app/>  
Integrante(s): Robinson Abraham

## 1. Diagnóstico de Maturidade

| Critério | Sim | Parcial | Não |
|---|:---:|:---:|:---:|
| Os requisitos são documentados? |  | X |  |
| Existe controle de mudanças? |  | X |  |
| Há atividades de teste definidas? | X |  |  |
| Os defeitos são registrados? |  | X |  |
| O processo de desenvolvimento é conhecido por toda a equipe? |  | X |  |
| As tarefas são planejadas e acompanhadas regularmente? |  | X |  |
| Existe padronização para implementação de funcionalidades? |  | X |  |
| Os testes são executados antes da entrega das funcionalidades? | X |  |  |
| Há revisão de código ou validação por outro integrante da equipe? |  | X |  |
| A equipe utiliza ferramentas para gerenciamento das atividades? | X |  |  |
| Os artefatos do projeto (requisitos, testes, código) são organizados e versionados? | X |  |  |
| Existe rastreabilidade entre requisitos e funcionalidades implementadas? |  | X |  |
| A equipe realiza reuniões ou momentos de retrospectiva para identificar melhorias? |  | X |  |
| Existem indicadores ou métricas para acompanhar a qualidade do projeto? |  | X |  |

Classificação do processo: **Gerenciado**.

O processo possui práticas importantes, como versionamento, testes, organização dos artefatos e uso de ferramentas. Porém, ainda existem lacunas em padronização, rastreabilidade, controle formal de mudanças e uso contínuo de métricas. Por isso, ele está acima de um processo inicial, mas ainda não pode ser considerado totalmente definido ou quantitativamente gerenciado. A evolução depende de transformar práticas informais em critérios claros, repetíveis e acompanhados por indicadores.

## 2. Lacunas Identificadas

| Lacuna | Impacto |
|---|---|
| Critérios de pronto e concluído ainda não formalizados | Funcionalidades podem entrar em desenvolvimento com informações incompletas ou serem entregues sem validação uniforme |
| Registro de defeitos parcialmente padronizado | Dificulta acompanhar causa, severidade, correção e recorrência dos problemas |
| Métricas de qualidade ainda simples | A equipe tem menos visibilidade sobre estabilidade, falhas e evolução do processo |
| Rastreabilidade parcial entre requisito, teste e entrega | Torna mais difícil provar que cada requisito foi validado |
| Retrospectivas sem rotina fixa | Oportunidades de melhoria podem ser esquecidas entre uma entrega e outra |

## 3. Propostas de Melhoria

| Melhoria | Benefício |
|---|---|
| Criar e aplicar uma Definition of Ready (DoR) | Garante que uma demanda só comece com objetivo, regras e critérios de aceite claros |
| Criar e aplicar uma Definition of Done (DoD) | Padroniza a conclusão de funcionalidades com testes, revisão e documentação mínima |
| Registrar defeitos como GitHub Issues | Facilita priorização, acompanhamento, histórico e evidência da correção |
| Manter um quadro Kanban para tarefas e bugs | Aumenta a visibilidade do andamento e reduz perda de informações |
| Acompanhar métricas simples de qualidade | Permite avaliar testes executados, falhas, bugs abertos e status do pipeline |
| Relacionar issue, branch, commit e teste | Melhora a rastreabilidade entre necessidade, implementação e validação |
