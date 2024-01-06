_, last_place = map(int, input().split())

scores = list(map(int, input().split()))

good_scores = [
    score for score in scores
    if score >= scores[last_place-1] and score > 0
]

print(len(good_scores))
