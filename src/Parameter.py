class FunctionParameter:
    def __init__(self, in_type: str, in_default, in_name) -> None:
        self.type = in_type
        self.name = in_name
        self.default_value = in_default

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, FunctionParameter):
            return False
        return self.type == o.type and self.name == o.name and self.default_value == o.default_value

    def __ne__(self, o: object) -> bool:
        return not self.__eq__(o)

    def get_str(self):
        return f"{self.type} {self.name} = {self.default_value} "

    def __repr__(self):
        return f"{self.type} {self.name} has a default value {self.default_value}"
