from GridState import GridState
from copy import deepcopy, copy

def main():    
    gridArray = initializeStates()
    print (len(gridArray))
    
    for i in range(10000):
        print("Starting sweep number: %d" % (i+1))
        gridArray = sweepStates(gridArray)
        print("Finished sweep \n\n")

#    newGridArray = sweepStates(gridArray)
 #   newGridArray2 = sweepStates(newGridArray)

def initializeStates():
    print("Initializing state space")
    
    #create the grids 
    gridState0 = GridState()
    gridState0.name = "0"
    gridState0.isTerminal = True
    
    gridState1 = GridState()
    gridState1.name = "1"
    
    gridState2 = GridState()
    gridState2.name = "2"
    
    gridState3 = GridState()
    gridState3.name = "3"
    
    gridState4 = GridState()
    gridState4.name = "4"
    
    gridState5 = GridState()
    gridState5.name = "5"
    
    gridState6 = GridState()
    gridState6.name = "6"

    gridState7 = GridState()
    gridState7.name = "7"
    
    gridState8 = GridState()
    gridState8.name = "8"

    gridState9 = GridState()
    gridState9.name = "9"

    gridState10 = GridState()
    gridState10.name = "10"
    
    gridState11 = GridState()
    gridState11.name = "11"
    
    gridState12 = GridState()
    gridState12.name = "12"
    
    gridState13 = GridState()
    gridState13.name = "13"
    
    gridState14 = GridState()
    gridState14.name = "14"
    
    gridState15 = GridState()
    gridState15.name = "15"    
    
    gridState16 = GridState()
    gridState16.name = "16" 
    gridState16.isTerminal = True
    
    #set their transitions
    gridState1.leftTransitionState = gridState0
    gridState1.upTransitionState = gridState1
    gridState1.rightTransitionState = gridState2
    gridState1.downTransitionState = gridState5
    
    gridState2.leftTransitionState = gridState1
    gridState2.upTransitionState = gridState2
    gridState2.rightTransitionState = gridState3
    gridState2.downTransitionState = gridState6
    
    gridState3.leftTransitionState = gridState2
    gridState3.upTransitionState = gridState3
    gridState3.rightTransitionState = gridState3
    gridState3.downTransitionState = gridState7
    
    gridState4.leftTransitionState = gridState4
    gridState4.upTransitionState = gridState0
    gridState4.rightTransitionState = gridState5
    gridState4.downTransitionState = gridState8    

    gridState5.leftTransitionState = gridState4
    gridState5.upTransitionState = gridState1
    gridState5.rightTransitionState = gridState6
    gridState5.downTransitionState = gridState9
    
    gridState6.leftTransitionState = gridState5
    gridState6.upTransitionState = gridState2
    gridState6.rightTransitionState = gridState7
    gridState6.downTransitionState = gridState10
    
    gridState7.leftTransitionState = gridState6
    gridState7.upTransitionState = gridState3
    gridState7.rightTransitionState = gridState7
    gridState7.downTransitionState = gridState11
    
    gridState8.leftTransitionState = gridState15
    gridState8.upTransitionState = gridState4
    gridState8.rightTransitionState = gridState9
    gridState8.downTransitionState = gridState12
    
    gridState9.leftTransitionState = gridState8
    gridState9.upTransitionState = gridState5
    gridState9.rightTransitionState = gridState10
    gridState9.downTransitionState = gridState13
    
    gridState10.leftTransitionState = gridState9
    gridState10.upTransitionState = gridState6
    gridState10.rightTransitionState = gridState11
    gridState10.downTransitionState = gridState14
    
    gridState11.leftTransitionState = gridState10
    gridState11.upTransitionState = gridState7
    gridState11.rightTransitionState = gridState15
    gridState11.downTransitionState = gridState16
      
    gridState12.leftTransitionState = gridState12
    gridState12.upTransitionState = gridState8
    gridState12.rightTransitionState = gridState13
    gridState12.downTransitionState = gridState12
    
    gridState13.leftTransitionState = gridState12
    gridState13.upTransitionState = gridState9
    gridState13.rightTransitionState = gridState14
    gridState13.downTransitionState = gridState13
    
    gridState14.leftTransitionState = gridState13
    gridState14.upTransitionState = gridState10
    gridState14.rightTransitionState = gridState16
    gridState14.downTransitionState = gridState14
    
    gridState15.leftTransitionState = gridState11
    gridState15.upTransitionState = gridState7
    gridState15.rightTransitionState = gridState10
    gridState15.downTransitionState = gridState16
    
    gridArray = [gridState0, gridState1, gridState2, gridState3, gridState4, gridState5, gridState6, gridState7, gridState8, gridState9, gridState10, gridState11, gridState12, gridState13, gridState14, gridState15, gridState16]
    
    return gridArray
    
    
def sweepStates(statesToSweep):
    
    gamma = 1.0
    
    newStatesArray = deepcopy(statesToSweep)
    
    for index, item in enumerate(statesToSweep):
        state = item
        stateInNewStatesArray = newStatesArray[index]
        if (state.isTerminal == False):
            #print("Sweeping %s" % state.name)
            #if (state.name == "2"):
            #    print("Analyzing 2 *********")
            #    print ("Left %f, Up %f, Right %f, Down %f" % (state.leftTransitionState.currentValue, state.upTransitionState.currentValue, state.rightTransitionState.currentValue, state.downTransitionState.currentValue ))

            stateInNewStatesArray.currentValue = 1/4 * (-1.0 + gamma * state.leftTransitionState.currentValue) + \
                    1/4 * (-1.0 + gamma * state.upTransitionState.currentValue) + \
                    1/4 * (-1.0 + gamma * state.rightTransitionState.currentValue) + \
                    1/4 * (-1.0 + gamma * state.downTransitionState.currentValue)
            print ("Name: %s, currentValue: %f" % (stateInNewStatesArray.name, stateInNewStatesArray.currentValue))        

    return newStatesArray
    
if __name__ == "__main__":
    main()


    