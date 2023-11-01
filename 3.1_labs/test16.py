lngth = int(input())
line = []
for _ in range(int(input())):
    line.append(input())
for i in line:
    if lngth > 3:
        if len(i) >= lngth - 3:
            print(i[:lngth - 3] + "...")
            break
        else:
            if lngth == 4:
                print(i + "...")
                break
            else:
                print(i)
            lngth -= len(i)
