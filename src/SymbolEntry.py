class SymbolEntry:
    def __init__(self, in_object, in_name: str, in_type: str, in_const: bool) -> None:
        self.object = in_object
        self.name = in_name
        self.type = in_type
        self.const = in_const


class FuncSymbolEntry(SymbolEntry):
    def __init__(self, in_object, in_name: str, in_type: str, in_const: bool) -> None:
        super().__init__(in_object, in_name, in_type, in_const)


class VarSymbolEntry(SymbolEntry):
    def __init__(self, in_object, in_name: str, in_type: str, in_const: bool) -> None:
        super().__init__(in_object, in_name, in_type, in_const)


