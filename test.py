def dec(f):
    def wrapper(*args, **kwargs):
        g = f(*args, **kwargs)
        g.send(None)
        return g
    return wrapper

def gen():
    x = 123
    mes = yield x
    print(mes)

#@dec
def ave():
    sum = 0
    count = 0
    ave = 0

    while True:
        try:
            print(1)
            x = yield ave
            print(2)
        except:
            pass
        else:
            count += 1
            sum += x
            ave = round(sum/count, 2)

g = dec(ave)