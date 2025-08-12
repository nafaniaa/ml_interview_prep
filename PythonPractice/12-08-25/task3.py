# def filter_scores(scores):
#     new_scores = {}
#     for key, value in scores.items():
#         if value > 80:
#             new_scores[key] = value
#     return new_scores

# best_scores = filter_scores({"Аня": 85, "Боб": 70, "Виктор": 90})
# print(best_scores)

def filter_scores(scores):
    return {key: value for key, value in scores.items() if value > 80}

best_scores = filter_scores({"Аня": 85, "Боб": 70, "Виктор": 90})
print(best_scores)