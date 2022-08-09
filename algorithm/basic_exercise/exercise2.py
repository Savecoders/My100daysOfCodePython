
# filter 0 false and list void from list

scoresCorrupted = [1, 23, 4, 2, 6, False, 0, []]

scores = list(filter(lambda score: score, scoresCorrupted))

print(scores)
