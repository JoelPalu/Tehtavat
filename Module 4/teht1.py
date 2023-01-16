num = 0

while num < 1000:
    devide = 0
    devide = num / 3
    devide_int = int(devide)
    while (devide - devide_int) == 0:
        print(num)
        devide = devide +1
    num = num + 1
