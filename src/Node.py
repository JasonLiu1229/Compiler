class Node:
    def __init__(self, key : str, value) -> None:
        super().__init__()
        self.key = key
        self.value = value

    def print(self):
        print(self.get_str())

    def save(self):
        if isinstance(self.value , VarNode):
            return { self.key : self.value.save() }
        out = { self.key : self.value }
        return out
    def get_str(self):
        return self.key + '\t' + ':' + '\t' + str(self.value)

    def save_dot(self):
        out = '\"' + self.key + '\"' + '\t' + '->' + '\t'
        if isinstance(self.value , str):
            out += '\"\\' + self.value + '\"\\'
        else:
            out += str(self.value)
        return out

    def recursive_dot(self, dictionary, count, name):
        if self.key not in dictionary or count[self.key] == 1:
            dictionary[self.key] = set()
            name = self.key
        else:
            dictionary[name] = set()

        if isinstance(self.value, Node):
            dictionary[name].add(self.value.key)
            self.value.recursive_dot(dictionary, count,  self.value.key)
        else:
            dictionary[name].add(self.value)


class VarNode( Node ):

    def __init__(self, key: str, value , vtype: str , const : bool = False , ptr: bool = False , deref_level: int = 0 , total_deref: int = 0) -> None:
        super().__init__(key, value)
        self.type = vtype
        self.const = const
        self.ptr = ptr
        self.deref_level = deref_level
        self.total_deref = total_deref

    def print(self):
        return self.get_str()

    def save(self):
        out_key = ""
        if self.type != "":
            out_key += self.type
            if self.type != "":
                out_key += " "
        out_key += str('*'*self.deref_level) + self.key
        if self.const:
            out_key = "const " + out_key
        if isinstance(self.value , VarNode):
            # out_key = str('*'*(self.deref_level+1)) + out_key
            out = {out_key : self.value.save()}
        else:
            out = { out_key : self.value }
        return out

    def assign_type(self, vtype):
        self.type = vtype
        if isinstance(self.value , VarNode):
            self.value.assign_type(vtype)

    def get_str(self):
        return self.type + ' ' + self.key + '\t' + ':' + '\t' + str(self.value)

    def save_dot(self):
        out = '\"' + self.type + ' ' + self.key + '\"' + '\t' + '->' + '\t'
        if isinstance(self.value , VarNode):
            out += self.value.save_dot()
        elif isinstance(self.value , str):
            out += '\"\\' + self.value + '\"'
        else:
            out += str(self.value)
        return out

class FunctionNode(Node):

    def __init__(self, key: str, value : dict , ret_type: str = None) -> None:
        super().__init__(key, value)
        self.body = None
        self.ret_type = ret_type
    def print(self):
        print(self.get_str())

    def save(self):
        if isinstance(self.value, VarNode):
            return {self.key: self.value.save()}
        values = []
        for key,val in self.value.items():
            values.append(str(key) + "=" + str(val.value))
        out = {self.key: values}
        return out

    def save_dot(self):
        if isinstance(self.value, VarNode):
            return {self.key: self.value.save()}
        values = []
        for key,val in self.value.items():
            values.append(str(key) + "=" + str(val.value))
        out = {self.key: values}
        return out

    def get_str(self):
        out = self.key + '\t' + ':' + '\t'
        for key,val in self.value.items():
            if isinstance(val , Node):
                out += str(key) + "=" + str(val.value)
            else:
                out += str(key) + "=" + str(val)
        return out

    def get_dot(self):
        out = '\"' + self.key + '\"' + '\t' + '->' + '\t'
        for key, val in self.value.items():
            if isinstance(val, Node):
                out += str(key) + "=" + str(val.value)
            else:
                out += str(key) + "=" + str(val)
        return out

    def recursive_dot(self, dictionary, count, name):
        super().recursive_dot(dictionary, count, name)

