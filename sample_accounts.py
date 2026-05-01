from bank_account import BankAccount

# Sample bank accounts for testing
ACCOUNTS = {
    "1001": BankAccount(
        account_number="1001",
        account_holder="John Doe",
        pin="1234",
        balance=5000.00
    ),
    "1002": BankAccount(
        account_number="1002",
        account_holder="Jane Smith",
        pin="5678",
        balance=3500.00
    ),
    "1003": BankAccount(
        account_number="1003",
        account_holder="Bob Johnson",
        pin="9012",
        balance=7200.00
    ),
    "1004": BankAccount(
        account_number="1004",
        account_holder="Alice Williams",
        pin="3456",
        balance=2100.00
    ),
}
