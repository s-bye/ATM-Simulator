from classes.user import User
from classes.dao.userDAO import UserDAO
from classes.dao.transactionsDAO import TransactionDAO
from classes.dao.loggingDAO import LoggingDAO
from classes.logging import Logging
from classes.transactions import Transaction



# ✅ Подключение DAO
user_dao = UserDAO()
trans_dao = TransactionDAO()
logs_dao = LoggingDAO()

user_dao.delete_all_users()
trans_dao.delete_all_transactions()
logs_dao.delete_all_logs()

# --- 1. Добавим пользователя ---
print("🟢 1. Добавление пользователя")
new_user = User(None, "Baiastan", 1234567890123456, 1234, 1000.0)
user_dao.add_user(new_user)
print("✅ Пользователь добавлен.")
user2 = User(None, "Imanbek", 1234567890123457, 2345, 1250.0)
user3 = User(None, 'Bektur', 1234567890123458, 3456, 1500.0)
user4 = User(None, "Baisal", 1234567890123459, 4567, 1750.0)
user5 = User(None, "Nurali", 1234567890123460, 5678, 2000.0)
user6 = User(None, "Marlen", 1234567890123461, 6789, 2250.0)
user7 = User(None, "Aisulu", 1234567890123462, 7890, 2500.0)
user8 = User(None, "Alina", 1234567890123463, 8901, 2750.0)
user9 = User(None, "Diana", 1234567890123464, 9012, 3000.0)
user_dao.add_user(user2)
user_dao.add_user(user3)
user_dao.add_user(user4)
user_dao.add_user(user5)
user_dao.add_user(user6)
user_dao.add_user(user7)
user_dao.add_user(user8)
user_dao.add_user(user9)

# --- 2. Получим пользователя по номеру карты ---
print("\n🟢 2. Получение пользователя по карте")
user = user_dao.get_user_by_card(1234567890123456)
print("✅ Найден:", user.full_name, "| Баланс:", user.get_balance())

# --- 3. Проверим PIN ---
print("\n🟢 3. Проверка PIN")
pin_ok = user_dao.check_pin(1234567890123456, 1234)
print("✅ PIN правильный" if pin_ok else "❌ PIN неверный")

# --- 4. Депозит ---
print("\n🟢 4. Депозит")
result = trans_dao.deposit(1234567890123456, 500.0)
print(result)

# --- 5. Снятие ---
print("\n🟢 5. Снятие")
result = trans_dao.withdraw(1234567890123456, 200.0)
print(result)

# --- 6. Добавим второго пользователя для перевода ---
print("\n🟢 6. Добавим второго пользователя")
receiver = User(None, "Abai", 9999888877776666, 4321, 300.0)
user_dao.add_user(receiver)

# --- 7. Перевод средств ---
print("\n🟢 7. Перевод средств")
result = trans_dao.transfer_funds(1234567890123456, 9999888877776666, 150.0)
print(result)

# --- 8. Получим все транзакции ---
print("\n🟢 8. История транзакций отправителя")
transactions = trans_dao.get_transactions_by_user_id(user.user_id)
for t in transactions:
    print(f"{t.timestamp}: {t.transaction_type} {t.get_amount()}")

# --- 9. Проверим логи ---
print("\n🟢 9. Логирование входа")
logs_dao.add_log(user.user_id, "login")

print("\n🟢 10. Получение логов")
logs = logs_dao.get_logs_by_user_id(user.user_id)
for log in logs:
    print(log)

# --- 11. Проверка финального баланса ---
print("\n🟢 11. Финальный баланс")
print("Sender:", user_dao.get_user_by_card(1234567890123456).get_balance())
print("Receiver:", user_dao.get_user_by_card(9999888877776666).get_balance())

# --- 12. Очистка данных после теста ---
"""print("\n🧹 Очистка всех данных (тест)")
user_dao.delete_all_users()
trans_dao.delete_all_transactions()
logs_dao.delete_all_logs()
print("✅ Все данные удалены.")

# input("Нажми Enter, чтобы выйти...")"""
