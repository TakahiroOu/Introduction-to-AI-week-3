import random

def sample():
    B = random.random() < 0.9
    R = B and random.random() < 0.9
    I = B and random.random() < 0.95
    G = random.random() < 0.95
    S = I and G and random.random() < 0.99
    M = S and random.random() < 0.99
    return B, R, I, G, S, M

data = [sample() for _ in range(100000)]

# P(B | R, G, not S)
matching = 0
hits = 0
for B, R, I, G, S, M in data:
    if R and G and not S:
        matching += 1
        if B:
            hits += 1
print("P(B | R, G, not S) =", hits / matching)

# P(S | R, I, G)
matching = 0
hits = 0
for B, R, I, G, S, M in data:
    if R and I and G:
        matching += 1
        if S:
            hits += 1
print("P(S | R, I, G)     =", hits / matching)

# P(S | not R, I, G)
matching = 0
hits = 0
for B, R, I, G, S, M in data:
    if not R and I and G:
        matching += 1
        if S:
            hits += 1
print("P(S | not R, I, G) =", hits / matching)


#P(B | R, G, not S) = 1.0, Radio is on, so Battery must work
#P(S | R, I, G)     = 0.9898464012647704, same value with the picture from the slide
#P(S | not R, I, G) = 0.9895117992258708, radio  is off, but the car still starts because the battery is working