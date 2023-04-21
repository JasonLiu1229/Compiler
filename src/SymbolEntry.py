from Parameter import *

class SymbolEntry:
    def __init__(self, in_object: object, in_name: str, in_type: str, in_const: bool) -> None:
        self.object = in_object
        self.name = in_name
        self.type = in_type
        self.const = in_const

    def __repr__(self):
        return f"{'const ' if self.const else ''}{self.type} {self.name}"

    def __eq__(self, o: object):
        if not isinstance(o, SymbolEntry):
            return False
        return self.name == o.name and self.type == o.type and self.const == o.const

    def __ne__(self, o: object):
        return self.__eq__(o)


class FuncSymbolEntry(SymbolEntry):
    def __init__(self, in_object, in_name: str, in_type: str, in_const: bool = False,
                 in_parameters: list[FunctionParameter] = None) -> None:
        super().__init__(in_object, in_name, in_type, in_const)
        self.parameters = in_parameters

    def __repr__(self):
        return f"{'const ' if self.const else ''}{self.type} {self.name}"

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, FuncSymbolEntry):
            return False
        if super().__eq__(o):
            if len(self.parameters) != len(o.parameters):
                return False
            for i in range(len(self.parameters)):
                if self.parameters[i] != o.parameters[i]:
                    return False
            return True
        else:
            return False

    def __ne__(self, o: object) -> bool:
        return not self.__eq__(o)


class VarSymbolEntry(SymbolEntry):
    def __init__(self, in_object, in_name: str, in_type: str, in_const: bool = False, in_ptr: bool = False) -> None:
        super().__init__(in_object, in_name, in_type, in_const)
        self.is_ptr = in_ptr

    def __eq__(self, o: object):
        if not isinstance(o, VarSymbolEntry):
            return False
        return super().__eq__(o) and (self.is_ptr and o.is_ptr)

    def __ne__(self, o: object):
        return super().__ne__(o)


class PtrVarEntry(VarSymbolEntry):
    def __init__(self, in_object, in_name: str, in_type: str, in_const: bool = False, in_ptr: bool = False,
                 prev_level=None, next_level=None) -> None:
        super().__init__(in_object, in_name, in_type, in_const, in_ptr)
        self.prev_level = prev_level
        self.next_level = next_level

    def __eq__(self, o: object):
        if not isinstance(o, PtrVarEntry):
            return False
        return super().__eq__(o) and self.prev_level == o.prev_level and self.next_level == o.next_level

    def __ne__(self, o):
        return not self.__ne__(o)
