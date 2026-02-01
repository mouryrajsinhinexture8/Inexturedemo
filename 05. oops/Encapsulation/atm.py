class ATMCard:

    def __init__(self, card_number, pin, balance):
        # "Private" fields (by convention in Python)
        self._card_number = card_number
        self._pin = pin
        self._balance = balance

        self._wrong_pin_count = 0
        self._is_blocked = False

    # Private method (by convention)
    def _validate_pin(self, entered_pin):
        if self._is_blocked:
            print("Card is blocked!")
            return False

        if self._pin == entered_pin:
            self._wrong_pin_count = 0 
            return True
        else:
            self._wrong_pin_count += 1
            print("Wrong PIN entered!")

            if self._wrong_pin_count == 3:
                self._is_blocked = True
                print("Card blocked due to 3 wrong PIN attempts!")
            return False

    # Withdraw money
    def withdraw(self, amount, entered_pin):
        if not self._validate_pin(entered_pin):
            return

        if amount > self._balance:
            print("Insufficient balance!")
        else:
            self._balance -= amount
            print(f"Withdrawal successful. Balance: Rs {self._balance}")

    # Deposit money
    def deposit(self, amount):
        if self._is_blocked:
            print("Card is blocked! Cannot deposit.")
            return

        self._balance += amount
        print(f"Deposit successful. Balance: Rs {self._balance}")

    # Check balance
    def check_balance(self, entered_pin):
        if not self._validate_pin(entered_pin):
            return

        print(f"Available balance: Rs {self._balance}")


if __name__ == "__main__":

    card = ATMCard("9898-8787", 1111, 5000)

    # Wrong PIN attempts
    card.check_balance(1234)
    card.check_balance(2222)
    card.check_balance(1111) 

    # Operations after block
    card.withdraw(1000, 1111)
    card.deposit(2000)
