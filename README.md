# Estoque T.I.

Sistema de controle de estoque desenvolvido em Python, usando Programação Orientada a Objetos e SQLAlchemy como ORM, com persistência em SQLite. Roda inteiramente via terminal.

## Motivação

Sou estudante de Análise e Desenvolvimento de Sistemas e estagiário de T.I. Esse projeto nasceu da junção de duas necessidades: fixar na prática o que aprendi em um curso de Python, POO e banco de dados com SQLAlchemy, e ao mesmo tempo ter uma ferramenta real para organizar o estoque de equipamentos e materiais de T.I. do meu trabalho.

Por isso o sistema é propositalmente simples. A ideia não foi construir algo comercial ou genérico, mas um projeto de estudo que resolve um problema concreto do dia a dia controlar entrada, saída e cadastro de itens de forma organizada, sem depender de planilhas soltas.

## Funcionalidades

- Cadastrar novos itens no estoque (categoria, nome e quantidade)
- Listar todos os itens cadastrados
- Aumentar a quantidade de um item existente
- Diminuir a quantidade de um item existente
- Excluir um item do estoque

Todas as operações validam a entrada do usuário e tratam erros de forma que o programa nunca trava sempre retorna uma mensagem clara e volta ao menu.

## Tecnologias

- Python
- SQLAlchemy (ORM)
- SQLite

## Como rodar

```bash
# clonar o repositório
git clone <https://github.com/douglaskevin201/estoque-t.i>
cd estoque-t.i

# instalar dependências
pip install sqlalchemy

# rodar o sistema
python menu.py
```

O banco de dados (`estoque.db`) é criado automaticamente na primeira execução.

## Decisões técnicas e aprendizados

Algumas escolhas do projeto vieram de problemas reais que apareceram durante o desenvolvimento, não de decisões definidas de antemão:

- **Tratamento de erros com `try/except`**: toda operação que mexe no banco ou recebe entrada do usuário está protegida contra falhas desde digitar uma letra onde se espera um número, até tentar remover mais itens do que existem em estoque. Em vez de deixar o programa quebrar, cada erro é capturado e devolve uma mensagem compreensível.

- **IDs não são reaproveitados após exclusão**: ao excluir um item, o próximo cadastro não "preenche" o ID que ficou vago ele segue a sequência normalmente. Esse é o comportamento padrão do SQLite/SQLAlchemy, e é proposital: reaproveitar IDs cria risco de ambiguidade caso, no futuro, outras tabelas venham a referenciar esses identificadores.

- **Separação entre `models.py` e `menu.py`**: as classes e regras de negócio ficam isoladas da camada de interação com o usuário, facilitando manutenção e futuras expansões.

- **Sem API nessa etapa**: o projeto foi mantido em Python puro + SQLAlchemy de propósito, para consolidar esses conceitos isoladamente antes de introduzir uma camada de API.

### Sobre o uso de IA no desenvolvimento

Usei o Claude como apoio de estudo ao longo de todo o projeto, mas com um papel bem delimitado: revisar o código que eu mesmo escrevia, apontando bugs reais, lógica que não funcionava como eu esperava, e código redundante  sem nunca escrever a solução pronta em meu lugar. Quando eu tinha dúvida conceitual (por exemplo, a diferença entre `print` e `raise`, ou por que usar `try/except`), a IA explicava o "porquê" por trás, e eu aplicava a correção sozinho.

Esse mesmo formato de ajuda guiada foi o que pedi para replicar ao usar outras IAs de apoio no dia a dia do desenvolvimento, como o GitHub Copilot: revisão de código, apontamento de problemas e perguntas que me ajudassem a pensar na lógica nunca a entrega da implementação final.

## Possíveis próximos passos

- Adicionar uma API para hospedar o banco de dados em outro ambiente
- Implementar busca por categoria
- Transformar o sistema em um programa com interface, facilitando o uso no dia a dia do trabalho
