class User:
    def __init__(self, user_id, full_name, card_number, pin_code, balance):
        self.user_id = user_id
        self.full_name = full_name
        self.card_number = card_number
        self.__pin_code = pin_code
        self.__balance = balance


    def __str__(self):
        return f"User(user_id={self.user_id}, full_name={self.full_name}, card_number={self.card_number}, pin_code={self.__pin_code}, balance={self.__balance})"

    def get_pincode(self):
        return self.__pin_code

    def set_pin_code(self, new_pin_code):
        self.__pin_code = new_pin_code

    def get_balance(self):
        return self.__balance

    def set_balance(self, new_balance):
        self.__balance = new_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount < self.__balance:
            self.__balance -= amount
            return True
        return False
    def __repr__(self):
        return f"User(user_id={self.user_id}, full_name='{self.full_name}', card_number='{self.card_number}', balance={self.__balance})"
