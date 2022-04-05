 /*
 * Lamda es representado por un . (fin de secuencia)
 * El símbolo de inicio de la pila es $ (pila vacía)
 * Los símbolos de entrada pueden ser cualesquiera excepto los de pila vacía y fin de secuencia
 * El simbolo inicial está estrictamente codificado con 0
  */
package lab_automataDePila;
import java.util.Scanner;
import java.util.Stack;

public class lab_automataDePila {

	// Variable globales
	public static int currentState = 0; //  Estado actual en el que nos encontramos
	public static int stateAmount; // numero total de estados de nuestro automata
	public static String alphabet; // Los símbolos de nuestro automata
	public static Stack<String> stack; // pila del automata
	public static State[] states; // Arreglo que contiene los estados de nuestro automata
	public static Scanner reader = new Scanner(System.in); // objeto de la clase escaner para leer caracter por caracter
	public static boolean isStringAcceptable = false; // VValor boolean que se torna en true si la hilera ingresada es aceptada
	public static boolean wasThereProperTransition = false; // valor boolean que se torna en true si existe una transición adecuada de un estado a otro
	public static String lambda = "."; // se usa el . para la representación de lambda

	public static void main(String[] args) {

		stack = new Stack<String>();
		stack.push("$"); // simbolo de entrada para la pila

		// se le pide al usuario que ingrese el numero de estados
		System.out.print("Ingrese el numero de estados: ");
		stateAmount = reader.nextInt();
		states = new State[stateAmount];
		for (int i = 0; i < stateAmount; i++) // se instancian los estados
			states[i] = new State();

		//se crea nuestro alfabeto
		System.out.print("Ingrese el alfabeto delimitado por espacios: ");
		alphabet = reader.next();

		// Crea las transiciones que tenemos
		System.out.println("Ingrese la transicion o -1 para finalizar: ");
		boolean isTransitionCreationDone = false;
		do {
			int stateSource = reader.nextInt();
			if (stateSource == -1)
				isTransitionCreationDone = true;
			else
				states[stateSource].addTransition(reader.next(), reader.next(), reader.nextInt(), reader.next());
		} while (!isTransitionCreationDone);

		// se asigna los estados finales
		System.out.print("Ingrese los estados que desea establecer como finales separados por espacio y luego digite -1  para continuar: ");
		boolean isFinalStateCreationDone = false;
		do {
			int finalState = reader.nextInt();
			if (finalState == -1)
				isFinalStateCreationDone = true;
			else
				states[finalState].changeStateStatus(true);
		} while (!isFinalStateCreationDone);

		// se inicia el proceso de validacion de las cadenas
		System.out.println(" Ingrese la cadena a validar y luego digite -1 para finalizar: ");
		boolean continueTestingStrings = true;
		while (continueTestingStrings) {
			currentState = 0;
			testStrings();
			System.out.println("Desea continuar probando hileras S/N?");
			if (!reader.next().toLowerCase().equals("S"))
				continueTestingStrings = false;
			stack.clear();
			stack.push("$");
			isStringAcceptable = false;
		}

		reader.close();
		System.out.println("Fin del programa");
	}

	public static  boolean userInput(String inputedString) {
		int transitionNumber = findProperTransition(inputedString);
		if (transitionNumber >= 0) { // se encontró una transición adecuada por lo que el número de transición no volvió a ser negativo
			popOutOfStack(transitionNumber);
			pushOntoStack(transitionNumber);
			currentState = states[currentState].getTransitions().get(transitionNumber).getDestination(); // Cambia el estado actual
			// siguiente ubicación
			wasThereProperTransition = true;
			return false;
		} else { // si la entrada no tiene una transición correcta, el programa finaliza y la hilera no se acepta
			isStringAcceptable = false;
			wasThereProperTransition = false;
			return true;
		}
	}

	public static void testStrings() {
		boolean isInputtingStringDone = false;
		do {
			System.out.print("Estado actual: " + currentState + ": ");
			// pone de salida lo que está en la hilera
			for (int i = stack.size() - 1; i >= 0; i--)
				System.out.print(stack.elementAt(i));

			System.out.print(", Ingresa un solo simbolo: ");

			String inputedString = reader.next();
			if (!inputedString.equals("-1")) { // if it's -1 we end the string input
				if (alphabet.contains(inputedString) || inputedString.equals(lambda))
					isInputtingStringDone = userInput(inputedString);
				else {
					isInputtingStringDone = true;
					isStringAcceptable = false;
				}

			} else { // si la entrada es -1
				isInputtingStringDone = true;
			}

		} while (!isInputtingStringDone);

		// revisa si la hilera es aceptable y que el usuario ingresó de forma correcta el fin de sus datos
		// entrada, transicion no incorrecta
		if (states[currentState].isFinalState() && wasThereProperTransition) {
			isStringAcceptable = true;
		} else
			isStringAcceptable = false;

		if (!isStringAcceptable)
			System.out.println("La hilera no se acepta");
		else
			System.out.println("La hilera se acepta");
	}

	public static void pushOntoStack(int transitionNumber) {
		if (!states[currentState].getTransitions().get(transitionNumber).getPush().equals(".")) // si no es igual
																								// . se añade algo
		{
			for (int j = states[currentState].getTransitions().get(transitionNumber).getPush().length()
					- 1; j >= 0; j--) {

				stack.push(Character
						.toString(states[currentState].getTransitions().get(transitionNumber).getPush().charAt(j)));
			}
		}
	}

	public static void popOutOfStack(int transitionNumber) {
		for (int j = 0; j < states[currentState].getTransitions().get(transitionNumber).getPop().length(); j++) {
			if (Character.toString(states[currentState].getTransitions().get(transitionNumber).getPop().charAt(j))
					.equals(stack.peek())) {
				stack.pop();
			}
		}
	}

	public static int findProperTransition(String inputedString) {
		// transición traversa del estado actual y verifica se se tiene una transición para la hilera ingresada
		for (int i = 0; i < states[currentState].getTransitions().size(); i++) {
			// si se encuentra una entrada que es igual a la hilera ingresada
			if (states[currentState].getTransitions().get(i).getInput().equals(inputedString)) {
				// Revise si la pila tiene lo que necesita
				for (int j = 0; j < states[currentState].getTransitions().get(i).getPop().length(); j++) {
					if (Character.toString(states[currentState].getTransitions().get(i).getPop().charAt(j))
							.equals(stack.elementAt(stack.size() - 1 - j))) {
						return i;
					}
				}
			}
		}
		return -1; // Si llegó hasta aquí la trnasición no está correcta
	}
