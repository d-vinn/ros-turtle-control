class ChangeTurtleLocate():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.theta = 0
        print(self.x, self.y)

    def goup(self):
        self.y += 2
        print(self.x, self.y)
        
    def godown(self):
        self.y -= 2
        print(self.x, self.y)

    def goright(self):
        self.x += 2
        print(self.x, self.y)

    def goleft(self):
        self.x -= 2
        print(self.x, self.y)

    def reset(self):
        self.x = 0
        self.y = 0
        print(self.x, self.y)
