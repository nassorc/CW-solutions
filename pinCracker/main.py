pad = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    ['',0,'']
]
def cracker(num):
    var = []
    num = [int(i) for i in str(num)]
    for i in range(len(pad)):
        for j in range(len(pad)-1):
            print(pad[i][j])
            for a in num:
                if pad[i][j] == a:
                    var.append(pad[i][j])
                    if i == 3 or j == 2:
                        if pad[i-1][j] != '':
                            var.append(pad[i-1][j])
                        if pad[i][j-1] != '':
                            var.append(pad[i][j-1])
                    else:
                        if pad[i+1][j] != '':
                            var.append(pad[i+1][j])
                        if pad[i][j+1] != '':
                            var.append(pad[i][j+1])
                        if pad[i-1][j] != '' and (i-1 != -1):
                            var.append(pad[i-1][j])
                        if pad[i][j-1] != '' and (j-1 != -1):
                            var.append(pad[i][j-1])

    return var

print(cracker(369))
