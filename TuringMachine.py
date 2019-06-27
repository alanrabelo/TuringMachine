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

    def __init__(self, tape, states, initial_state, accept_state,
                 reject_state, transitions, tape_alphabet, input_alphabet):

        if not input_alphabet.issubset(tape_alphabet):
            raise InputNotInTapeAlphabetError("Input alphabet must be a subset of tape alphabet")

        if ' ' in input_alphabet:
            raise EmptyStringInAlphabetError("Empty values should not be in input alphabet")

        if accept_state == reject_state:
            raise InitialAndFinalStatesAreEqualError("Initial and final states are equal. Not possible in a Machine")

        self.tape = list(tape)
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

        while (self.current_state is not self.accept_state) and (self.current_state is not self.reject_state):

            input = self.tape[self.current_index]

            if self.current_state not in self.transitions or input not in self.transitions[self.current_state]:
                return 'Rejected'

            transition = self.transitions[self.current_state][input]

            next_state = transition['next_state']
            symbol_to_write = transition['symbol']
            tape_direction = transition['direction']

            if symbol_to_write is not None:

                self.tape[self.current_index] = symbol_to_write

            if tape_direction is 'L' and self.current_index is not 0:
                self.current_index -= 1

            if tape_direction is 'R' and self.current_index < len(self.tape)-1:
                self.current_index += 1

            self.current_state = next_state

        return "Accepted" if self.current_state == self.accept_state else "Rejected"


