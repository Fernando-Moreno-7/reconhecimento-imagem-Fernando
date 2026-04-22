# Explicação Técnica da Função is_prime

## Visão Geral

A função `is_prime(n)` é implementada em Python para verificar se um número inteiro `n` é primo. Um número primo é definido como um número natural maior que 1 que não possui divisores positivos além de 1 e ele mesmo.

Esta implementação segue princípios de clean code, incluindo type hints, validação de entrada, documentação detalhada e separação de responsabilidades.

## Assinatura da Função

```python
from typing import Union

def is_prime(n: int) -> bool:
    """
    Verifica se um número inteiro é primo.

    Um número primo é um número natural maior que 1 que não possui
    divisores positivos além de 1 e ele mesmo.

    Args:
        n (int): O número inteiro a ser verificado. Deve ser não-negativo.

    Returns:
        bool: True se o número for primo, False caso contrário.

    Raises:
        TypeError: Se n não for um inteiro.

    Examples:
        >>> is_prime(2)
        True
        >>> is_prime(4)
        False
    """
```

- **Parâmetros**: `n` (int) - O número a ser testado.
- **Retorno**: `bool` - Verdadeiro se primo, falso caso contrário.
- **Exceções**: `TypeError` se a entrada não for um inteiro.

## Lógica da Função

A função segue uma abordagem eficiente para verificar a primalidade:

1. **Validação de entrada**:
   - Verifica se `n` é um inteiro; caso contrário, lança `TypeError`.

2. **Verificação de casos base**:
   - Se `n <= 1`, retorna `False` porque números menores ou iguais a 1 não são primos.
   - Se `n == 2`, retorna `True` porque 2 é o único número primo par.
   - Se `n % 2 == 0`, retorna `False` porque números pares maiores que 2 não são primos.

3. **Loop de verificação**:
   - Calcula o divisor máximo como `int(n ** 0.5) + 1`.
   - Itera de 3 até o divisor máximo, pulando números pares (passo 2).
   - Para cada `i`, verifica se `n % i == 0`. Se sim, retorna `False`.
   - Se nenhum divisor for encontrado, retorna `True`.

## Complexidade de Tempo

- **Melhor caso**: O(1) - Para `n <= 1`, `n == 2`, ou `n` par.
- **Pior caso**: O(√n) - O loop executa até √n, com verificações a cada dois números.

Essa implementação é eficiente para números grandes, pois evita verificar todos os números até `n`.

## Casos de Teste

A função `run_tests()` executa testes automatizados:

```python
def run_tests():
    """Executa testes simples para a função is_prime."""
    test_cases = [
        (2, True),
        (3, True),
        (4, False),
        (17, True),
        (18, False),
        (1, False),
        (0, False),
        (-5, False),
    ]

    print("Executando testes:")
    for num, expected in test_cases:
        result = is_prime(num)
        status = "PASS" if result == expected else "FAIL"
        print(f"is_prime({num}) = {result} ({status})")
```

## Princípios de Clean Code Aplicados

- **Type Hints**: Uso de anotações de tipo para clareza e detecção de erros.
- **Validação de Entrada**: Verificação de tipo para robustez.
- **Documentação**: Docstring detalhada seguindo convenções do Google.
- **Separação de Responsabilidades**: Função de teste separada do código principal.
- **Nomes Descritivos**: Variáveis como `max_divisor` para legibilidade.
- **Comentários**: Explicações inline onde necessário.
- **Testes**: Cobertura de casos edge, incluindo negativos e zero.

## Considerações

- A função assume que `n` é um inteiro. Lança erro para tipos inválidos.
- Para números muito grandes, algoritmos mais avançados como Miller-Rabin podem ser necessários.
- A implementação é pura Python, sem dependências externas além de `typing`.