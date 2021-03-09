import random
def scatter(pieces,l,w):
    for i in pieces:
        i[0] = random.randint(0,l)
        i[1] = random.randint(0,w)

    return pieces
