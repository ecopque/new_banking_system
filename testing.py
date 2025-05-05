# FILE: /testing.py

from abc import ABC, abstractclassmethod

class A001_TransactionCLS(ABC):
    def __init__(self, value: float):
        self.A001_value = value

    @abstractclassmethod
    def A001_registerMTD(self, account):
        pass