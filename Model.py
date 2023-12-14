notes: list[dict[str, str]] = []
PATH = 'Notes.json'


def open_file():
    with open(PATH, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for note in data:
        note = note.strip().split(';')
        note = {'data': note[0], 'name': note[1], 'body': note[2]}
        notes.append(note)


def save_file():
    data =[]
    for note in notes:
        note = ';'.join([value for value in note.values()])
        data.append(note)
    with open(PATH, 'w', encoding='UTF-8') as file:
        file.write('\n'.join(data))


def get_pb() -> list[dict[str, str]]:
    return notes

def add_contact(note: dict[str, str]):
    notes.append(note)


def change(ind: int, note: dict[str, str]) -> dict[str, str]:
    cur = notes[ind]
    cur.update(note)
    result = notes.pop(ind)
    notes.insert(ind, cur)
    return result


def del_contact(index: int):
    if index == 0:
        return
    else:
        return notes.pop(index-1).get('name')
   
            
        
def find_date(message: str, pb: dict) ->list:
    filtred =[]
    for note in pb:
        if message.lower() in note.get('data').lower():
            filtred.append(note)
    return filtred 

def find_name(message: str, pb: dict) ->list:
    filtred =[]
    for contact in pb:
        if message.lower() in contact.get('name').lower():
            filtred.append(contact)
    return filtred 