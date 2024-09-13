from fake_math import divide2 as fake_divide
from true_math import divide1 as true_divide

result1 = fake_divide(52, 3)
result2 = fake_divide(3, 0)
result3 = true_divide(23, 7)
result4 = true_divide(145, 0)

print(result1)
print(result2)
print(result3)
print(result4)