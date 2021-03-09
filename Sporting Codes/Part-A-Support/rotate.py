import random

def rotate(pieces):
	new_pieces = []
	for p in pieces:
		rotated = False
		if random.uniform(0,1) > 0.6:
			t = p[2]
			p[2] = p[3]
			p[3] = t

			rotated = True
			new_pieces.append(p)

		if not(rotated):
			new_pieces.append(p)

	return new_pieces
