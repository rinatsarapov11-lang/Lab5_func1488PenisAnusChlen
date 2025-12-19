def calculate_area(shape, *args):
    if shape == "круг":
        r = args[0]
        return 3.14 * r * r
    if shape == "прямоугольник":
        a = args[0]
        b = args[1]
        return a * b
    if shape == "треугольник":
        a = args[0]
        h = args[1]
        return a * h / 2
result1 = calculate_area("круг", 5 )
print(f"Площадь круга: {result1}")
result2 = calculate_area("прямоугольник", 3, 5 )
print(f"Площадь прямоугольника: {result2}")
result3 = calculate_area("треугольник", 5 , 6 )
print(f"Площадь треугольника: {result3}")