class Logging:
    def __init__(self, log_id, user_id, action, timestamp):
        self.log_id = log_id
        self.user_id = user_id
        self.action = action
        self.timestamp = timestamp

    def __repr__(self):
        return f"Logging(log_id={self.log_id}, user_id={self.user_id}, action='{self.action}', timestamp='{self.timestamp}')"

