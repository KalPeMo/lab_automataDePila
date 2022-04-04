#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to multiple constructors:
#ORIGINAL LINE: Transition(String input, String pop, int destination, String push)
class transicion
 #class Transition
    def __init__(self, input, desapilar, destino, apilar):

        self.input = input
        self.apilar = apilar
        self.destino = destino
        self.desapilar = desapilar
        #self.input = input
        #self.pop = pop
        #self.destination = destination
        #self.push = push

    def getInput(self):
        return self.input

    def getDespilar(self):
        return self.desapilar
    #def getPop(self):
    #    return self.pop

    def getApilar(self):
        return self.apilar
    #def getPush(self):
    #    return self.push

    def getDestino(self):
        return self.destino
    #def getDestination(self):
    #    return self.destination
