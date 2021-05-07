import re

MIN_CHARS = 50

sentence = open("sentence.txt", "r").read().lower()
print(sentence + "\n")

words = [w for w in open("words.txt", "r").read().lower().split("\n") if " " not in w and "-" not in w]

results = []

for w in words:

    cpt = sum([1 for c in sentence if re.search(c,w)])
    # cpt = sum(1 for c in w if sentence.count(c) == 1)

    tup = (w,cpt)

    results.append(tup)

results = [r for r in list(reversed(sorted(results, key=lambda tup: tup[1]))) if r[1] > MIN_CHARS]
print(results[:100])

# print("\n".join(results))
