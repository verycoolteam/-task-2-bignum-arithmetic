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

def compare(first_value, second_value):
    if len(first_value) > len(second_value):
        return 1
    elif len(second_value) > len(first_value):
        return -1
    else:
        for i in range(len(first_value)):
            if first_value[i] > second_value[i]:
                return 1
            if second_value[i] > first_value[i]:
                return -1
    return 0

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

def sub(first_value, second_value, M, N):
    if compare(first_value, second_value) == 0:
        return [0]
    elif compare(first_value, second_value) == 1:
        first_len = len(first_value)
        second_len = len(second_value)
        if first_len > second_len:
            second_value = (first_len - second_len)*[0] + second_value
        carry_over = 0
        first_value.reverse()
        second_value.reverse()
        result = []
        for i in range(first_len):
            if first_value[i] >= second_value[i] + carry_over:
                res = first_value[i] - second_value[i] - carry_over
                carry_over = 0
            else:
                res = M - abs(first_value[i] - second_value[i] - carry_over)
                carry_over = 1
            result.append(res)
        result.reverse()
        return normalize(result, M, N)
            


a = from_int(0b1001, M, N)
b = from_int(0b11, M, N)
print(sub(a, b, M, N), bin(0b1001 - 0b11))