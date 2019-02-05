class BasePair:
    def __init__(self, nOne, nTwo, orientation, interaction):
        self.nOne = nOne
        self.nTwo = nTwo
        self.orientation = orientation
        self.interaction = interaction

    def setPair(self, nOne, nTwo):
        self.nOne = nOne
        self.nTwo = nTwo

    def setOrientation(self, orientation):
        self.orientation = orientation

    def setInteraction(self, interaction):
        self.interaction = interaction

    def nOne(self, nOne):
        self.nOne = nOne

    def nOne(self, nTwo):
        self.nTwo = nTwo

    def show(self):
        print(self.nOne.index, self.nTwo.index, self.nOne.label, self.nTwo.label, self.interaction, self.orientation)