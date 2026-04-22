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
    if not isinstance(n, int):
        raise TypeError("O argumento deve ser um inteiro.")

    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # Verifica divisores ímpares até a raiz quadrada de n
    max_divisor = int(n ** 0.5) + 1
    for i in range(3, max_divisor, 2):
        if n % i == 0:
            return False
    return True

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

if __name__ == "__main__":
    run_tests()