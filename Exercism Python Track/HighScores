"""
Instructions:
Manage a game player's High Score list.

Your task is to build a high-score component of the classic Frogger game, one of the highest selling and addictive games of all time, and a classic of the arcade era.
Your task is to write methods that return the highest score from the list, the last added score and the three highest scores.
"""

class HighScores(object):
    def __init__(self, scores):
        self.scores = scores
        self.sorted = sorted(scores)

    def scores(self):
        return self.scores

    def latest(self):
        return self.scores[-1]

    def personal_best(self):
        return self.sorted[-1]

    def personal_top_three(self):
        return self.sorted[-1:-4:-1]

