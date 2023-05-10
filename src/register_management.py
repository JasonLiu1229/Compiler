class Manager:  # Manager class for register management using LRU
    """
    Manager class for register management using LRU
    Head is the least recently used register
    Tail is the most recently used register
    """

    def __init__(self, size) -> None:
        self.head = None
        self.tail = None
        self.size = size

    def add(self, register):
        """
        Adds a register to the manager
        :param register: the register to be added
        :return:
        """
        if self.head is None:
            self.head = register
            self.tail = register
        else:
            self.tail.next = register
            register.prev = self.tail
            self.tail = register

    def remove(self):
        """
        Removes the least recently used register
        :return: register
        """
        if self.head is None:
            return None
        else:
            register = self.head
            self.head = self.head.next
            self.head.prev = None
            return register


class zeroManager(Manager):

    def __init__(self) -> None:
        super().__init__(1)
        self.head = Register(in_name="zero")
        self.tail = self.head


class returnManager(Manager):

    def __init__(self) -> None:
        super().__init__(2)
        self.head = Register(in_name="v0")
        self.tail = Register(in_prev=self.head, in_name="v1")
        self.head.next = self.tail


class argumentManager(Manager):

    def __init__(self) -> None:
        super().__init__(4)
        self.head = Register(in_name="a0")
        self.tail = Register(in_prev=self.head, in_name="a1")
        self.tail = Register(in_prev=self.tail, in_name="a2")
        self.tail = Register(in_prev=self.tail, in_name="a3")
        self.head.next = self.tail


class temporaryManager(Manager):

    def __init__(self) -> None:
        super().__init__(8)
        self.head = Register(in_name="t0")
        self.tail = Register(in_prev=self.head, in_name="t1")
        self.tail = Register(in_prev=self.tail, in_name="t2")
        self.tail = Register(in_prev=self.tail, in_name="t3")
        self.tail = Register(in_prev=self.tail, in_name="t4")
        self.tail = Register(in_prev=self.tail, in_name="t5")
        self.tail = Register(in_prev=self.tail, in_name="t6")
        self.tail = Register(in_prev=self.tail, in_name="t7")
        self.head.next = self.tail


class savedManager(Manager):

    def __init__(self) -> None:
        super().__init__(8)
        self.head = Register(in_name="s0")
        self.tail = Register(in_prev=self.head, in_name="s1")
        self.tail = Register(in_prev=self.tail, in_name="s2")
        self.tail = Register(in_prev=self.tail, in_name="s3")
        self.tail = Register(in_prev=self.tail, in_name="s4")
        self.tail = Register(in_prev=self.tail, in_name="s5")
        self.tail = Register(in_prev=self.tail, in_name="s6")
        self.tail = Register(in_prev=self.tail, in_name="s7")
        self.head.next = self.tail


class globalManager(Manager):

    def __init__(self) -> None:
        super().__init__(4)
        self.head = Register(in_name="gp")
        self.tail = Register(in_prev=self.head, in_name="sp")
        self.tail = Register(in_prev=self.tail, in_name="fp")
        self.tail = Register(in_prev=self.tail, in_name="ra")
        self.head.next = self.tail


class reservedManager(Manager):

    def __init__(self) -> None:
        super().__init__(4)
        self.head = Register(in_name="k0")
        self.tail = Register(in_prev=self.head, in_name="k1")
        # self.tail = Register(in_prev=self.tail, in_name="hi")
        # self.tail = Register(in_prev=self.tail, in_name="lo")
        self.head.next = self.tail


class pointer:

    def __init__(self) -> None:
        self.gp = Register(in_name="gp")
        self.sp = Register(in_name="sp")
        self.fp = Register(in_name="fp")


class Register:

    def __init__(self, in_prev=None, in_next=None, in_object=None, in_register=None, in_name=None) -> None:
        self.name = in_name
        self.prev = in_prev
        self.next = in_next
        self.object = in_object
        self.register = in_register
