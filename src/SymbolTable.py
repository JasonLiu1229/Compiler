from SymbolEntry import *


class SymbolTable:
    def __init__(self) -> None:
        self.table = []

    def lookup(self, in_name):
        """
        Search for the object in the table
        :param in_name: name of the object
        :return: SymbolEntry or None
        """
        for entry in self.table:
            if entry.name == in_name:
                return entry
        return None

    def insert(self, in_object: SymbolEntry, index: int = 0) -> None:
        """
        Insert symbol table entry with default index 0
        :param index: indicates where to insert the object
        :type in_object: SymbolEntry
        """
        self.table.insert(index, in_object)

    def remove(self, in_object: SymbolEntry):
        """
        Remove object from the table
        :param in_object: object that needs to be removed
        """
        self.table.remove(in_object)


