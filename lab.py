M = 2
N = 4

def from_int(num, M, N):
    result = []
    for i in range(N):
        new_element = num % M
        result.append(new_element)
        num //= M
    result.reverse()
    return normalize(result, M, N)

def normalize(num, M, N):
    while num[0] == 0 and len(num) > 1:
        num = num[1:]
    return num

def sum(first_value, second_value, M, N):
    first_len = len(first_value)
    second_len = len(second_value)
    max_len = max(first_len, second_len) + 1
    first_value = (max_len - first_len)*[0] + first_value
    second_value = (max_len - second_len)*[0] + second_value
    first_value.reverse()
    second_value.reverse()
    result = []
    carry_over = 0
    for i in range(max_len):
        res = first_value[i] + second_value[i] + carry_over
        result.append(res % M)
        if res >= M:
            carry_over = 1
        else:
            carry_over = 0
    if len(result) > N:
        result = result[:N]
    result.reverse()
    return normalize(result, M, N)

a = from_int(0b1111, M, N)
b = from_int(0b11, M, N)
print(sum(a, b, M, N))