
class Student:
    def __init__(self, fio, group, scores):
        self.fio = fio
        self.group = group
        self.points = scores

    def avg_scores(self):
        result = sum(self.points)/len(self.points)
        return result

    def get_fio(self):
        return self.fio