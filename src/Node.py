from math import floor
from pprint import pprint


class Node:
    def __init__(self, key: str, value, parent=None) -> None:
        """
        Initializer function
        :param key: key value of the node
        :param value: value of the node
        """
        super().__init__()
        self.key = key
        self.value = value
        self.parent = parent

    # def __eq__(self, o: object) -> bool:
    #     return (self.key == o.key) and (self.value == o.value)
    #
    # def __ne__(self, o: object) -> bool:
    #     return not self.__eq__(o)

    def __repr__(self) -> str:
        return f'{self.key} : {self.value}'

    def print(self):
        """
        print function of node
        :return: None
        """
        print(self.get_str())

    def __mul__(self, other):
        return Node("", self.value * other.value)

    def __floordiv__(self, other):
        if other.value != 0:
            return Node("int", floor(self.value / other.value))
        else:
            raise ZeroDivisionError

    def __truediv__(self, other):
        if other.value != 0:
            return Node("float", self.value / other.value)
        else:
            raise ZeroDivisionError

    def __add__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Node("", self.value + other)
        return Node("", self.value + other.value)

    def __sub__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Node("", self.value - other)
        return Node("", self.value - other.value)

    def __mod__(self, other):
        return Node("", self.value % other.value)

    def __neg__(self):
        if self.key == 'char':
            return Node("int", -ord(self.value))
        return Node("", -self.value)

    def __lt__(self, other):
        if self.key == 'char':
            return Node("int", ord(self.value) < ord(other.value))
        return Node("int", self.value < other.value)

    def __le__(self, other):
        if self.key == 'char':
            return Node("int", ord(self.value) <= ord(other.value))
        return Node("int", self.value <= other.value)

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        return self.value == other.value and self.key == other.key

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        if self.key == 'char':
            return Node("int", ord(self.value) > ord(other.value))
        return Node("int", self.value > other.value)

    def __ge__(self, other):
        if self.key == 'char':
            return Node("int", ord(self.value) >= ord(other.value))
        return Node("int", self.value >= other.value)

    def save(self):
        """
        Saves the node in a json / dictionary format
        :return: dictionary
        """
        if isinstance(self.value, VarNode):
            return {self.key: self.value.save()}
        out = {self.key: self.value}
        return out

    def get_str(self):
        """
        converts Node in a string format
        :return:
        """
        return f"{self.key}\t:\t{str(self.value)}"

    def save_dot(self):
        """
        converts Node in a dot dictionary format
        :return: dot dictionary format
        """
        out = '<\"' + self.key + '\t' + ':' + '\t'
        if isinstance(self.value, str):
            out += '\"\\' + self.value + '\"\\'
        else:
            out += str(self.value)
        out += '\">'
        return out

    def recursive_dot(self, dictionary, count, name):
        """
        recursion for the dot format
        :return: None
        """
        if self.key not in dictionary or count[self.key] == 1:
            dictionary[self.key] = set()
            name = self.key
        else:
            dictionary[name] = set()

        if isinstance(self.value, Node):
            dictionary[name].add(self.value.key)
            self.value.recursive_dot(dictionary, count, self.value.key)
        else:
            dictionary[name].add(self.value)


class VarNode(Node):

    def __init__(self, key: str, value, vtype: str, const: bool = None, ptr: bool = False, deref_level: int = 0,
                 total_deref: int = 0, const_ptr: bool = False) -> None:
        """
        Initializer function for VarNode
        """
        super().__init__(key, value)
        self.type = vtype
        self.const = const
        self.ptr = ptr
        self.deref_level = deref_level
        self.total_deref = total_deref
        self.const_ptr = const_ptr

    def __repr__(self) -> str:
        rep = f"{self.type} {'*' * self.total_deref} {self.key} : {self.value}"
        return rep

    def __eq__(self, o):
        if not isinstance(o, VarNode):
            return False
        return self.key == o.key and (self.const == o.const or (self.const is None and o.const is not None)) and self.ptr == o.ptr and self.deref_level == o.deref_level and self.total_deref == o.total_deref

    def __ne__(self, o):
        return not self.__eq__(o)

    def print(self):
        """
        print function for VarNode
        :return:
        """
        return self.get_str()

    def save(self):
        """
        Converts VarNode in a json / dictionary format
        :return: dictionary
        """
        out_key = f"{'const ' if self.const else ''}{self.type}{'*' * (self.total_deref - self.deref_level)} {self.key}"
        if isinstance(self.value, VarNode):
            # out_key = str('*'*(self.deref_level+1)) + out_key
            out = {out_key: self.value.save()}
        else:
            out = {out_key: self.value}
        return out

    def assign_type(self, vtype):
        """
        assign a type to VarNode
        :param vtype: variable type
        :return: None
        """
        self.type = vtype
        if isinstance(self.value, VarNode):
            self.value.assign_type(vtype)

    def get_str(self):
        """
        string format of VarNode
        :return: string
        """
        return f"{'const ' if self.const else ''}{self.type}{'*' * (self.total_deref - self.deref_level)} {self.key} : {self.value}"

    def save_dot(self):
        """
        dot format
        :return: string
        """
        out = '\"' + self.type + ' ' + self.key + '\"' + '\t' + '->' + '\t'
        if isinstance(self.value, VarNode):
            out += self.value.save_dot()
        elif isinstance(self.value, str):
            out += '\"\\' + self.value + '\"'
        else:
            out += str(self.value)
        return out


class FunctionNode(Node):

    def __init__(self, key: str, ret_type: str = None, in_const: bool = False) -> None:
        """
        Initializer
        """
        super().__init__(key, None)
        self.body = None
        self.type = ret_type
        self.const = in_const

    def print(self):
        """
        print function fof FunctionNode
        :return: None
        """
        print(self.get_str())

    def save(self):
        """
        convert FunctionNode in to json / dictionary
        :return: dictionary
        """
        if isinstance(self.value, VarNode):
            return {self.key: self.value.save()}
        values = []
        for key, val in self.value.items():
            values.append(str(key) + "=" + str(val.value))
        out = {self.key: values}
        return out

    def save_dot(self):
        """
        converts FunctionNode in to dot format as dictionary
        :return: dictionary
        """
        if isinstance(self.value, VarNode):
            return {self.key: self.value.save()}
        values = []
        for key, val in self.value.items():
            values.append(str(key) + "=" + str(val.value))
        out = {self.key: values}
        return out

    def get_str(self):
        """
        string version of FunctionNode
        :return: string
        """
        out = self.key + '\t' + ':' + '\t'
        for key, val in self.value.items():
            if isinstance(val, Node):
                out += str(key) + "=" + str(val.value)
            else:
                out += str(key) + "=" + str(val)
        return out

    def get_dot(self):
        """
        dot format of FunctionNode
        :return: string
        """
        out = '\"' + self.key + '\"' + '\t' + '->' + '\t'
        for key, val in self.value.items():
            if isinstance(val, Node):
                out += str(key) + "=" + str(val.value)
            else:
                out += str(key) + "=" + str(val)
        return out

    def recursive_dot(self, dictionary, count, name):
        """
        recursion function for dot format
        """
        super().recursive_dot(dictionary, count, name)
