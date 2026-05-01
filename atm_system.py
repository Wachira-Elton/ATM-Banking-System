from sample_accounts import ACCOUNTS
from bank_account import BankAccount


class ATMSystem:
    """Main ATM system interface for banking operations."""

    def __init__(self):
        """Initialize the ATM system."""
        self.current_user: BankAccount = None
        self.is_logged_in: bool = False

    def login(self) -> bool:
        """Handle user login with account number and PIN verification."""
        print("\n" + "="*50)
        print("LOGIN")
        print("="*50)
        
        account_number = input("Enter account number: ").strip()
        
        if account_number not in ACCOUNTS:
            print("❌ Account not found. Please check your account number.")
            return False
        
        account = ACCOUNTS[account_number]
        pin = input("Enter PIN: ").strip()
        
        if not account.verify_pin(pin):
            print("❌ Invalid PIN. Access denied.")
            return False
        
        self.current_user = account
        self.is_logged_in = True
        print(f"\n✅ Welcome, {account.account_holder}!")
        return True

    def logout(self) -> None:
        """Logout the current user."""
        if self.is_logged_in:
            print(f"\n👋 Thank you for using our ATM, {self.current_user.account_holder}!")
            self.current_user = None
            self.is_logged_in = False

    def check_balance(self) -> None:
        """Display the current account balance."""
        balance = self.current_user.get_balance()
        print(f"\n💰 Current Balance: ${balance:.2f}")

    def withdraw_funds(self) -> None:
        """Handle withdrawal transaction."""
        print("\n" + "-"*50)
        print("WITHDRAWAL")
        print("-"*50)
        
        try:
            amount = float(input("Enter withdrawal amount: $"))
            success, message = self.current_user.withdraw(amount)
            if success:
                print(f"✅ {message}")
                print(f"💰 New Balance: ${self.current_user.get_balance():.2f}")
            else:
                print(f"❌ {message}")
        except ValueError:
            print("❌ Invalid amount. Please enter a valid number.")

    def deposit_funds(self) -> None:
        """Handle deposit transaction."""
        print("\n" + "-"*50)
        print("DEPOSIT")
        print("-"*50)
        
        try:
            amount = float(input("Enter deposit amount: $"))
            success, message = self.current_user.deposit(amount)
            if success:
                print(f"✅ {message}")
                print(f"💰 New Balance: ${self.current_user.get_balance():.2f}")
            else:
                print(f"❌ {message}")
        except ValueError:
            print("❌ Invalid amount. Please enter a valid number.")

    def transfer_funds(self) -> None:
        """Handle fund transfer to another account."""
        print("\n" + "-"*50)
        print("TRANSFER FUNDS")
        print("-"*50)
        
        recipient_account = input("Enter recipient account number: ").strip()
        
        if recipient_account not in ACCOUNTS:
            print("❌ Recipient account not found.")
            return
        
        if recipient_account == self.current_user.account_number:
            print("❌ Cannot transfer to your own account.")
            return
        
        try:
            amount = float(input("Enter transfer amount: $"))
            recipient = ACCOUNTS[recipient_account]
            success, message = self.current_user.transfer(amount, recipient)
            if success:
                print(f"✅ {message}")
                print(f"💰 New Balance: ${self.current_user.get_balance():.2f}")
            else:
                print(f"❌ {message}")
        except ValueError:
            print("❌ Invalid amount. Please enter a valid number.")

    def change_pin(self) -> None:
        """Handle PIN change request."""
        print("\n" + "-"*50)
        print("CHANGE PIN")
        print("-"*50)
        
        old_pin = input("Enter current PIN: ").strip()
        
        if not self.current_user.verify_pin(old_pin):
            print("❌ Incorrect PIN. Operation cancelled.")
            return
        
        new_pin = input("Enter new PIN: ").strip()
        confirm_pin = input("Confirm new PIN: ").strip()
        
        if new_pin != confirm_pin:
            print("❌ PINs do not match. Operation cancelled.")
            return
        
        if self.current_user.change_pin(old_pin, new_pin):
            print("✅ PIN changed successfully!")
        else:
            print("❌ Failed to change PIN.")

    def view_transaction_history(self) -> None:
        """Display transaction history."""
        print("\n" + "="*50)
        print("TRANSACTION HISTORY")
        print("="*50)
        
        history = self.current_user.get_transaction_history()
        
        if not history:
            print("No transactions yet.")
        else:
            for entry in history:
                print(entry)

    def display_menu(self) -> None:
        """Display the main menu and handle user selection."""
        while self.is_logged_in:
            print("\n" + "="*50)
            print("MAIN MENU")
            print("="*50)
            print("1. Check Balance")
            print("2. Withdraw Funds")
            print("3. Deposit Funds")
            print("4. Transfer Funds")
            print("5. Change PIN")
            print("6. View Transaction History")
            print("7. Logout")
            print("="*50)
            
            choice = input("Select an option (1-7): ").strip()
            
            if choice == "1":
                self.check_balance()
            elif choice == "2":
                self.withdraw_funds()
            elif choice == "3":
                self.deposit_funds()
            elif choice == "4":
                self.transfer_funds()
            elif choice == "5":
                self.change_pin()
            elif choice == "6":
                self.view_transaction_history()
            elif choice == "7":
                self.logout()
                break
            else:
                print("❌ Invalid option. Please select a valid option (1-7).")

    def run(self) -> None:
        """Start the ATM system."""
        print("\n" + "#"*50)
        print("#" + " "*48 + "#")
        print("#" + "  WELCOME TO THE ATM BANKING SYSTEM".center(48) + "#")
        print("#" + " "*48 + "#")
        print("#"*50)
        
        while True:
            if not self.is_logged_in:
                print("\n1. Login")
                print("2. Exit")
                choice = input("Select an option: ").strip()
                
                if choice == "1":
                    if self.login():
                        self.display_menu()
                elif choice == "2":
                    print("\n👋 Thank you for using our ATM. Goodbye!")
                    break
                else:
                    print("❌ Invalid option.")
            else:
                self.display_menu()


if __name__ == "__main__":
    atm = ATMSystem()
    atm.run()
