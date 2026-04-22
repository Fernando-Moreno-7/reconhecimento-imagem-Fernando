# Explicação dos Erros Encontrados no debug.py

## Erro 1: Falta de Aspas em String (Linha 6)
**Localização:** `float(input(Preço do item 1? ))`
**Problema:** O string "Preço do item 1? " não está entre aspas.
**Solução:** Adicionar aspas duplas: `float(input("Preço do item 1? "))`

---

## Erro 2: Tipo de Dado Incorreto para desconto_cupom (Linha 21)
**Localização:** `desconto_cupom = (input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))`
**Problema:** `input()` retorna uma string, mas na linha 22 é usado em operação matemática `desconto_cupom / 100` e na linha 34 em comparação `if desconto_cupom > 0:`, o que causa erro.
**Solução:** Converter para número: `desconto_cupom = int(input("..."))`

---

## Erro 3: F-string Faltando (Linha 29)
**Localização:** `print(" Item 2:        R$ {total_item2:.2f}")`
**Problema:** Falta o prefixo `f` antes das aspas. Sem o `f`, as chaves não são interpretadas como expressões.
**Solução:** Adicionar `f`: `print(f" Item 2:        R$ {total_item2:.2f}")`

---

## Erro 4: Comparação de String com Número (Linha 34)
**Localização:** `if desconto_cupom > 0:`
**Problema:** Como `desconto_cupom` é uma string, não é possível compará-la com um número usando `>`.
**Solução:** Converter `desconto_cupom` para `int()` (já resolvido no Erro 2)

---

## Erro 5: Indentação Incorreta (Linha 35)
**Localização:** `print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")`
**Problema:** Esta linha deve estar indentada dentro do bloco `if`, mas está no mesmo nível.
**Solução:** Indentar a linha para estar dentro do bloco `if`

---

## Resumo dos Erros
| Linha | Tipo | Descrição |
|-------|------|-----------|
| 6 | Sintaxe | Falta aspas em string |
| 21 | Tipo de Dado | `input()` retorna string, precisa converter para `int()` |
| 29 | F-string | Falta prefixo `f` antes das aspas |
| 34 | Tipo de Dado | Comparação de string com número |
| 35 | Indentação | Linha não indentada dentro do `if` |
