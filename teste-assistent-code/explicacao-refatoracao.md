# Explicação do Código em refatoracao.py

O código define uma função chamada `c` que recebe uma lista `l` como parâmetro. Esta função calcula e retorna quatro valores estatísticos básicos da lista: a soma total dos elementos, a média, o maior valor e o menor valor.

## Detalhes da Função

- **Soma total (`t`)**: Inicializa `t` em 0 e itera sobre cada elemento da lista, somando-os a `t`.
- **Média (`m`)**: Calcula a média dividindo a soma total pelo número de elementos (`len(l)`).
- **Maior valor (`mx`)**: Inicializa `mx` com o primeiro elemento da lista e itera para encontrar o maior valor.
- **Menor valor (`mn`)**: Inicializa `mn` com o primeiro elemento da lista e itera para encontrar o menor valor.

A função retorna uma tupla com os quatro valores: `(t, m, mx, mn)`.

## Demonstração

O código cria uma lista `x` com valores numéricos: `[23, 7, 45, 2, 67, 12, 89, 34, 56, 11]`.

Chama a função `c(x)` e desempacota os resultados em variáveis `a`, `b`, `c2`, `d` (nota: `c2` é usado para evitar conflito com o nome da função `c`).

Imprime os resultados:
- Total: soma dos elementos
- Média: valor médio
- Maior: maior elemento
- Menor: menor elemento

Este código é uma implementação simples de cálculos estatísticos básicos em Python.