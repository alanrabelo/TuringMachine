# A máquina de Turing possui:
# 1. uma fita com dados de entrada pertencentes ao alfabeto + símbolos especiais
# 2. Um cabeçote que pode se movimentar para a esquerda e direita
# 3. A capacidade de escrever e ler os dados na fita
# 4. Um conjunto de estados Pré-definidos
# 5. Um estado inicial
# 6. Um conjunto de estados finais
# 7. Um conjunto de transições compostas por: Estado atual, próximo estado, símbolo a ser escrito, movimento do cabeçote
from enum import Enum

class InputNotInTapeAlphabetError(Exception):
    pass

class EmptyStringInAlphabetError(Exception):
    pass

class InitialAndFinalStatesAreEqualError(Exception):
    pass

class StateType(Enum):
    simple = 0
    accept = 1
    reject = 2


class TuringMachine:

    def __init__(self, tape, states, initial_state, accept_state, reject_state, transitions, tape_alphabet, input_alphabet):

        if input_alphabet not in tape_alphabet:
            raise InputNotInTapeAlphabetError("Input alphabet must be a subset of tape alphabet")

        if ' ' in input_alphabet:
            raise EmptyStringInAlphabetError("Empty values should not be in input alphabet")

        if accept_state == reject_state:
            raise InitialAndFinalStatesAreEqualError("Initial and final states are equal. Not possible in a Machine")

        self.tape = tape
        self.states = states
        self.input_alphabet = input_alphabet
        self.tape_alphabet = tape_alphabet
        self.transitions = transitions
        self.initial_state = initial_state
        self.accept_state = accept_state
        self.reject_state = reject_state
        self.current_state = self.initial_state
        self.current_index = 0


    def run(self):

        while (self.current_state is not self.accept_state) or (self.current_state is not self.reject_state):
            # Lógica da máquina aqui
            print('LOL')

        print("Accepted" if self.current_state.state_type == StateType.accept else "Rejected")


