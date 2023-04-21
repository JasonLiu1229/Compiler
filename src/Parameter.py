class FunctionParameter:
    def __init__(self, in_type: str, in_default, in_name):
        self.type = in_type
        self.name = in_name
        self.default_value = in_default

    def __eq__(self, o: object):
        if not isinstance(o, FunctionParameter):
            return False
        return self.type == o.type and self.name == o.name and self.default_value == o.default_value

    def __ne__(self, o: object):
        return not self.__eq__(o)