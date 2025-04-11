def cand_elim(data):
    S = list(data[0][0])
    G = [['?'] * len(S)]
    for i, (x, p) in enumerate(data, 1):
        if p:  # Positive example: update S exactly and filter G.
            S = list(x)
            G = [g for g in G if all(a == '?' or a == b for a, b in zip(g, x))]
        else:  # Negative example: specialize any g that covers x.
            newG = []
            for g in G:
                if all(a == '?' or a == b for a, b in zip(g, x)):
                    for j in range(len(g)):
                        if S[j] != x[j]:
                            newg = g[:]
                            newg[j] = S[j]
                            if newg not in newG:
                                newG.append(newg)
                else:
                    if g not in newG:
                        newG.append(g)
            G = newG
        print(f"\\nAfter instance {i}:")
        print("G =", G)
        print("S =", S)

data = [
    (['sunny', 'warm', 'normal', 'strong', 'warm', 'same'], 1),
    (['sunny', 'warm', 'high',   'strong', 'warm', 'same'], 1),
    (['rainy', 'cold', 'high',   'strong', 'warm', 'change'], 0),
    (['sunny', 'warm', 'high',   'strong', 'cool', 'change'], 1)
]
cand_elim(data)
