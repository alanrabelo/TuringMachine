from TuringMachine import TuringMachine
import numpy as np
# PROBLEMA DO GATO E DO RATO
# Teremos uma fita do gato e outra do rato ou contendo a sequência de ações

# transitions rato exibe os possíveis caminhos que o rato pode executar no problema a
transitions_rato = {
    1: [1, 3, 5],
    2: [1, 2],
    3: [2, 3],
    4: [1, 4],
    5: [4, 5],
}

# Da mesma forma para o gato
transitions_gato = {
    1: [1, 2, 4],
    2: [2, 3, 4],
    3: [1, 3],
    4: [2, 4, 5],
    5: [1, 5],
}

# transitions rato exibe os possíveis caminhos que o rato pode executar no problema b
transitions_rato_b = {
    1: [1, 3],
    2: [1, 2],
    3: [2, 3],
    4: [1, 4],
    5: [4, 5],
}

# Da mesma forma para o gato
transitions_gato_b = {
    1: [1, 2, 4],
    2: [2, 3, 4],
    3: [1, 3],
    4: [2, 4],
    5: [1, 5],
}

# Transições vazias inicialmente
cat_mouse_transitions = {
                        'q0': {
                            '11': {'next_state': 'qReject', 'direction': ['R', 'R']},
                            '22': {'next_state': 'qReject', 'direction': ['R', 'R']},
                            '33': {'next_state': 'qReject', 'direction': ['R', 'R']},
                            '44': {'next_state': 'qReject', 'direction': ['R', 'R']},
                            '55': {'next_state': 'qReject', 'direction': ['R', 'R']},
                            '12': {'next_state': '12', 'direction': ['R', 'R']},
                            '13': {'next_state': '13', 'direction': ['R', 'R']},
                            '14': {'next_state': '14', 'direction': ['R', 'R']},
                            '15': {'next_state': '15', 'direction': ['R', 'R']},
                            '21': {'next_state': '21', 'direction': ['R', 'R']},
                            '23': {'next_state': '23', 'direction': ['R', 'R']},
                            '24': {'next_state': '24', 'direction': ['R', 'R']},
                            '25': {'next_state': '25', 'direction': ['R', 'R']},
                            '31': {'next_state': '31', 'direction': ['R', 'R']},
                            '32': {'next_state': '32', 'direction': ['R', 'R']},
                            '34': {'next_state': '34', 'direction': ['R', 'R']},
                            '35': {'next_state': '35', 'direction': ['R', 'R']},
                            '41': {'next_state': '41', 'direction': ['R', 'R']},
                            '42': {'next_state': '42', 'direction': ['R', 'R']},
                            '43': {'next_state': '43', 'direction': ['R', 'R']},
                            '45': {'next_state': '45', 'direction': ['R', 'R']},
                            '51': {'next_state': '51', 'direction': ['R', 'R']},
                            '52': {'next_state': '52', 'direction': ['R', 'R']},
                            '53': {'next_state': '53', 'direction': ['R', 'R']},
                            '54': {'next_state': '54', 'direction': ['R', 'R']},
                            '$$': {'next_state': 'qAccept', 'direction': ['R', 'R']},
                        }
                    }

from itertools import permutations

# Esta função utiliza os possíveis caminhos do gato e rato para gerar um estado para cada possível combinação de valores
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
            cat_mouse_transitions[key][sequence_as_str] = {'next_state': sequence_as_str, 'direction': ['R', 'R']}

    cat_mouse_transitions[key]['$$'] = {'next_state': 'qAccept', 'direction': ['R', 'R']}


CatMouseMachine = TuringMachine(tapes=['5415$', '3122$'],
                                states=possible_states,
                                initial_state='q0',
                                accept_state='qAccept',
                                reject_state='qReject',
                                transitions=cat_mouse_transitions,
                                tape_alphabet={'11', '22', '12', '21', '$$'},
                                input_alphabet={'11', '22', '12', '21'})

print(CatMouseMachine.run())

CatMouseMachine = TuringMachine(tapes=['54132$', '31222$'],
                                states=possible_states,
                                initial_state='q0',
                                accept_state='qAccept',
                                reject_state='qReject',
                                transitions=cat_mouse_transitions,
                                tape_alphabet={'11', '22', '12', '21', '$$'},
                                input_alphabet={'11', '22', '12', '21'})

print(CatMouseMachine.run())


# Esta função utiliza os possíveis caminhos do gato e rato para gerar um estado para cada possível combinação de valores
# Especialmente para o problema b
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
        if sequence[0] != '5' and sequence[1] != '5':
            sequence_as_str = str(sequence[0]) + str(sequence[1])
            cat_mouse_transitions[key][sequence_as_str] = {'next_state': sequence_as_str, 'direction': ['R', 'R']}

    cat_mouse_transitions[key]['$$'] = {'next_state': 'qAccept', 'direction': ['R', 'R']}


CatMouseMachine = TuringMachine(tapes=['5415$', '3122$'],
                                states=possible_states,
                                initial_state='q0',
                                accept_state='qAccept',
                                reject_state='qReject',
                                transitions=cat_mouse_transitions,
                                tape_alphabet={'11', '22', '12', '21', '$$'},
                                input_alphabet={'11', '22', '12', '21'})

print(CatMouseMachine.run())

CatMouseMachine = TuringMachine(tapes=['54132$', '31222$'],
                                states=possible_states,
                                initial_state='q0',
                                accept_state='qAccept',
                                reject_state='qReject',
                                transitions=cat_mouse_transitions,
                                tape_alphabet={'11', '22', '12', '21', '$$'},
                                input_alphabet={'11', '22', '12', '21'})

print(CatMouseMachine.run())



