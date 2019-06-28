from TuringMachine import TuringMachine
import numpy as np
# PROBLEMA DO GATO E DO RATO
# Teremos uma fita do gato e outra do rato ou contendo a sequência de ações
# Gerar as transições baseados no grafo

transitions = {
                        'q00': {
                            '$ ': {'next_state': 'q0', 'word': [None, None], 'direction': ['R', None]},
                        },
                        'q0': {
                            'x ': {'next_state': 'q0', 'word': [None, None], 'direction': ['R', None]},
                            '# ': {'next_state': 'q0', 'word': [None, None], 'direction': ['R', None]},
                            '$ ': {'next_state': 'qAccept', 'word': [None, None], 'direction': ['R', None]},
                            '1 ': {'next_state': 'q1', 'word': ['x', None], 'direction': ['R', None]},
                        },
                        'q1': {
                            '# ': {'next_state': 'q2', 'word': [None, None], 'direction': ['L', None]},
                            '$ ': {'next_state': 'q2', 'word': [None, None], 'direction': ['L', None]},
                            '1 ': {'next_state': 'q3', 'word': [None, None], 'direction': ['R', None]},
                        },
                        'q2': {
                            'x ': {'next_state': 'q2', 'word': [None, 1], 'direction': ['L', 'R']},
                            '# ': {'next_state': 'q0', 'word': [None, '#'], 'direction': ['R', 'R']},
                            '$ ': {'next_state': 'q4', 'word': [None, '#'], 'direction': ['L', 'R']},
                        },
                        'q3': {
                            '# ': {'next_state': 'q0', 'word': [None, None], 'direction': ['R', None]},
                            '1 ': {'next_state': 'q3', 'word': [None, None], 'direction': ['R', None]},
                            '$ ': {'next_state': 'q4', 'word': [None, None], 'direction': ['L', None]},
                        },
                        'q4': {
                            '# ': {'next_state': 'q4', 'word': [None, None], 'direction': ['L', None]},
                            'x ': {'next_state': 'q4', 'word': [None, None], 'direction': ['L', None]},
                            '$ ': {'next_state': 'q0', 'word': [None, None], 'direction': ['R', None]},
                            '1 ': {'next_state': 'q4', 'word': [None, None], 'direction': ['L', None]},
                        }
                    }


input = '$11#1#111#1111$'
output_tape = [' '] * (len(input) + 5)
CatMouseMachine = TuringMachine(tapes=[input, output_tape],
                                states=['q00', 'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'qAccept'],
                                initial_state='q00',
                                accept_state='qAccept',
                                reject_state='qReject',
                                transitions=transitions,
                                tape_alphabet={'1', '#', '$'},
                                input_alphabet={'1'})

print(CatMouseMachine.run())
print(CatMouseMachine.tapes)