from decimal import Decimal

class Account:
	def __init__(self, initial: Decimal):
		if (initial < Decimal("0")):
			raise ValueError("initial must be non-negative")
		self._balance = Decimal(str(initial))
	
	def balance(self) -> Decimal:
		return self._balance
	
	def deposit(self, amount: Decimal):
		if (amount <= Decimal("0")):
			raise ValueError("amount must be positive")
		self._balance += amount
	
	def withdraw(self, amount: Decimal):
		if (amount <= Decimal("0")):
			raise ValueError("amount must be positive")
		if (amount > self._balance):
			raise ValueError("insufficient funds")
		self._balance -= amount
