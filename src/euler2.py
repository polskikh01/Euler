def dxdy(x, y, dy):
    f = dy + 2 * x - 2
    return f


h = 0.1

x = [0]
y = [1]
dy = [1]
n = 0

for i in range(11):
    x.append(x[i] + h)
    y.append(y[i] + h * dy[i])
    dy.append(dy[i] + h * dxdy(x[i], y[i], dy[i]))
    print("%.1f, %.5f, %.5f" % (x[i], y[i], dy[i]))

