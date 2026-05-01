from datetime import datetime
from typing import List, Tuple


class BankAccount:
    """Represents a bank account with balance, PIN, and transaction history."""

    def __init__(self, account_number: str, account_holder: str, pin: str, balance: float = 0.0):
        """
        Initialize a bank account.

        Args:
            account_number: Unique account identifier
            account_holder: Name of account holder
            pin: Personal Identification Number
            balance: Initial account balance
        """
        self.account_number = account_number
        self.account_holder = account_holder
        self.pin = pin
        self.balance = balance
        self.transactions: List[Tuple[str, float, float, str]] = []

    def verify_pin(self, entered_pin: str) -> bool:
        """Verify if the entered PIN matches the account PIN."""
        return self.pin == entered_pin

    def change_pin(self, old_pin: str, new_pin: str) -> bool:
        """Change the account PIN after verification."""
        if self.verify_pin(old_pin):
            self.pin = new_pin
            self._add_transaction("PIN Changed", 0, self.balance)
            return True
        return False

    def get_balance(self) -> float:
        """Get the current account balance."""
        return self.balance

    def withdraw(self, amount: float) -> Tuple[bool, str]:
        """Withdraw funds from the account."""
        if amount <= 0:
            return False, "Withdrawal amount must be positive."
        if amount > self.balance:
            return False, f"Insufficient funds. Available balance: ${self.balance:.2f}"
        
        self.balance -= amount
        self._add_transaction("Withdrawal", amount, self.balance)
        return True, f"Successfully withdrew ${amount:.2f}"

    def deposit(self, amount: float) -> Tuple[bool, str]:
        """Deposit funds into the account."""
        if amount <= 0:
            return False, "Deposit amount must be positive."
        
        self.balance += amount
        self._add_transaction("Deposit", amount, self.balance)
        return True, f"Successfully deposited ${amount:.2f}"

    def transfer(self, amount: float, recipient_account: 'BankAccount') -> Tuple[bool, str]:
        """Transfer funds to another account."""
        if amount <= 0:
            return False, "Transfer amount must be positive."
        if amount > self.balance:
            return False, f"Insufficient funds. Available balance: ${self.balance:.2f}"
        
        self.balance -= amount
        recipient_account.balance += amount
        self._add_transaction(f"Transfer to {recipient_account.account_holder}", amount, self.balance)
        recipient_account._add_transaction(f"Transfer from {self.account_holder}", -amount, recipient_account.balance)
        
        return True, f"Successfully transferred ${amount:.2f} to {recipient_account.account_holder}"

    def get_transaction_history(self, limit: int = 10) -> List[str]:
        """Get the last N transactions."""
        history = []
        for i, (transaction_type, amount, new_balance, timestamp) in enumerate(self.transactions[-limit:], 1):
            history.append(f"{i}. {timestamp} - {transaction_type}: ${amount:.2f} (Balance: ${new_balance:.2f})")
        return history

    def _add_transaction(self, transaction_type: str, amount: float, new_balance: float) -> None:
        """Record a transaction in the history."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.transactions.append((transaction_type, amount, new_balance, timestamp))
