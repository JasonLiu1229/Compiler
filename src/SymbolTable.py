import copy

from SymbolEntry import *
from Node import VarNode, FunctionNode
class SymbolTable:
    def __init__(self) -> None:
        self.table: list[SymbolEntry] = []

    def __repr__(self):
        out = f""
        for entry in self.table:
            out += f"| {entry.__repr__()} "
        return out + "|"

    def lookup(self, in_object: object | str):
        """
        Search for the object in the table
        :param in_object: the object
        :return: SymbolEntry or raise error
        """
        matching = []
        if isinstance(in_object, object):
            for entry in self.table:
                if entry.object == in_object:
                    matching.append(entry)
        if isinstance(in_object, str):
            for entry in self.table:
                if entry.name == in_object:
                    matching.append(entry)
        return matching

    def exists(self, in_object: object | str) -> bool:
        if len(self.lookup(in_object)) == 0:
            return False
        return True
    def insert(self, in_object: SymbolEntry, index: int = 0) -> None:
        """
        Insert symbol table entry with default index 0
        :param index: indicates where to insert the object
        :type in_object: SymbolEntry
        """
        self.table.insert(index, copy.deepcopy(in_object))

    def update(self, in_object: VarNode | FunctionNode) -> bool:
        if not (isinstance(in_object, VarNode) or isinstance(in_object, FunctionNode)):
            return False
        for entry in self.table:
            if entry.object == in_object:
                entry.object = copy.deepcopy(in_object)
                return True

    def refresh(self):
        for entry in self.table:
            if entry.object is not None:
                entry.name = entry.object.key
                entry.type = entry.object.type
                entry.const = entry.object.const

    def remove(self, in_object: SymbolEntry) -> None:
        """
        Remove an object from the table
        :param in_object: object that needs to be removed
        """
        self.table.remove(in_object)

    def print(self):


        # get larges entry
        max_width = 10
        for entry in self.table:
            if isinstance(entry, FuncSymbolEntry):
                new_length = 0
                for element in entry.parameters:
                    new_length += len(element.get_str())
                if new_length > max_width:
                    max_width = new_length
        max_width += 1
        print(f"{'|':<2}{'Name':<15}{'|':<2}{'Value':<{max_width}}{'|':<2}")
        under = ""
        for i in range(21+max_width):
            under += '-'
        print(under)
        for item in self.table:
            Object = item.object
            name = item.name
            value = Object.value
            if value is None:
                value = 'None'
            if isinstance(item, FuncSymbolEntry):
                value = item.get_str()
                print(f"{'|':<2}{name:<15}{'|':<2}{value:<{max_width}}{'|':<2}")
            else:
                print(f"{'|':<2}{name:<15}{'|':<2}{value:<{max_width}}{'|':<2}")

