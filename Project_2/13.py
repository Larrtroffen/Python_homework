# 练习13：一张纸对折对少次能到珠穆朗玛
x = 0.08
y = 8848.13 * 1000
c = 0
while 1:
    x *= 2
    c += 1
    if x >= y:
        print('对折%d次可以达到珠峰高度' % c)
        break
