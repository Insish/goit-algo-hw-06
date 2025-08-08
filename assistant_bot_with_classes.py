from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError(f"Телефон має бути рядком із 10 цифр")
        super().__init__(value)

class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, new_phone: str):
        phone = Phone(new_phone)
        self.phones.append(phone)

    def remove_phone(self, rem_phone: str):
        for ph in self.phones:
            if ph.value == rem_phone:
                self.phones.remove(ph)
                break

    def edit_phone(self, old: str, new: str):
        for idx, ph in enumerate(self.phones):
            if ph.value == old:
                new_phone = Phone(new)
                self.phones[idx] = new_phone
                return

    def find_phone(self, phone_str: str):
        for ph in self.phones:
            if ph.value == phone_str:
                return ph
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record: Record):
        key = record.name.value
        self.data[key] = record

    def find(self, name_str: str):
        return self.data.get(name_str)

    def delete(self, name_str: str):
        self.data.pop(name_str, None)

    def __str__(self):
        if not self.data:
            return "Адресна книжка порожня"
        lines = [str(rec) for rec in self.data.values()]
        return "\n".join(lines)
    