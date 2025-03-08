meal_cost = float(input("Nhập chi phí bữa ăn: "))

tax = meal_cost * 0.05

tip = meal_cost * 0.18

total_cost = meal_cost + tax + tip

print(f"Chi phí bữa ăn: {meal_cost:.2f}")
print(f"Tiền thuế: {tax:.2f}")
print(f"Tiền boa: {tip:.2f}")
print(f"Tổng tiền (bao gồm thuế và tiền boa): {total_cost:.2f}")
