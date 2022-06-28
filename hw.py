def fibs_up_to(x):
    result = [1, 1]
    while result[-1] + result[-2] <= x:
        result.append(result[-2] + result[-1])
    return result
