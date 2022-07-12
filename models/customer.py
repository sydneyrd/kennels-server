from ctypes import addressof
import email


class Customer():

    def __init__(self, id, name, email, address, password):
        self.id = id
        self.name = name
        self.address = address
        self.email = email
        self.password = password