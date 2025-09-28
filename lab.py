M = 2**15
N = 100

def normalize(num, M=None, N=None):
    while len(num) > 1 and num[0] == 0:
        num = num[1:]
    return num

def from_int(num, M=2**15, N=100):
    if num == 0:
        return [0]
    digits = []
    while num > 0:
        digits.append(num % M)
        num //= M
    digits.reverse()
    return normalize(digits)

def compare(first_value, second_value):
    a = normalize(first_value[:])
    b = normalize(second_value[:])
    if len(a) > len(b):
        return 1
    if len(a) < len(b):
        return -1
    for x, y in zip(a, b):
        if x > y:
            return 1
        if x < y:
            return -1
    return 0

def sum(first_value, second_value, M, N):
    a = first_value[:]
    b = second_value[:]
    if len(a) < len(b):
        a = [0] * (len(b) - len(a)) + a
    if len(b) < len(a):
        b = [0] * (len(a) - len(b)) + b
    carry = 0
    res = [0] * (len(a) + 1)
    for i in range(len(a) - 1, -1, -1):
        s = a[i] + b[i] + carry
        res[i + 1] = s % M
        carry = s // M
    res[0] = carry
    return normalize(res)

def sub(first_value, second_value, M, N):
    if compare(first_value, second_value) == 0:
        return [0]
    if compare(first_value, second_value) == 1:
        a = first_value[:]
        b = second_value[:]
        if len(b) < len(a):
            b = [0] * (len(a) - len(b)) + b
        res = [0] * len(a)
        borrow = 0
        for i in range(len(a) - 1, -1, -1):
            val = a[i] - b[i] - borrow
            if val < 0:
                val += M
                borrow = 1
            else:
                borrow = 0
            res[i] = val
        return normalize(res)
    else:
        temp = sub(second_value, first_value, M, N)
        temp_minus_one = sub(temp, from_int(1, M, N), M, N)
        new_first = [M - 1] * N
        return sub(new_first, temp_minus_one, M, N)

def mul_small(a, k, M, N=None):
    if k == 0 or a == [0]:
        return [0]
    a = a[:]
    res = [0] * (len(a) + 1)
    carry = 0
    for i in range(len(a) - 1, -1, -1):
        prod = a[i] * k + carry
        res[i + 1] = prod % M
        carry = prod // M
    res[0] = carry
    return normalize(res)

def times(first_value, second_value, M, N):
    a = normalize(first_value[:])
    b = normalize(second_value[:])
    if a == [0] or b == [0]:
        return [0]
    res = [0] * (len(a) + len(b))

    for i in range(len(a) - 1, -1, -1):
        carry = 0
        for j in range(len(b) - 1, -1, -1):
            idx = i + j + 1
            total = res[idx] + a[i] * b[j] + carry
            res[idx] = total % M
            carry = total // M
        res[i] += carry
    return normalize(res)

def div(first_value, second_value, M, N):
    if compare(second_value, [0]) == 0:
        raise ZeroDivisionError("division by zero")
    a = normalize(first_value[:])
    b = normalize(second_value[:])
    if compare(a, b) == -1:
        return [0]
    quotient = []
    remainder = [0]
    for digit in a:
        remainder = [digit] if remainder == [0] else (remainder + [digit])
        remainder = normalize(remainder)
        
        lo, hi = 0, M - 1
        q = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            prod = mul_small(b, mid, M, N)
            if compare(prod, remainder) <= 0:
                q = mid
                lo = mid + 1
            else:
                hi = mid - 1
        quotient.append(q)
        if q:
            remainder = sub(remainder, mul_small(b, q, M, N), M, N)
    return normalize(quotient)




a = from_int(10000000000, M, N)
b = from_int(1000000000, M, N)
print(sum(a, b, M, N), sub(a, b, M, N), times(a, b, M, N), div(a, b, M, N))