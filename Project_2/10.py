# 练习10：代码计算100以内的偶数和
s = 0
for i in range(2, 101):
    if i % 2 == 0:
        s += i
print('100以内的偶数和为:', s)
