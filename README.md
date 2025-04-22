# 🏧 ATM Simulator

This repository contains an ATM Simulator built using Python. The project implements a Graphical User Interface (GUI) with functionality for user authentication, balance management, money transfers, deposits, withdrawals, and more.
### Project Requirements List
- User Authentication: Secure login with card insertion and PIN entry.

- Balance Inquiry: Display the current account balance and transaction history.

- Cash Withdrawal: Allow users to withdraw cash within their available balance.

- Cash Deposit: Enable users to deposit money into their account.

- Fund Transfer: Transfer funds between accounts with validation.

- Change PIN: Allow users to change their PIN securely.

- Transaction History: View detailed transaction history.

- Multi-Language Support: Interface available in multiple languages.

- Transaction Receipt: Print receipts for transactions.

- Error Handling and Notifications: Handle errors like insufficient funds and notify users.
## 👥 Our Team

- **Abai Nurlanov**: 🎨 Design, GUI, code and documentation.
- **Baiastan Zamirbekov**: 🧠 Code, logic and documentation.
- **Imanbek Mashrapov**: 🗄️ Databases, documentation and code.

## 📂 Project Structure

### **classes**
- **dao**
  - `baseDAO.py`: Contains the base class for CRUD operations on the database.
  - `loggingDAO.py`: Manages log operations related to the ATM transactions.
  - `transactionsDAO.py`: Manages transactions (deposit, withdrawal, transfer) in the database.
  - `userDAO.py`: Handles user-related database operations (add, retrieve, update users).

- **logging.py**: Defines the `Logging` class used for storing and retrieving log entries.
- **transactions.py**: Defines the `Transaction` class for handling transaction-related data.
- **user.py**: Defines the `User` class representing the ATM user with attributes such as username, password, and balance.

### **gui** - Controllers
The `gui` directory contains all the graphical user interface (GUI) files for the ATM Simulator project, including assets and the code to manage user interaction with the application.
- **access_denied**: Contains the design and assets for the "Access Denied" screen.
- **authentication**: Contains the design for the authentication/login page.
- **change_pin**: Contains the design for the screen where users can change their PIN code.
- **deposit**: Contains the design for the deposit screen.



### **Other Files**
- **bank_database.sqlite**: SQLite database used to store user, transaction, and log data.
- **unittest.py**: Contains unit tests to ensure the proper functionality of various parts of the system.
- `main.py`: The main entry point of the program, initializing the application and displaying the GUI.
- `model.py`: Contains the business logic of the program, such as deposit, withdrawal, and account management.

- **README.md**: Documentation for the project, including an overview and file descriptions.

### **User Class**
The `User` class represents a user in the ATM Simulator system. It holds essential user information and provides methods to get and set sensitive attributes such as the PIN code and balance.

#### **Attributes:**
- `user_id`: Unique identifier for the user.
- `full_name`: Full name of the user.
- `card_number`: Card number associated with the user.
- `pin_code`: Private attribute holding the user's PIN code.
- `balance`: Private attribute representing the user's balance.

#### **Methods:**
- `get_pin_code()`: Returns the user's PIN code.
- `set_pin_code(new_pin_code)`: Sets a new PIN code for the user.
- `get_balance()`: Returns the user's current balance.
- `set_balance(new_balance)`: Sets a new balance for the user.
- `__repr__()`: Provides a string representation of the user for debugging.

### **Transaction Class**
The `Transaction` class represents a transaction made by a user in the ATM Simulator system. It holds the details of the transaction and provides methods to retrieve and modify the amount.

#### **Attributes:**
- `transaction_id`: Unique identifier for the transaction.
- `user_id`: The ID of the user who initiated the transaction.
- `transaction_type`: Type of the transaction (e.g., Deposit, Withdrawal, Transfer).
- `amount`: Private attribute representing the amount involved in the transaction.
- `timestamp`: The time when the transaction occurred.

#### **Methods:**
- `__repr__()`: Provides a string representation of the transaction for debugging.
- `get_amount()`: Returns the amount involved in the transaction.
- `set_amount(new_amount)`: Sets a new amount for the transaction.
### **Logging Class**
The `Logging` class represents a log entry in the ATM Simulator system. It captures actions performed by the users and stores related information for tracking and auditing purposes.

#### **Attributes:**
- `log_id`: Unique identifier for the log entry.
- `user_id`: The ID of the user who performed the action.
- `action`: A string describing the action performed by the user (e.g., "Deposited 100", "Withdrew 50").
- `timestamp`: The time when the action was logged.

#### **Methods:**
- `__repr__()`: Provides a string representation of the log for debugging and auditing purposes.

## DAO classes
### LoggingDAO Class
This class provides methods for interacting with the `logs` table in the database. It allows for adding logs, retrieving logs by user ID, fetching all logs, and deleting logs.

