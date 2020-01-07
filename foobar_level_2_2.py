def solution(x, y):
    delta = y - 1
    result = sum(range(x + y)) - delta
    return str(result)
