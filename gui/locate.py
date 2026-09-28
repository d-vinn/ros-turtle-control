class ChangeTurtleLocate():
    def __init__(self):
        self.x = 5.5
        self.y = 5.5
        self.theta = 0.0
        print(self.x, self.y)

    def goup(self):
        self.y += 2.0
        self.theta = 1.57
        print(self.x, self.y)
        
    def godown(self):
        self.y -= 2.0
        self.theta = -1.57
        print(self.x, self.y)

    def goright(self):
        self.x += 2.0
        self.theta = 0.0
        print(self.x, self.y)

    def goleft(self):
        self.x -= 2.0
        self.theta = 3.14
        print(self.x, self.y)

    def reset(self):
        self.x = 5.5
        self.y = 5.5
        self.theta = 0.0
        print(self.x, self.y)
