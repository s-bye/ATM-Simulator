class Transaction:
    def __init__(self, transaction_id, user_id, transaction_type, amount, timestamp):
        self.transaction_id = transaction_id
        self.user_id = user_id
        self.transaction_type = transaction_type
        self.__amount = amount
        self.timestamp = timestamp

    def __repr__(self):
        return f"Transaction(transaction_id={self.transaction_id}, user_id={self.user_id}, " \
               f"transaction_type={self.transaction_type}, amount={self.__amount}, timestamp={self.timestamp})"
