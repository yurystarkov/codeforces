banana_price, budget, banana_num = map(int, input().split())

to_pay = sum(banana_price * i for i in range(1, banana_num + 1))

print(0 if budget >= to_pay else to_pay - budget)
