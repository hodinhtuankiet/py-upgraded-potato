def is_perfect_number(n):
    if n <= 1:
        return False
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

# Kiểm tra các số hoàn hảo từ 1 đến 10,000
perfect_numbers = [n for n in range(1, 10001) if is_perfect_number(n)]

# Hiển thị tất cả các số hoàn hảo
print("Perfect numbers between 1 and 10,000:", perfect_numbers)
