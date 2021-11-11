def generate_number(N:int, M:int, prefix=None):
    """ Генерирует все числа (с лидирующими незначащими нулями)
        в N-й системе счисления (N <= 10)
        длины M
    """
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for digit in range(N):
        prefix.append(digit)
        generate_number(N, M-1, prefix)
        prefix.pop()



generate_number(3, 3)
