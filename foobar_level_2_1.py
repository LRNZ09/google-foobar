def compare(x, y):
    numbers_x = x.split('.')
    numbers_y = y.split('.')
    
    # Major
    try:
        major_x = int(numbers_x[0])
    except IndexError:
        if len(numbers_x) < len(numbers_y):
            return -1

        major_x = 0

    try:
        major_y = int(numbers_y[0])
    except IndexError:
        if len(numbers_x) > len(numbers_y):
            return 1

        major_y = 0
        
    if major_x != major_y:
        if major_x < major_y:
            return -1
        if major_x > major_y:
            return 1
            
    # Minor
    try:
        minor_x = int(numbers_x[1])
    except IndexError:
        if len(numbers_x) < len(numbers_y):
            return -1

        minor_x = 0
        
    try:
        minor_y = int(numbers_y[1])
    except IndexError:
        if len(numbers_x) > len(numbers_y):
            return 1

        minor_y = 0
        
    if minor_x != minor_y:
        if minor_x < minor_y:
            return -1
        if minor_x > minor_y:
            return 1

    # Revision
    try:
        revision_x = int(numbers_x[2])
    except IndexError:
        if len(numbers_x) < len(numbers_y):
            return -1

        revision_x = 0
        
    try:
        revision_y = int(numbers_y[2])
    except IndexError:
        if len(numbers_x) > len(numbers_y):
            return 1

        revision_y = 0
        
    if revision_x != revision_y:
        if revision_x < revision_y:
            return -1
        if revision_x > revision_y:
            return 1

    return 0

def solution(l):
    result = list(set(l))
    result.sort(cmp=compare)
    return result
