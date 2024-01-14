from collections import UserDict
from datetime import date
from re import match
import pickle
import json


class WrongBirthday(Exception):
    pass
class ExistsPhone(Exception):
    pass
class WrongEmail(Exception):
    pass
class ExistsEmail(Exception):
    pass
class WrongNote(Exception):
    pass
class ExistsNote(Exception):
    pass
class ExistsAddress(Exception):
    pass
class WrongAddress(Exception):
    pass

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __repr__(self):
        return str(self.value)


class Phone(Field):
    def __init__(self, value):
        self.__value = ""
        self.value = value

    @property
    def value(self):
        return self.__value
        
    @value.setter
    def value(self, new_value):
        if self.is_valid_phone(new_value):
            norm_phone = self.normalis_phone(new_value)
            self.__value =  norm_phone
        else:
            raise ValueError
 
    def is_valid_phone(self, value):
        if  value!= "":
            # if match(r"^[\+]?3?8?[\s]?\(?0\d{2}?\)?[\s]?\d{3}[\s|-]?\d{2}[\s|-]?\d{2}$", value) != None:
            if match(r"^[\+]?3?8?\(?\d{3}?\)?\d{3}[\-]?\d{2}[\-]?\d{2}$", value) != None:
                return True
            else:
                return False

    def normalis_phone(self, value):
        norm_mob = value.replace("+","")\
                        .replace(" ","")\
                        .replace("(","")\
                        .replace(")","")\
                        .replace("-","")
        if len(norm_mob) == 10:
            return "+38" + norm_mob
        if len(norm_mob) == 11:
            return "+3" + norm_mob
        if len(norm_mob) == 12:
            return "+" + norm_mob
        return ""

    def __eq__(self, other):
        if isinstance(other, Phone):
            return self.value == other.value
        return NotImplemented


class Email(Field):
    def __init__(self, value):
        self.__value = ""
        self.value = value

    @property
    def value(self):
        return self.__value
        
    @value.setter
    def value(self, new_value):
        if self.is_valid_email(new_value):
            self.__value = new_value
        else:
            raise WrongEmail
 
    def is_valid_email(self, value):
        if  value!= "":
            if match(r"[a-zA-Z0-9]+[\w\-]+[\.]?[a-zA-Z\w\-]+[@]{1}[a-z]+[\.]{1}[a-z]{2,}", value) != None:
                return True
            else:
                return False

    def __eq__(self, other):
        if isinstance(other, Email):
            return self.value == other.value
        return NotImplemented   
    
    def __str__(self):
        return str(self.__value)


class Birthday(Field):
    def __init__(self, value):
        self.__value = ""
        self.value = value

    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, new_value):
        if self.is_valid_birthday(new_value):
            norm_birthday = self.normalis_birthday(new_value)
            if norm_birthday != "":
                self.__value = norm_birthday
            else:
                raise WrongBirthday
        else:
            raise WrongBirthday

    def is_valid_birthday(self, value):
        if value != "":
            if match(r"^\d{2}['\s'|\-|'.'|:]{1}\d{2}[\s|\-|'.'|:]{1}\d{4}$|^\d{4}['\s'|\-|'.'|:]{1}\d{2}[\s|\-|'.'|:]{1}\d{2}$", value) != None:
                return True
            else:
                return False
            
    def normalis_birthday(self, new_value):
        norm_birthday = new_value.replace(".",",")\
                    .replace(" ",",")\
                    .replace("-",",")\
                    .replace(":",",")
        date_birthday = norm_birthday.split(",")
        if len(date_birthday[0]) == 4:
            try:
                return date(int(date_birthday[0]), int(date_birthday[1]), int(date_birthday[2]))
            except:
                raise WrongBirthday
        else:
            try:
                return date(int(date_birthday[2]), int(date_birthday[1]), int(date_birthday[0]))
            except:
                raise WrongBirthday
        
    def __sub__(self, other):
        birthday_month = self.value.month
        birthday_day = self.value.day
        my_birthday = date(other.value.year, birthday_month, birthday_day)
        date_today = other.value
        if my_birthday < date_today:
            my_birthday = my_birthday.replace(year=date_today.year + 1)
        day_to_birthday = my_birthday - date_today
        return day_to_birthday.days
    
    def __str__(self):
        return self.value.strftime("%d.%m.%Y")
    

class Note(Field):
    def __init__(self, note_text: str):
        self.__value = ''
        self.value = note_text

    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, note_text: str):
        print(type(note_text))
        if note_text.isprintable() and len(note_text)<=240:
            self.__value = note_text
        else:
            raise WrongNote

    def __str__(self):
        return str(self.__value)


class Address(Field):
    def __init__(self, adr_text: str):
        self.__value = None
        self.value = adr_text

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, adr_text):
        if adr_text.isprintable() and len(adr_text) <= 100:
            self.__value = adr_text
        else:
            raise WrongAddress

    def __str__(self):
        return self.__value

