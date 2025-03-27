from typing import Iterator
from itertools import count


ticket_counter: Iterator = count(1)

while True:
    user_input = input("Press 'Enter' to receive the ticket: ")

    match user_input:
        case '':
            print(next(ticket_counter))
        case 'q':
            break
        case _:
            print("Try again")