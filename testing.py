# FILE: /testing.py

# ORIGINAL EXPRESSION:  ((√10 + 3) / (√10 - 3))

# A good guess for √10​ is x0=3, since √3 = 9 and √4 = 16.
# Babylonian Method (iterative formula): xn + 1 = (xn + (S / xn) / 2).
# 'S' is the nuymber we want the square root. S = 10.
# Iteration (xo = 3): x1 = (x0 + (10/x0) / 2) = (3 + (10 / 3) / 2) = ((3 + 3,33333333) / 2) = (6,33333333 / 2) ≈ 3,16666667. You can continue iteration.
# I made several iterations and the value of x4 is identical to x3, up to 8 decimal places provided, showing that the method has already converged to the desired precision. This is because √10 is very close to 3, and additional iterations do not significantly change the result within this precision. Therefore, I can create the code.

# Step 1: Calculate sqrt(10) using the Babylonian method (already implemented):
def calculates_square_root(n, precision=0.0001):
    estimate = (n / 2.0)
    while True:
        next_estimate = ((estimate + (n / estimate)) / 2)
        if abs(next_estimate - estimate) < precision:
            return next_estimate
        else:
            estimate = next_estimate

# Calculate sqrt(10):
sqrt_10 = calculates_square_root(10)
print(f'STEP 1: Calculate √10 numerically:')
print(f'√10 ≈ {sqrt_10}.')
print()


# Step 2: Define the original expression and the conjugate
numerator = (sqrt_10 + 3)
numerator_str = '√10 + 3' #TODO

denominator = (sqrt_10 - 3)
denominator_str = '√10 - 3' #TODO

conjugate = (sqrt_10 + 3)

print(f'STEP 2: Define the expression and multiply by the conjugate of the denominator:')
print(f'Original expression ({numerator_str} / {denominator_str}): ({numerator}) / ({denominator}).')
print(f'Multiplying numerator and denominator by Conjugate: ({conjugate}).')
print()


# Step 3: Calculate the numerator using "Squade of Sum" (a + b)^2 = (a^2 + 2ab + b^2)
print('STEP 3: Calculate the numerator using "Squade of Sum" = (a + b)^2 = (a^2 + 2ab + b^2): ')

a = sqrt_10
b = 3

term1 = (a * a) # (√10)^2
term2 = (2 * a * b) # 2(√10)(3)
term3 = (b * b) # 3^2
numerator_expanded = (term1 + term2 + term3)

print('Numerator: (√10 + 3)(√10 + 3) = (√10)^2 + 2(√10)(3) + 3^2')
print(f'(√10)^2 = {term1}')
print(f'2(√10)(3) = {term2}')
print(f'3^2 = {term3}')
print(f'Expanded numerator: {term1} + {term2} + {term3} = {numerator_expanded}.')
print()


# Step 4: Calculate the denominator using the "Difference of Squares" (a - b)(a + b) = a^2 - b^2
print('STEP 4: Calculate the denominator using the "Difference of Squares" (a - b)(a + b) = a^2 - b^2:')

term1_den = (a * a) # (√10)^2
term2_den = (b * b) # 3^2
denominator_expanded = (term1_den - term2_den)

print(f'Denominator: (√10 - 3)(√10 + 3) = (√10)^2 - 3^2')
print(f'(√10)^2 = {term1_den}')
print(f'3^2 = {term2_den}')
print(f'Expanded denominator: {term1_den} - {term2_den} = {denominator_expanded}.')
print()

# Step 5: Form the new fraction and simplify:
print('STEP 5: Form the new fraction and simplify:')

new_expression = (numerator_expanded / denominator_expanded)

print(f'New expression: ({numerator_expanded} / {denominator_expanded}).')
print(f'Numerical result: {new_expression}')
print()

# Step 6: Interpret the result to deduce the exact form using (c + (d * √10)):
print('Interpret the result to deduce the exact form using (c + (d * √10)): ')
print('Attention: The shape must be c + (d * √10). So we need to test integer values ​​for "c" and "d" until we find a match.')

precision = 0.0001
for c in range(15, 25):
    for d in range(1, 10):
        candidate = (c + (d * sqrt_10))
        if abs(candidate - new_expression) < precision:
            print(f'Exact shape found: {c} + {d}√10.')
            break
        else:
            continue
        break


# Edson Copque - https://linktr.ee/edsoncopque