

# * 
# * Lamda es representado por un . (fin de secuencia)
# * El símbolo de inicio de la pila es $ (pila vacía)
# * Los símbolos de entrada pueden ser cualesquiera excepto los de pila vacía y fin de secuencia
# * El simbolo inicial está estrictamente codificado con 0
# 




from collections import deque
import estado
import transicion


class DeterministicPushdownAutomata():

    # Global variables
    currentState = 0 # Estado actual en el que nos encontramos
    stateAmount = 0 # pushOntoStack(int transitionNumber)
    alphabet = ""
    stack = Deque() # Los símbolos de nuestro automata
    states = [] # Arreglo que contiene los estados de nuestro automata
    isStringAcceptable = False # Valor boolean que se torna en true si la hilera ingresada es aceptada
    wasThereProperTransition = False # valor boolean que se torna en true si existe una transición adecuada de un estado a otro
    lambda_ = "." # se usa el . para la representación de lambda

    def userInput(inputedString):
        
        transitionNumber = findProperTransition(inputedString)
        
        if transitionNumber >= 0: #Se encontró una transición correcta entonces el número de transiciones no retorno negativo

            popOutOfStack(transitionNumber)
			pushOntoStack(transitionNumber)
            currentState = states[currentState].getTransiciones()[transitionNumber].getDestino()

            wasThereProperTransition = True
			return false

        else:

            isStringAcceptable = False
			wasThereProperTransition = False
			
            return true;

    def testStrings():

        isInputtingStringDone = False

        
        while True:

            print("Current Status: " + currentState + ": ",end="")

            for i in reversed(stack):
                print(i)

            print(", Enter single Input: ",end="");

			inputedString = Input()

            if inputedString != "-1": # si es -1 entonces se finaliza la hilera de entrada 

                if alphabet.find(inputedString) or inputedString == ".":
                    isInputtingStringDone = userInput(inputedString)
                
                else:
                    isInputtingStringDone = True
                    isStringAcceptable = False
            
            else:

                isInputtingStringDone = true

            if ( isInputtingStringDone == True):
                break

        # Verifica si la hilera es aceptable y si el usuario ingreso el fin de sus entradas correctamenteinput ended because of proper
		# input, transición no incorrecta
        if (states[currentState].isFinalState() and wasThereProperTransition):
			isStringAcceptable = True;
		else
			isStringAcceptable = False;

		if !isStringAcceptable:
			print("String is not Accepted.")
		else:
			print("String is Accepted.")
            

    def pushOntoStack(transitionNumber):

        if (!states[currentState].getTransitions()[transitionNumber].getApilar() != "."): #if it does not equal

            for j in reversed(range(states[currentState].getTransitions()[transitionNumber].getApilar())):

                stack.append(states[currentState].getTransitions()[transitionNumber].getApilar()[j])
    

    def popOutOfStack(transitionNumber):

        for j in 

    

            
            








    @staticmethod
    if __name__ == "__main__":

    
       stack.append("$") # Símbolo de inicio para la pila - también representa el símbolo de hilera vacia

        # aqui tenemos el número de estados y creamos un arreglo para los estados
        print("Ingrese el numero de estados: ", end = '')
        stateAmount = Input()

       for i in range(stateAmount):
           states.append(estado)


        #crea los simbolos de entrada
        print("Ingrese los símbolos de entrada sin espacios: ", end = '')
        alphabet = Input()

        #crea las transiciones
        print("Ingrese la transición o ingrese -1 para terminar ", end = '')

        isTransitionCreationDone = False

        while True:

            stateSource = Input()

            if  stateSource == "-1":
                isTransitionCreationDone = True
            else:
                stateSource = stateSource.split()


                states[stateSource[0]].addTransicion(stateSource[1],stateSource[2],int(stateSource[3]),stateSource[4])
            if ( isTransitionCreationDone ==  True):
                break

        # realiza los estados finales
        print("Ingrese los estados finales separados por espacios, después escriba -1 y presione enter:" , end = '');
        #print("Enter the Final States, seperated by spaces, and then enter -1 to continue:" , end = '');
        isTransitionCreationDone = False

        finalState = Input()
        for caracter in finalState.split():
            
            if caracter == "-1":
                isTransitionCreationDone = True
            else:
                states[int(caracter)].cambiaEstadoaFinal = True

        print("Enter a String to test, and then enter -1 to end the input: ", end = '')

        continueTestingStrings = True

        while(continueTestingStrings):

            currentState = 0
            testStrings()
            print("Continuamos revisando hileras (S/N)?",end="");
            #print("Continue Testing Strings (y/n)?",end="");
            if(Input().lower() == "S"):
                continueTestingStrings = False
                stack.clear()
                stack.append("$")
			    isStringAcceptable = false

        print("Programa finalizado",end="");




    @staticmethod
    def userInput(inputedString):
        transitionNumber = DeterministicPushDownAutomata.DeterministicPushdownAutomata.findProperTransition(inputedString)
        if transitionNumber >= 0:
            DeterministicPushDownAutomata.DeterministicPushdownAutomata.popOutOfStack(transitionNumber)
            DeterministicPushDownAutomata.DeterministicPushdownAutomata.pushOntoStack(transitionNumber)
            DeterministicPushDownAutomata.DeterministicPushdownAutomata.currentState = DeterministicPushDownAutomata.DeterministicPushdownAutomata.states[DeterministicPushDownAutomata.DeterministicPushdownAutomata.currentState].getTransitions()[transitionNumber].getDestination() # change
            # Estado actual
            # hacía la siguiente locación
            DeterministicPushDownAutomata.DeterministicPushdownAutomata.wasThereProperTransition = True
            return False
        else:
            # Aceptado
            DeterministicPushDownAutomata.DeterministicPushdownAutomata.isStringAcceptable = False
            DeterministicPushDownAutomata.DeterministicPushdownAutomata.wasThereProperTransition = False
            return True

    @staticmethod
    def testStrings():
        isInputtingStringDone = False
        condition = True
        while condition:
            print("Current Status: " + str(DeterministicPushDownAutomata.DeterministicPushdownAutomata.currentState) + ": ", end = '')
            # Salida de lo que hay en la pila
            for i in range(DeterministicPushDownAutomata.DeterministicPushdownAutomata.stack.size() - 1, -1, -1):
                print(DeterministicPushDownAutomata.DeterministicPushdownAutomata.stack.elementAt(i), end = '')

            print(", ingrese una sola entrada: ", end = '')
            #print(", Enter single Input: ", end = '')

            inputedString = DeterministicPushDownAutomata.DeterministicPushdownAutomata.reader.next()
            if inputedString != "-1":
                if inputedString in DeterministicPushDownAutomata.DeterministicPushdownAutomata.alphabet or inputedString == DeterministicPushDownAutomata.DeterministicPushdownAutomata.lambda_:
                    isInputtingStringDone = DeterministicPushDownAutomata.DeterministicPushdownAutomata.userInput(inputedString)
                else:
                    isInputtingStringDone = True
                    DeterministicPushDownAutomata.DeterministicPushdownAutomata.isStringAcceptable = False

            else:
                isInputtingStringDone = True

            condition = not isInputtingStringDone

        # verifica si la hilera es aceptable y el usuario finalizó debido a una entrada correctaended because of proper
        # input, transición no incorrecta
        if DeterministicPushDownAutomata.DeterministicPushdownAutomata.states[DeterministicPushDownAutomata.DeterministicPushdownAutomata.currentState].isFinalState() and DeterministicPushDownAutomata.DeterministicPushdownAutomata.wasThereProperTransition:
            DeterministicPushDownAutomata.DeterministicPushdownAutomata.isStringAcceptable = True
        else:
            DeterministicPushDownAutomata.DeterministicPushdownAutomata.isStringAcceptable = False

        if not DeterministicPushDownAutomata.DeterministicPushdownAutomata.isStringAcceptable:
            print("La hilera no se acepta.")
            #print("String is not Accepted.")
        else:
            print("La hilera se acepta.")
            print("String is Accepted.")

    @staticmethod
    def pushOntoStack(transitionNumber):
        if DeterministicPushDownAutomata.DeterministicPushdownAutomata.states[DeterministicPushDownAutomata.DeterministicPushdownAutomata.currentState].getTransitions()[transitionNumber].getPush() != ".": # if it does not equal
            # añadimos .
            # algo
            for j in range(len(DeterministicPushDownAutomata.DeterministicPushdownAutomata.states[DeterministicPushDownAutomata.DeterministicPushdownAutomata.currentState].getTransitions()[transitionNumber].getPush()) - 1, -1, -1):


