M = 2
N = 4

def from_int(num, M, N):
    result = []
    for i in range(N):
        new_element = num % M
        result.append(new_element)
        num //= M
    result.reverse()
    return result

print(from_int(35, M, N))
