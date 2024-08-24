"""
Qus 2. Given three integers x, y, and z, the task is to find the sum of all the numbers formed by
having 4 at most x times, having 5 at most y times, and having 6 at most z times as a digit.

Note: Output the sum modulo 10^9+7.
"""

# Method 1
from itertools import permutations

MOD = 10 ** 9 + 7


def generate_and_sum(x, y, z):
    digits = []
    if x > 0:
        digits.extend(['4'] * x)
    if y > 0:
        digits.extend(['5'] * y)
    if z > 0:
        digits.extend(['6'] * z)

    unique_numbers = set()

    # Generate all permutations of the available digits
    for i in range(1, len(digits) + 1):
        for perm in permutations(digits, i):
            number = int(''.join(perm))
            unique_numbers.add(number)

    # Sum all unique numbers modulo MOD
    total_sum = sum(unique_numbers) % MOD
    return total_sum


x, y, z = 1, 1, 1
print(generate_and_sum(x, y, z))  # Expected output: 3675


# Method 2
MOD = 10 ** 9 + 7


def generate_numbers(current_num, count4, count5, count6, x, y, z, total_sum):
    if count4 == x and count5 == y and count6 == z:
        if current_num:
            print(current_num)
            total_sum[0] = (total_sum[0] + int(current_num)) % MOD
        return

    if current_num:
        print(total_sum)
        total_sum[0] = (total_sum[0] + int(current_num)) % MOD

    # Add more '4's if possible
    if count4 < x:
        generate_numbers(current_num + '4', count4 + 1, count5, count6, x, y, z, total_sum)

    # Add more '5's if possible
    if count5 < y:
        generate_numbers(current_num + '5', count4, count5 + 1, count6, x, y, z, total_sum)

    # Add more '6's if possible
    if count6 < z:
        generate_numbers(current_num + '6', count4, count5, count6 + 1, x, y, z, total_sum)


def sum_of_all_combinations(x, y, z):
    total_sum = [0]
    generate_numbers("", 0, 0, 0, x, y, z, total_sum)
    return total_sum[0]


# Example 1
x, y, z = 1, 1, 1
print(sum_of_all_combinations(x, y, z))  # Expected output: 3675
