def compete_scores(a0, a1, a2, b0, b1, b2):
    # from HackerRank
    alice = 0
    bob = 0
    for a, b in zip([a0, a1, a2], [b0, b1, b2]):
        if a < b:
            bob += 1
        elif a > b:
            alice += 1
    return alice, bob
