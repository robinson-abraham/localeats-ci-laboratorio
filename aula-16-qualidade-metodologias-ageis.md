# Aula 16 - Qualidade em Metodologias Ágeis

Projeto: LocalEats  
Sistema: <https://local-eats-unisenac.vercel.app/>  
Integrante(s): Robinson Abraham

## 1. Análise de Práticas Ágeis no Processo

| Prática | Existe no processo? | Como é aplicada atualmente? | Pode ser melhorada? |
|---|---|---|---|
| Planejamento iterativo | Parcial | As demandas são separadas em funcionalidades pequenas para facilitar implementação e validação | Sim, com ciclos curtos e metas explícitas por iteração |
| Priorização de funcionalidades | Parcial | As tarefas mais importantes ou mais simples de validar tendem a ser feitas primeiro | Sim, usando critérios de valor, risco e dependência |
| Entregas incrementais | Sim | O projeto permite evoluir por pequenas funcionalidades e ajustes | Sim, associando cada incremento a uma issue e a critérios de aceite |
| Feedback frequente | Parcial | O feedback ocorre em testes, revisão e validação do resultado | Sim, com revisões mais frequentes e checklist de aceite |
| Trabalho colaborativo | Sim | O trabalho pode ser dividido entre implementação, teste e revisão | Sim, usando pair review ou revisão obrigatória antes da entrega |
| Controle visual das atividades | Parcial | As atividades podem ser acompanhadas por issues e status no GitHub | Sim, com um quadro Kanban com colunas padronizadas |
| Melhoria contínua | Parcial | Melhorias são identificadas durante correções e entregas | Sim, com retrospectiva curta ao final de cada ciclo |

Conclusão: o processo do LocalEats já possui práticas próximas de métodos ágeis, principalmente entregas incrementais, colaboração e uso de versionamento. A principal oportunidade está em tornar essas práticas mais explícitas e repetíveis. O uso de DoR, DoD, Kanban, revisão de código e pipeline automatizado ajuda a preservar a agilidade sem abrir mão da qualidade. Assim, a equipe reduz retrabalho, melhora a comunicação e entrega funcionalidades com evidências mais claras de validação.

## 2. Propostas de Melhoria Ágil

| Melhoria Proposta | Metodologia Relacionada | Benefício Esperado |
|---|---|---|
| Usar quadro Kanban com colunas Backlog, Pronto, Em desenvolvimento, Em teste, Revisão e Concluído | Kanban | Maior visibilidade do fluxo e identificação de gargalos |
| Adotar Definition of Ready para entrada de funcionalidades | Scrum | Reduz dúvidas antes do desenvolvimento e evita retrabalho |
| Adotar Definition of Done para entrega | Scrum / XP | Garante que a entrega inclua teste, revisão e validação |
| Executar testes automatizados a cada push | XP / Integração Contínua | Detecta regressões rapidamente |
| Realizar revisão curta de código antes de concluir uma issue | XP | Melhora qualidade interna e compartilhamento de conhecimento |
| Fazer retrospectiva ao final de cada ciclo | Scrum / Lean | Transforma problemas do processo em ações de melhoria |

## 3. Definition of Ready (DoR)

Uma funcionalidade do LocalEats estará pronta para desenvolvimento quando:

1. O objetivo da funcionalidade estiver descrito em uma issue.
2. O comportamento esperado estiver claro para a equipe.
3. Os critérios de aceite estiverem definidos.
4. As regras de negócio e restrições forem conhecidas.
5. A funcionalidade tiver prioridade definida no backlog.
6. A equipe souber quais arquivos ou módulos provavelmente serão impactados.
7. Existir entendimento sobre como a funcionalidade será testada.

## 4. Definition of Done (DoD)

Uma funcionalidade do LocalEats será considerada concluída quando:

1. O código estiver implementado conforme os critérios de aceite.
2. Os testes automatizados relacionados estiverem criados ou atualizados.
3. Os testes locais estiverem aprovados.
4. O pipeline do GitHub Actions estiver aprovado.
5. O código tiver sido revisado ou validado por outro integrante quando aplicável.
6. Defeitos encontrados durante a validação estiverem corrigidos ou registrados.
7. A documentação ou evidência da atividade estiver atualizada no repositório.
