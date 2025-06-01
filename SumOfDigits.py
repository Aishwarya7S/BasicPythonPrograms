def sum_of_digits(n):
    return sum(int(d) for d in str(n))

print(sum_of_digits(12345))