class Record:
    def __init__(self, name, birthday = None):
        if birthday is not None:
            self.birthday = Birthday(birthday)
        self.name = Name(name)
        self.phones = []
        self.emails = None
        self.notes = None
        self.address = None

    def add_phone(self, phone):
        phone_obj = Phone(phone)
        if phone_obj not in self.phones:
            self.phones.append(phone_obj)

    def remove_phone(self, phone):
        search_phone = Phone(phone)
        self.phones.remove(search_phone)

    def edit_phone(self, phone, new_phone):
        search_phone = Phone(phone)
        chandge_phone = Phone(new_phone)
        index = self.phones.index(search_phone)
        self.phones[index] = chandge_phone
    
    def find_phone(self, phone):
        search_phone = Phone(phone)
        for item in self.phones:
            if item == search_phone:
                return item
            
    def add_email(self, email):
        if self.emails:
            raise ExistsEmail
        email_obj = Email(email)
        self.emails = email_obj

    def delete_email(self):
        self.emails = None
                    
    def days_to_birthday(self):
        today = Birthday(date.today().strftime("%Y %m %d"))
        return self.birthday - today

    def add_note(self, note_str):
        if self.notes:
            raise ExistsNote
        note = Note(note_str)
        self.notes = note

    def delete_note(self):
        self.notes = None
        
    def add_address(self, adr_text):
        if self.address:
            raise ExistsAddress
        adr = Address(adr_text)
        self.address = adr
        
    def delete_address(self):
        self.address = None

    def __str__(self):

        msg = f"Contact name: {self.name.value}, phones: {', '.join(p.value for p in self.phones)}"
    
        if hasattr(self, "birthday"):
            msg += f", birthday: {date.strftime(self.birthday.value, '%d.%m.%Y')}"

        if self.emails:
            msg += f", e-mail: {self.emails}"

        if self.notes:
            msg += f", notes: {self.notes}"
        if self.address:
            msg += f", address: {self.address}"
        return msg

class AddressBook(UserDict):
    qua_for_iter = 2
    list_for_iter = []

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        record = self.data.get(name)
        if record is not None:
            return record
        else:
            raise KeyError
    
    def delete(self, name):
        self.data.pop(name)
    
    def finde_records(self, search = None):
        list_rec = []
        for name, records in self.data.items():
            if search.lower() in name.lower():
                list_rec.append(records)
            else:
                for phones in records.phones:
                    if search in phones.value:
                        list_rec.append(records)
                        break
        return list_rec
    
    def exists_phone(self, phone = None):
        if phone is not None:
            phone_ = Phone(phone)
            for record_ in self.data.values():
                if phone_ in record_.phones:
                    raise ExistsPhone

    def __next__(self):
        if len(self.list_for_iter) == len(self.data):
            self.list_for_iter.clear()
            raise StopIteration
        iter = 0
        for_return = []
        for key, value in self.data.items():
            if key in self.list_for_iter:
                pass
            else:
                for_return.append(str(value))
                self.list_for_iter.append(key)
                iter += 1
            if len(for_return) == self.qua_for_iter:
                break
        # return for_return
        return f"{'; '.join(i for i in for_return)} \n"

    def __iter__(self):
        return self
    
    def save_to_file_pickle(self, file_name):
        with open(file_name, 'wb') as file:
            pickle.dump(self, file)
    
    def load_from_file_pickle(self, file_name):
        with open(file_name, 'rb') as file:
            return pickle.load(file)
        
    def save_to_file_json(self, file_name):
        data = {}
        dict_phones = {}
        list_phones = []
        for name_i, records_i in self.data.items():
            for i_phone in records_i.phones:
                list_phones.append(i_phone.value)
            dict_phones["phone"] = list_phones
            if hasattr(records_i, "birthday"):
                data[name_i] = [dict_phones, {"birthday": records_i.birthday.value.strftime("%Y %m %d")}]
            else:
                data[name_i] = [dict_phones]
            list_phones = []
            dict_phones = {}
        with open(file_name, 'w') as file:
            json.dump(data, file)

    def load_from_file_json(self, file_name):
        data = None
        with open(file_name, 'r') as file:
            data = json.load(file)
        ret_book = self
        for j_name, j_records in data.items():
            if len(j_records) == 2:
                record = Record(j_name, j_records[1].get("birthday"))
            else:
                record = Record(j_name)
            for j_phone in j_records[0].get("phone"):
                record.add_phone(j_phone)
            ret_book.add_record(record)
        return ret_book
    
    def __str__(self):
        ret_list = ""
        for record in self:
            ret_list += str(record)
        return ret_list

            
if __name__ == "__main__":
    pass