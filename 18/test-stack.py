test =  [[[[[4,3],4],4],[69,[[2,4],3]]],[1,1]]

xs = [0]
ps = [test]

while xs:
    if xs[-1] <= 1:
        if isinstance(ps[-1][xs[-1]], int):
            if ps[-1][xs[-1]] == 69:
                # Find the right integer
                psc = ps.copy()
                xsc = xs.copy()

                while xsc and xsc[-1] == 0:
                    psc.pop()
                    xsc.pop()
                if xsc:
                    xsc[-1] = 0
                while xsc:
                    if xsc[-1] >= 0 :
                        if isinstance(psc[-1][xsc[-1]], int):
                            print("The number left of 69 is %d" % psc[-1][xsc[-1]])
                            break
                        else:
                            psc.append(psc[-1][xsc[-1]])
                            xsc.append(1)
                    else:
                        xsc.pop()
                        psc.pop()
                        if xsc:
                            xsc[-1] -= 1

            xs[-1] += 1
        else:
            if len(xs) == 4:
                #ps[-1][xs[-1]] = 0
                #xs = [0]
                #ps = [test]
                xs[-1] += 1
            else:
                ps.append(ps[-1][xs[-1]])
                xs.append(0)
    else:
        xs.pop()
        ps.pop()
        if xs:
            xs[-1] += 1

