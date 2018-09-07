def plus_one(digits):
    for idx, digit in reversed(list(enumerate(digits))):
        digits[idx] = (digits[idx] + 1) % 10
        if digits[idx]:
            return digits