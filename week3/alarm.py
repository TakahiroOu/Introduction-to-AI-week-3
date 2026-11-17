import random

def sample():
    E = random.random() < 1 / 111
    B = random.random() < 1 / 365
    if E and B:
        A = random.random() < 0.97
    elif E:
        A = random.random() < 0.81
    elif B:
        A = random.random() < 0.92
    else:
        A = random.random() < 0.0095
    return E, B, A

def experiment(n):
    data = [sample() for _ in range(n)]

    alarms = 0
    burglar = 0
    for E, B, A in data:
        if A:
            alarms += 1
            if B:
                burglar += 1

    alarms_quake = 0
    burglar_quake = 0
    for E, B, A in data:
        if A and E:
            alarms_quake += 1
            if B:
                burglar_quake += 1

    return burglar / alarms, burglar_quake / alarms_quake

# Main experiment: n = 100 000
p1, p2 = experiment(100000)
print("n = 100000")
print("Among A=1:        fraction B=1 =", round(p1, 4))
print("Among A=1, E=1:   fraction B=1 =", round(p2, 4))

# Repeat a few times with different n to see the variability
for n in [1000, 10000, 100000, 1000000]:
    print()
    print("n =", n)
    for i in range(5):
        p1, p2 = experiment(n)
        print("  run", i + 1, ":", round(p1, 4), "  ", round(p2, 4))

# RESULTS (n = 100 000)

# 1. Among the tuples with A=1, fraction where B=1:          0.1217
# 2. Among the tuples with A=1 and E=1, fraction where B=1:  0.0053

# 3. P(B | A):    probability of a burglar, given that the alarm went off.
# 2. P(B | A, E): probability of a burglar, given that the alarm went off and there was an earthquake.

# 4. Yes. Fraction 1 is bigger: the earthquake already explains the alarm, so a burglar becomes unlikely ("explaining away").

# 5. Results vary by chance; bigger n gives less variability.
