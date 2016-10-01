class GridState:
    
    currentValue = 0.0
    name = ""
    isTerminal = False
    
    
    def __init__(self):
        print("Initializing GridState from GridState.py")
        
    def printGridState(self):
        print ("Name: %s, currentValue: %d" % (self.name, self.currentValue))
        
    def setTransitions(self, leftTransitionState, rightTransitionState, upTransitionState, downTransitionState):
        self.leftTransitionState = leftTransitionState
        self.rightTransitionState = rightTransitionState
        self.upTransitionState = upTransitionState
        self.downTransitionState = downTransitionState