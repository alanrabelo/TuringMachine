from TuringMachine import TuringMachine
import numpy as np
# PROBLEMA DO GATO E DO RATO
# Teremos uma fita do gato e outra do rato ou contendo a sequência de ações
# Gerar as transições baseados no grafo

transitions_rato = {
    1: [1, 3, 5],
    2: [1, 2],
    3: [2, 3],
    4: [1, 4],
    5: [4, 5],
}

transitions_gato = {
    1: [1, 2, 4],
    2: [2, 3, 4],
    3: [1, 3],
    4: [2, 4, 5],
    5: [1, 5],
}

cat_mouse_transitions = {
                        'q0': {
                            '11': {'next_state': 'qReject', 'direction': 'R'},
                            '22': {'next_state': 'qReject', 'direction': 'R'},
                            '33': {'next_state': 'qReject', 'direction': 'R'},
                            '44': {'next_state': 'qReject', 'direction': 'R'},
                            '55': {'next_state': 'qReject', 'direction': 'R'},
                            '12': {'next_state': '12', 'direction': 'R'},
                            '13': {'next_state': '13', 'direction': 'R'},
                            '14': {'next_state': '14', 'direction': 'R'},
                            '15': {'next_state': '15', 'direction': 'R'},
                            '21': {'next_state': '21', 'direction': 'R'},
                            '23': {'next_state': '23', 'direction': 'R'},
                            '24': {'next_state': '24', 'direction': 'R'},
                            '25': {'next_state': '25', 'direction': 'R'},
                            '31': {'next_state': '31', 'direction': 'R'},
                            '32': {'next_state': '32', 'direction': 'R'},
                            '34': {'next_state': '34', 'direction': 'R'},
                            '35': {'next_state': '35', 'direction': 'R'},
                            '41': {'next_state': '41', 'direction': 'R'},
                            '42': {'next_state': '42', 'direction': 'R'},
                            '43': {'next_state': '43', 'direction': 'R'},
                            '45': {'next_state': '45', 'direction': 'R'},
                            '51': {'next_state': '51', 'direction': 'R'},
                            '52': {'next_state': '52', 'direction': 'R'},
                            '53': {'next_state': '53', 'direction': 'R'},
                            '54': {'next_state': '54', 'direction': 'R'},
                            '$$': {'next_state': 'qAccept', 'direction': 'R'},
                        }
                    }

from itertools import permutations

possible_indexes = list(permutations(list(transitions_gato.keys()), 2))
possible_states = ['q0', 'qAccept', 'qReject']

for index in possible_indexes:
    rato_index = index[0]
    gato_index = index[1]
    key = str(rato_index) + str(gato_index)
    possible_states.append(key)

    possible_values_for_rato = transitions_rato[rato_index]
    possible_values_for_gato = transitions_gato[gato_index]

    possible_sequences = np.array(np.meshgrid(possible_values_for_rato, possible_values_for_gato)).T.reshape(-1,2)

    cat_mouse_transitions[key] = {}

    for sequence in possible_sequences:
        if sequence[0] != sequence[1]:
            sequence_as_str = str(sequence[0]) + str(sequence[1])
            cat_mouse_transitions[key][sequence_as_str] = {'next_state': sequence_as_str, 'direction': 'R'}

    cat_mouse_transitions[key]['$$'] = {'next_state': 'qAccept', 'direction': 'R'}


CatMouseMachine = TuringMachine(tapes=['5415$', '3122$'],
                                states=possible_states,
                                initial_state='q0',
                                accept_state='qAccept',
                                reject_state='qReject',
                                transitions=cat_mouse_transitions,
                                tape_alphabet={'11', '22', '12', '21', '$$'},
                                input_alphabet={'11', '22', '12', '21'})

print(CatMouseMachine.run())
