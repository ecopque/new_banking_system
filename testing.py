# FILE: /testing.py

while True:
    print('Who are you?')
    name = str(input('What is your name?'))

    if name != 'Joe':
        continue

    print('Hello Joe. What is the password?')
    password = input()
    if password == 'swordfish':
        break

print('Access garanted.')