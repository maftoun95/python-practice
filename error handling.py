def divideBy(denominator):
    try:
        return 42 / denominator
    except:
        return 'Error: Invalid argument.'

print(divideBy(42))
print(divideBy(10))
print(divideBy(0))
print(divideBy(16))
