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
            raise ValueError(f"Phone must be a 10-digit string")
        super().__init__(value)

class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, new_phone: str):
        if self.find_phone(new_phone):
            raise ValueError(f"Phone number {new_phone} already exists for {self.name.value}")
        phone = Phone(new_phone)
        self.phones.append(phone)

    def remove_phone(self, rem_phone: str):
        phone_obj = self.find_phone(rem_phone)
        if phone_obj:
            self.phones.remove(phone_obj)

    def edit_phone(self, old: str, new: str):
        phone_obj = self.find_phone(old)
        if not phone_obj:
            raise ValueError(f"Phone number {old} not found")
        self.remove_phone(old)
        self.add_phone(new)

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
            return "Address book is empty."
        lines = [str(rec) for rec in self.data.values()]
        return "\n".join(lines)
