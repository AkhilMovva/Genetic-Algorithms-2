import puzzleDraw as d
import random
import fitnessEval as f
import split2Dpiece as s
import shuffle2DPieces as shuffle
import rotate as r
import copy


def generate(l, w, n, solution):
    pieces = [[0, 0, l, w]]
    p = pieces[0]
    while(n > 1):
        count = 0
        while(p[2] < 6 or p[3] < 6): #only picks the pieces of dimensions greater than 6
            p = random.choice(pieces) #randomly selects pieces for spliting
            count += 1
            if count > 100:
                return [],[]
        pieces.remove(p)
        p, n_p = s.split(p)
        pieces.append(p)
        pieces.append(n_p)
        n -= 1

    solved = copy.deepcopy(pieces) #has the solution
    scattered_pieces = shuffle.scatter(pieces, l, w)
    scattered_pieces = r.rotate(scattered_pieces)
    random.shuffle(scattered_pieces)

    return scattered_pieces,solved
