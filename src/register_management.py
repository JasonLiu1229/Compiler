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

    def LRU(self, in_object):
        return

    def clear(self):
        return


class returnManager(Manager):

    def __init__(self) -> None:
        super().__init__(2)
        self.head = Register(in_name="v0")
        self.tail = Register(in_prev=self.head, in_name="v1")
        self.head.next = self.tail

    def LRU(self, in_object):
        # check if the registers are in use
        # if v0 not in use, replace object of register v0 with in_object
        # if v1 not in use, replace object of register v1 with in_object
        tempHead = self.head
        free = False
        while tempHead is not None:
            if tempHead.used is False:
                tempHead.update(in_object)
                free = True
                break
            tempHead = tempHead.next
        if not free:
            self.head.update(in_object)
            newHead = self.head.next
            self.tail.next = self.head
            self.head.prev = self.tail
            self.tail = self.head
            self.tail.next = None
            newHead.prev = None
            self.head = newHead

    def clear(self):
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

    def LRU(self, in_object):
        # check if the registers are in use
        # if a0 not in use, replace object of register a0 with in_object
        # if a1 not in use, replace object of register a1 with in_object
        # if a2 not in use, replace object of register a2 with in_object
        # if a3 not in use, replace object of register a3 with in_object
        tempHead = self.head
        free = False
        while tempHead is not None:
            if tempHead.used is False:
                tempHead.update(in_object)
                free = True
                break
            tempHead = tempHead.next
        if not free:
            self.head.update(in_object)
            newHead = self.head.next
            self.tail.next = self.head
            self.head.prev = self.tail
            self.tail = self.head
            self.tail.next = None
            newHead.prev = None
            self.head = newHead

    def clear(self):
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

    def LRU(self, in_object):
        # check if the registers are in use
        # if t0 not in use, replace object of register t0 with in_object
        # if t1 not in use, replace object of register t1 with in_object
        # if t2 not in use, replace object of register t2 with in_object
        # if t3 not in use, replace object of register t3 with in_object
        # if t4 not in use, replace object of register t4 with in_object
        # if t5 not in use, replace object of register t5 with in_object
        # if t6 not in use, replace object of register t6 with in_object
        # if t7 not in use, replace object of register t7 with in_object
        tempHead = self.head
        free = False
        while tempHead is not None:
            if tempHead.used is False:
                tempHead.update(in_object)
                free = True
                break
            tempHead = tempHead.next
        if not free:
            self.head.update(in_object)
            newHead = self.head.next
            self.tail.next = self.head
            self.head.prev = self.tail
            self.tail = self.head
            self.tail.next = None
            newHead.prev = None
            self.head = newHead

    def clear(self):
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

    def LRU(self, in_object):
        # check if the registers are in use
        # if s0 not in use, replace object of register s0 with in_object
        # if s1 not in use, replace object of register s1 with in_object
        # if s2 not in use, replace object of register s2 with in_object
        # if s3 not in use, replace object of register s3 with in_object
        # if s4 not in use, replace object of register s4 with in_object
        # if s5 not in use, replace object of register s5 with in_object
        # if s6 not in use, replace object of register s6 with in_object
        # if s7 not in use, replace object of register s7 with in_object
        tempHead = self.head
        free = False
        while tempHead is not None:
            if tempHead.used is False:
                tempHead.update(in_object)
                free = True
                break
            tempHead = tempHead.next
        if not free:
            self.head.update(in_object)
            newHead = self.head.next
            self.tail.next = self.head
            self.head.prev = self.tail
            self.tail = self.head
            self.tail.next = None
            newHead.prev = None
            self.head = newHead

    def clear(self):
        self.head = Register(in_name="s0")
        self.tail = Register(in_prev=self.head, in_name="s1")
        self.tail = Register(in_prev=self.tail, in_name="s2")
        self.tail = Register(in_prev=self.tail, in_name="s3")
        self.tail = Register(in_prev=self.tail, in_name="s4")
        self.tail = Register(in_prev=self.tail, in_name="s5")
        self.tail = Register(in_prev=self.tail, in_name="s6")
        self.tail = Register(in_prev=self.tail, in_name="s7")
        self.head.next = self.tail


class reservedManager(Manager):

    def __init__(self) -> None:
        super().__init__(4)
        self.head = Register(in_name="k0")
        self.tail = Register(in_prev=self.head, in_name="k1")
        self.head.next = self.tail

    def LRU(self, in_object):
        # check if the registers are in use
        # if k0 not in use, replace object of register k0 with in_object
        # if k1 not in use, replace object of register k1 with in_object
        tempHead = self.head
        free = False
        while tempHead is not None:
            if tempHead.used is False:
                tempHead.update(in_object)
                free = True
                break
            tempHead = tempHead.next
        if not free:
            self.head.update(in_object)
            newHead = self.head.next
            self.tail.next = self.head
            self.head.prev = self.tail
            self.tail = self.head
            self.tail.next = None
            newHead.prev = None
            self.head = newHead

    def clear(self):
        self.head = Register(in_name="k0")
        self.tail = Register(in_prev=self.head, in_name="k1")
        self.head.next = self.tail


class singleManager:

    def __init__(self) -> None:
        self.gp = Register(in_name="gp")
        self.sp = Register(in_name="sp")
        self.fp = Register(in_name="fp")
        self.ra = Register(in_name="ra")
        self.zero = Register(in_name="zero")
        self.at = Register(in_name="at")

    def clear(self):
        self.gp = Register(in_name="gp")
        self.sp = Register(in_name="sp")
        self.fp = Register(in_name="fp")
        self.ra = Register(in_name="ra")
        self.zero = Register(in_name="zero")
        self.at = Register(in_name="at")


class Registers:
    def __init__(self) -> None:
        self.returnManager = returnManager()
        self.argumentManager = argumentManager()
        self.temporaryManager = temporaryManager()
        self.savedManager = savedManager()
        self.reservedManager = reservedManager()
        self.singleManager = singleManager()

    def clearAll(self):
        self.returnManager.clear()
        self.argumentManager.clear()
        self.temporaryManager.clear()
        self.savedManager.clear()
        self.reservedManager.clear()
        self.singleManager.clear()


class Register:

    def __init__(self, in_prev=None, in_next=None, in_object=None, in_register=None, in_name=None) -> None:
        self.name = in_name
        self.prev = in_prev
        self.next = in_next
        self.object = in_object
        self.register = in_register
        self.used = False if self.object is None else True

    def update(self, in_object):
        self.object = in_object
        self.used = True