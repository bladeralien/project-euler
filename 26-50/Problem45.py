startt, startp, starth = 286, 167, 144
while True:
    triangle = startt * (startt + 1) / 2
    print(triangle)
    while startp * (startp * 3 - 1) / 2 < triangle:
        startp += 1
    while starth * (starth * 2 - 1) < triangle:
        starth += 1   
    if startp * (startp * 3 - 1) / 2 == triangle and starth * (starth * 2 - 1) == triangle:
        print(triangle)
        break
    startt += 1
