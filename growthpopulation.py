def nb_year(p0, percent, aug, p):
    year = 0
    percent = (100 + percent)/100
    while p0 <=p:
        if p0 == p or p0 > p:
            break
        p0 = p0 + percent + aug
        year = year + 1
        
    return year


print(nb_year(1500, 5, 100, 5000))