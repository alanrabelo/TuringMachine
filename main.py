from TuringMachine import TuringMachine


transitions = {'q0': {
                        'a': {'next_state': 'q1', 'symbol': 'X', 'direction': 'R'},
                        'Y': {'next_state': 'q3', 'symbol': 'Y', 'direction': 'R'}
                     },
               'q1': {
                        'a': {'next_state': 'q1', 'symbol': 'a', 'direction': 'R'},
                        'Y': {'next_state': 'q1', 'symbol': 'Y', 'direction': 'R'},
                        'b': {'next_state': 'q2', 'symbol': 'Y', 'direction': 'L'}
                     },
               'q2': {
                        'a': {'next_state': 'q2', 'symbol': 'a', 'direction': 'L'},
                        'Y': {'next_state': 'q2', 'symbol': 'Y', 'direction': 'L'},
                        'X': {'next_state': 'q0', 'symbol': 'X', 'direction': 'R'}
                     },
               'q3': {
                        '$': {'next_state': 'q4', 'symbol': '$', 'direction': 'L'},
                        'Y': {'next_state': 'q3', 'symbol': 'Y', 'direction': 'R'}
                     },
               }

M1 = TuringMachine(tape='aaaaabbbbb$',
                   states=['q0', 'q1', 'q2', 'q3', 'q4'],
                   initial_state='q0',
                   accept_state='q4',
                   reject_state='q5',
                   transitions=transitions,
                   tape_alphabet={'a', 'b', 'X', 'Y', '$'},
                   input_alphabet={'a', 'b'})

print(M1.run())
