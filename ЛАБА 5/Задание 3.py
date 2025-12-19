def convert(t, f, to):
    if f == 'C' and to == 'F':
        return t * 9/5 + 32
    if f == 'F' and to == 'C':
        return (t - 32) * 5/9
    if f == 'C' and to == 'K':
        return t + 273
    return t
print(convert(100, 'C', 'F'))
print(convert(32, 'F', 'C'))
print(convert(0, 'C', 'K'))