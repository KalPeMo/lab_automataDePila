class estado:
 #class State:
    def __init__(self):
        #instance fields found by Java to Python Converter:
        self.transiciones = []
        self.esEstadoFinal = False
        #self.transitions = []
        #self.isFinalState = False


    def addTransicion(self, input, pop, destination, push):
        self.transiciones.append(transicion(input, desapilar, destino, apilar))
    #def addTransition(self, input, pop, destination, push):
        #self.transitions.append(Transition(input, pop, destination, push))

    def getTransiciones(self):
        return self.transiciones
    #def getTransitions(self):
    #    return self.transitions

    def esEstadoFinal(self):
        return self.esEstadoFinal
    #def isFinalState(self):
    #    return self.isFinalState

    def cambiaEstadoaFinal(self,status):
        self.esEstadoFinal = status
    #def changeStateStatus(self, status):
    #    self.isFinalState = status


