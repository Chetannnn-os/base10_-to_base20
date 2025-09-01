def base20(n: int) -> str:
    # Digits mapping: 0 → A, 1 → B, ..., 19 → T
    digits = [chr(ord('A') + i) for i in range(20)]
    
    if n == 0:
        return digits[0]  # "A" for zero
    
    result = []
    while n > 0:
        remainder = n % 20
        result.append(digits[remainder])  # get corresponding base20 digit
        n //= 20
    
    # The digits were collected in reverse order
    return ''.join(reversed(result))


# Example tests
print(base20(0))    # A
print(base20(19))   # T
print(base20(20))   # BA
print(base20(400))  # KKA (example)
