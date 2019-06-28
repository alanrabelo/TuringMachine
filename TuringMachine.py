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

    def __init__(self, tapes, states, initial_state, accept_state,
                 reject_state, transitions, tape_alphabet, input_alphabet):

        if not input_alphabet.issubset(tape_alphabet):
            raise InputNotInTapeAlphabetError("Input alphabet must be a subset of tape alphabet")

        if ' ' in input_alphabet:
            raise EmptyStringInAlphabetError("Empty values should not be in input alphabet")

        if accept_state == reject_state:
            raise InitialAndFinalStatesAreEqualError("Initial and final states are equal. Not possible in a Machine")

        self.tapes = [list(tape) for tape in tapes]
        self.states = states
        self.input_alphabet = input_alphabet
        self.tape_alphabet = tape_alphabet
        self.transitions = transitions
        self.initial_state = initial_state
        self.accept_state = accept_state
        self.reject_state = reject_state
        self.current_state = self.initial_state
        self.current_index = [0] * len(tapes)


    def run(self):

        while (self.current_state is not self.accept_state) and (self.current_state is not self.reject_state):

            input = ''

            for index, tape in enumerate(self.tapes):

                input += tape[self.current_index[index]]

            if self.current_state not in self.transitions or input not in self.transitions[self.current_state]:
                return 'Rejected'

            transition = self.transitions[self.current_state][input]

            next_state = transition['next_state']

            tape_direction = transition['direction']

            if 'word' in transition:

                word_to_write = transition['word']

                for index, value in enumerate(self.tapes):

                    if word_to_write[index]:
                        value[self.current_index[index]] = word_to_write[index]

            for index, direction in enumerate(tape_direction):

                if direction is 'L' and self.current_index[index] is not 0:
                    self.current_index[index] -= 1

                if direction is 'R' and self.current_index[index] < len(self.tapes[index])-1:
                    self.current_index[index] += 1

            self.current_state = next_state

        return "Accepted" if self.current_state == self.accept_state else "Rejected"


