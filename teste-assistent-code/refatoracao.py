def calculate_statistics(numbers):
    """
    Calcula estatísticas básicas de uma lista de números.

    Args:
        numbers (list): Lista de números.

    Returns:
        tuple: (total, média, máximo, mínimo)
    """
    if not numbers:
        raise ValueError("A lista não pode estar vazia.")

    total = sum(numbers)
    mean = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    return total, mean, maximum, minimum

# Exemplo de uso
data = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
total, mean, maximum, minimum = calculate_statistics(data)
print("Total:", total)
print("Média:", mean)
print("Maior:", maximum)
print("Menor:", minimum)