#### Attributes
- `db_file`: The path to the SQLite database file.

#### Methods
- `add_log(user_id, action)`: Adds a new log entry to the `logs` table, including the user ID, action, and timestamp.
- `get_logs_by_user_id(user_id)`: Retrieves all logs associated with a given user ID, ordered by timestamp.
- `get_all_logs()`: Retrieves all logs from the `logs` table, ordered by timestamp.
- `delete_logs_by_user_id(id)`: Deletes all logs associated with a given user ID.
- `delete_all_logs()`: Deletes all logs from the `logs` table.

### TransactionDAO Class
This class provides methods for interacting with the `transactions` table in the database. It handles operations like adding transactions, retrieving transactions by user ID, processing deposits, withdrawals, and transfers, and deleting all transactions.

#### Attributes
- `db_file`: Path to the SQLite database file.
- `UserDao`: Instance of the `UserDAO` class to interact with the users table.

#### Methods
- `add_transaction(user_id, transaction_type, amount)`: Adds a new transaction to the `transactions` table with the specified user ID, transaction type (e.g., 'Deposit', 'Withdraw', 'Transfer'), and amount.
- `get_transactions_by_user_id(user_id)`: Retrieves all transactions associated with a given user ID, ordered by timestamp.
- `get_all_transactions()`: Retrieves all transactions from the `transactions` table, ordered by timestamp.
- `deposit(card_number, amount)`: Processes a deposit for a user identified by their card number. Updates the balance and logs the transaction.
- `withdraw(card_number, amount)`: Processes a withdrawal for a user identified by their card number, ensuring sufficient funds. Updates the balance and logs the transaction.
- `transfer_funds(sender_card, receiver_card, amount)`: Transfers funds between two users, identified by their card numbers. Updates the balances and logs the transactions.
- `delete_all_transactions()`: Deletes all records in the `transactions` table.

### Model Class
The `Model` class is responsible for managing the business logic of the application, interacting with various data access objects (DAOs) to perform operations such as deposits, withdrawals, transfers, and logging. It acts as an intermediary between the user interface and the database.

#### Attributes:
- `transaction_dao`: Instance of the `TransactionDAO` class, responsible for managing transaction-related database operations.
- `user_dao`: Instance of the `UserDAO` class, responsible for managing user-related database operations.
- `logging_dao`: Instance of the `LoggingDAO` class, responsible for managing log entries in the database.

#### Methods:
- `deposit(card_number, amount)`: Processes a deposit for a user, updates the balance, logs the transaction, and returns a success message.
- `withdraw(card_number, amount)`: Processes a withdrawal for a user, ensuring sufficient funds, updates the balance, logs the transaction, and returns a success message.
- `transfer(sender_card, receiver_card, amount)`: Transfers funds between two users, updates their balances, logs the transactions, and returns a success message.
- `delete_logs_for_user(user_id)`: Deletes all logs associated with a given user ID.
- `delete_all_users()`: Deletes all users from the database.
- `delete_all_transactions()`: Deletes all transactions from the database.
- `delete_all_logs()`: Deletes all logs from the database.
- `check_pin(card_number, pin)`: Verifies if the provided pin matches the pin associated with the user identified by the given card number.
- `get_user_by_card(card_number)`: Retrieves a user by their card number.
- `add_log(user_id, action)`: Adds a log entry for a user action.
- `update_pin(user_id, new_pin)`: Updates the pin for the user with the given user ID.




## 📊 UML Diagrams

![UML Class Diagram](./images/uml_class_diagram.png)

## 📊 Database Reports

1. **Table users**
   ![](https://raw.githubusercontent.com/s-bye/ATM-Simulator/refs/heads/feature/screenshots/img.png)

2. **Displaying each users, where balance > 2000**
   ![](https://raw.githubusercontent.com/s-bye/ATM-Simulator/refs/heads/feature/screenshots/img_1.png)

3. **Displaying users ordered by balance**
   ![](https://raw.githubusercontent.com/s-bye/ATM-Simulator/refs/heads/feature/screenshots/img_2.png)

4. **Displaying logs table where from user taked money.**
   ![](https://raw.githubusercontent.com/s-bye/ATM-Simulator/refs/heads/feature/screenshots/img_4.png)

5. **User's transaction history spended**
   ![](https://raw.githubusercontent.com/s-bye/ATM-Simulator/refs/heads/feature/screenshots/img_5.png)

## ⚙️ Installation and Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/s-bye/ATM-Simulator.git
ATM Simulator

This repository contains an ATM Simulator built using Python. The project implements a Graphical User Interface (GUI) with functionality for user authentication, balance management, money transfers, deposits, withdrawals, and more.

