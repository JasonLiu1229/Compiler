import copy

from SymbolEntry import *
from Node import VarNode, FunctionNode


class SymbolTable:
    def __init__(self, in_owner= None) -> None:
        self.table: list[SymbolEntry] = []
        self.parent: SymbolTable | None = None
        self.owner = in_owner

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

    def insert(self, in_object: SymbolEntry, index: int = 0):
        """
        Insert symbol table entry with default index 0
        :param index: indicates where to insert the object
        :type in_object: SymbolEntry
        """
        self.table.insert(index, copy.deepcopy(in_object))
        return self.table[index]

    def update(self, in_object: VarNode | FunctionNode) -> bool:
        if not (isinstance(in_object, VarNode) or isinstance(in_object, FunctionNode)):
            return False
        for entry in self.table:
            # check dereference level
            current_object = entry.object
            entry_stack = []
            # if current_object.ptr:
            #     while current_object.ptr and current_object.value is not None:
            #         entry_stack.append(current_object)
            #         current_object = current_object.value
            #         if current_object == in_object:
            #             current_object.value = in_object.value
            #             while len(entry_stack) > 0:
            #                 current_parent = entry_stack.pop()
            #                 current_parent.value = current_object
            #                 current_object = current_parent
            #             return True
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

    def print(self, print_each: bool = False) -> None:
        if len(self.table) == 0:
            print(f"Symbol Table for {self.owner.root.key} is empty")
            return
        print(f"Symbol Table for {self.owner.root.key}:\n")
        # get larges entry
        max_width = 10
        for entry in self.table:
            if isinstance(entry, FuncSymbolEntry):
                new_length = 0
                for element in entry.parameters:
                    new_length += len(element.get_str()) + 2
                if new_length > max_width:
                    max_width = new_length
            if entry.array:
                new_length = 0
                for value in entry.object.values:
                    new_length += len(value.get_str()) + 2
                    if new_length > max_width:
                        max_width = new_length

        max_width += 1
        print(f"{'|':<2}{'Name':<15}{'|':<2}{'Value':<{max_width}}{'|':<2}")
        under = ""
        for i in range(21 + max_width):
            under += '-'
        print(under)
        for item in self.table:
            Object = item.object
            name = item.name
            value = Object.value
            if value is None and not item.array:
                value = 'None'
            elif item.array:
                value = f"{Object.values}"
            elif isinstance(Object, VarNode) and Object.ptr:
                while isinstance(value, VarNode):
                    value = value.value
            if isinstance(item, FuncSymbolEntry):
                value = item.get_str()
                print(f"{'|':<2}{name:<15}{'|':<2}{value:<{max_width}}{'|':<2}")
            else:
                print(f"{'|':<2}{name:<15}{'|':<2}{value:<{max_width}}{'|':<2}")
        print(under)

        # if print_each, print for each entry it's symbol table
        if print_each:
            for entry in self.table:
                if entry.symbol_table is not None:
                    entry.symbol_table.print(print_each)