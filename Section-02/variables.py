

def who_do_you_know():
    who_they_know = input('Who do you know? ')
    people_list = [person.strip().lower() for person in who_they_know.split(',')]
    return people_list
def ask_user(known_people):
    name = input("Type a name ")
    if name.lower() in known_people:
        print(f"You know {name}")
    else:
        print(f"You don't know {name}")

known_people = who_do_you_know()
ask_user(known_people)
