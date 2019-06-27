from TuringMachine import TuringMachine

# PROBLEMA DO GATO E DO RATO
# Teremos uma fita do gato e outra do rato ou contendo a sequência de ações
# Gerar as transições baseados no grafo

cat_mouse_transitions = {
                    'q0': {
                        '11': {'next_state': 'qReject', 'symbol': None, 'direction': 'R'},
                        '22': {'next_state': 'qReject', 'symbol': None, 'direction': 'R'},
                        '12': {'next_state': '12', 'symbol': None, 'direction': 'R'},
                        '21': {'next_state': '21', 'symbol': None, 'direction': 'R'},
                        '$$': {'next_state': 'qAccept', 'symbol': None, 'direction': 'R'},
                    },
                    '12': {
                        '11': {'next_state': 'qReject', 'symbol': None, 'direction': 'R'},
                        '12': {'next_state': '12', 'symbol': None, 'direction': 'R'},
                        '21': {'next_state': '21', 'symbol': None, 'direction': 'R'},
                        '22': {'next_state': '2qReject1', 'symbol': None, 'direction': 'R'},
                        '$$': {'next_state': 'qAccept', 'symbol': None, 'direction': 'R'},
                    },
                    '21': {
                        '21': {'next_state': '21', 'symbol': None, 'direction': 'R'},
                        '11': {'next_state': 'qReject', 'symbol': None, 'direction': 'R'},
                        '$$': {'next_state': 'qAccept', 'symbol': None, 'direction': 'R'},
                    },
                }

CatMouseMachine = TuringMachine(tapes=['1121$', '2211$'],
                                states=['q0', '12', '21', 'qAccept', 'qReject'],
                                initial_state='q0',
                                accept_state='qAccept',
                                reject_state='qReject',
                                transitions=cat_mouse_transitions,
                                tape_alphabet={'11', '22', '12', '21', '$$'},
                                input_alphabet={'11', '22', '12', '21'})

print(CatMouseMachine.run())
