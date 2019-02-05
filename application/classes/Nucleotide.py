class Nucleotide:
    def __init__(self, cordX=None, cordY=None, label=None, index=None, interactions=None):
        self.cordX = cordX
        self.cordY = cordY
        self.label = label
        self.index = index
        self.interactions = interactions

    def setCords(self, cordX, cordY):
        self.cordX = cordX
        self.cordY = cordY

    def setLabel(self, label):
        self.label = label

    def setnonCanonical(self, interactions):
        self.interactions = interactions

    def show(self):
        print(self.cordX)
        print(self.cordY)
        print(self.label)
        print(self.index)
        print(self.interactions)