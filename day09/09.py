INPUT = 'input.txt'

with open(INPUT, 'r') as f:
    data = f.read().split()
    nplayers = int(data[0])
    nmarbles = int(data[-2]) + 1
    nmarbles2 = int(data[-2]) * 100 + 1

scores = {i: 0 for i in range(nplayers)}
curr_player = 1
curr_marble = 1
circle = [0]

for miss_marble in range(1, nmarbles):
    # print(circle)
    if miss_marble % 23 == 0 and miss_marble:
        scores[curr_player] += miss_marble
        ix = (curr_marble - 7) % len(circle)
        scores[curr_player] += circle.pop(ix)
        curr_marble = ix
    else:
        curr_marble += 2
        curr_marble %= len(circle)
        circle.insert(curr_marble, miss_marble)

    curr_player = (curr_player + 1) % nplayers

biggest_score = max(scores.values())

print(biggest_score)

print('---- PART 2 ----')


class Marble:
    '''Linked list to speed up the process'''

    def __init__(self, value, left=None, right=None):
        self.value = value
        if left:
            self.left = left
            left.right = self
        else:
            self.left = self

        if right:
            self.right = right
            right.left = self
        else:
            self.right = self

    def get_marble_left(self, distance):
        m = self
        for i in range(distance):
            m = m.left
        return m

    def get_marble_right(self, distance):
        m = self
        for i in range(distance):
            m = m.right
        return m

    def pop(self):
        self.left.right = self.right
        self.right.left = self.left
        self.left = None
        self.right = None
        return self


scores = {i: 0 for i in range(nplayers)}
curr_player = 1

marble = Marble(0)

for miss_marble in range(1, nmarbles2):

    if miss_marble % 23 == 0 and miss_marble:
        scores[curr_player] += miss_marble
        bonus = marble.get_marble_left(7)
        scores[curr_player] += bonus.value
        marble = bonus.right
        bonus.pop()
    else:
        marble = Marble(miss_marble, marble.get_marble_right(1), marble.get_marble_right(2))

    curr_player = (curr_player + 1) % nplayers

highscore = max(scores.values())
print(highscore)
