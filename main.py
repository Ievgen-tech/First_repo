import math

def solve_quadratic(a, b, c):
    print(f"Рівняння: {a}x² + {b}x + {c} = 0")
    discriminant = b**2 - 4*a*c
    print(f"Дискримінант: {discriminant}")

    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return f"Два дійсних корені: x₁ = {x1:.2f}, x₂ = {x2:.2f}"
    elif discriminant == 0:
        x = -b / (2*a)
        return f"Один дійсний корінь: x = {x:.2f}"
    else:
        real_part = -b / (2*a)
        imag_part = math.sqrt(-discriminant) / (2*a)
        return f"Комплексні корені: x₁ = {real_part:.2f} + {imag_part:.2f}i, x₂ = {real_part:.2f} - {imag_part:.2f}i"

# Приклад використання
a = 1
b = -3
c = 2
result = solve_quadratic(a, b, c)
print(result)