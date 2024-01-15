from collections import UserDict
from re import match
import pickle

class ExistsTag(Exception):
    pass

class Field:
    def __init__(self, value):
        self.value = value
    
    def __eq__(self, other):
        return self.value == other.value

    def __str__(self):
        return str(self.value)


class Title(Field):
    def __init__(self, value):
        self.__value = ""
        self.value = value

    @property
    def value(self):
        return self.__value
        
    @value.setter
    def value(self, new_value):
        self.__value =  new_value

    def __repr__(self):
        return self.__value

class Text(Field):
    def __init__(self, value):
        self.__value = ""
        self.value = value

    @property
    def value(self):
        return self.__value
        
    @value.setter
    def value(self, new_value):
        self.__value =  new_value
    
    def __repr__(self):
        return self.__value

class Tag(Field):
    def __init__(self, value):
        self.__value = ""
        self.value = value

    @property
    def value(self):
        return self.__value
        
    @value.setter
    def value(self, new_value):
        self.__value =  new_value

    def __repr__(self):
        return self.__value


class Record:
    def __init__(self, title, text):

        self.title = Title(title)
        self.text = Text(text)
        self.tags = []

    def add_tag(self, tag):
        tag_obj = Tag(tag)
        if tag_obj not in self.tags:
                self.tags.append(tag_obj)

    def remove_tag(self, tag):
        search_tag = Tag(tag)
        print(search_tag)
        self.tags.remove(search_tag)
    
    def find_by_tag(self, tag):
        search_tag = Tag(tag)
        for item in self.tags:
            if item == search_tag:
                return item


    def edit_text(self, new_text):
        chandge_text = Text(new_text)
        self.text = chandge_text

    def __str__(self):
    
        return f"Title: {self.title.value}, text: {self.text.value}, tags: {', '.join(t.value for t in self.tags)}"

class NoteBook(UserDict):
    qua_for_iter = 5
    list_for_iter = []

    def add_record(self, record):
        self.data[record.title.value] = record

    def find(self, title):
        record = self.data.get(title)
        if record is not None:
            return record
        else:
            raise KeyError
    
    def delete(self, title):
        self.pop(title)
    
    def find_records(self, search=None):
        list_recs = []
        for title, records in self.data.items():
            if search.lower() in title.lower():
                list_recs.append(records)
            else:
                for tags in records.tags:
                    if search in tags.value:
                        list_recs.append(records)
                        break
        return list_recs
    
    #def exists_tag(self, tag=None):
    #    if tag is not None:
    #        tag_ = Tag(tag)
    #        for record_ in self.values():
    #            if tag_ in record_.tags:
    #                raise ExistsTag
                
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
        return f"{'; '.join(i for i in for_return)} \n"

    def __iter__(self):
        return self
    
    def save_to_file_pickle(self, file_name):
        with open(file_name, 'wb') as file:
            pickle.dump(self, file)
    
    def load_from_file_pickle(self, file_name):
        with open(file_name, 'rb') as file:
            return pickle.load(file)
    
    def __str__(self):
        ret_list = ""
        for record in self:
            ret_list += str(record)
        return ret_list

            
if __name__ == "__main__":
    pass

# note = NoteBook()
# note1_record = Record("Tiiitle", "text")
# note1_record.add_tag("Tag1")
# note1_record.add_tag("Tag2")
# note.add_record(note1_record)

# note2_record = Record("Title23", "a lot of text")
# note2_record.add_tag("a")
# note2_record.add_tag("lot")
# note2_record.add_tag("of")
# note2_record.add_tag("tags")
# note.add_record(note2_record)

# note.find_records("Title23")
# # note1_record.remove_tag("tag2")
# for title, record in note.data.items():
#    print(record)