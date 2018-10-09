from enigma.machine import EnigmaMachine

# setup machine according to specs from a daily key sheet:

machine = EnigmaMachine.from_key_sheet(
       rotors='VIII VI VIII',
       reflector='C',
       ring_settings=[0,0,0],
       plugboard_settings='')

# set machine initial starting position
machine.set_display('LZA')

# decrypt the message key
msg_key = machine.process_text('AAAAA')
print(msg_key)
# decrypt the cipher text with the unencrypted message key
# machine.set_display(msg_key)
#
# ciphertext = 'ERMJLADMAEOILPIDHPCNYJGJC'
# plaintext = machine.process_text(ciphertext)
#
# print(plaintext)