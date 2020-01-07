def solution(data, n): 
    result = data[:]

    for unique_number in set(data):
        if data.count(unique_number) > n:
            result[:] = (number for number in result if number != unique_number)
            
    return result
