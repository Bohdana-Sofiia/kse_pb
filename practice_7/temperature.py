def c_to_f(celsius):
    f = celsius * 1.8 + 32
    return f

def f_to_c(far):
    c = 5/9*(far-32)
    return c

print(c_to_f(20))
print(f_to_c(68))
