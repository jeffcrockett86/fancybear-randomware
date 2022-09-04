def SUCK_THAT(DICK):
    print(DICK)
    if len(DICK) == 3:
        print("SHLURP")
        return
    return SUCK_THAT(DICK[:-1])

DICK = '8============D'
SUCK_THAT(DICK)