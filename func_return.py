def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'Числа равны'
    else:
        return y
    
print(maximum(2, 3))
print(maximum(3, 3))
print(maximum(2, 1))
