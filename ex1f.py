def factors(n):
    if n <= 0:
        raise ValueError("Number must be positive.")
    l = []
    for i in range(1, n + 1):
        if n % i == 0:
            l.append(i)
    return l
def prime_factors(n):
    if n <= 1:
        raise ValueError("Number must be greater than 1.")
    l = []
    i = 2
    while n > 1:
        if n % i == 0:
            l.append(i)
            n //= i
        else:
            i += 1
    return l
if __name__ == "__main__":
    num = 60
    print(f"Factors of {num}: {factors(num)}")
    print(f"Prime factors of {num}: {prime_factors(num)}")
