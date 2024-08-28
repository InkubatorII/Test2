def admin_only(func):
    def wrapper(*args, **kwargs):
        user_role = kwargs.get('role', 'user')
        if user_role == 'admin':
            return func(*args, **kwargs)
        else:
            print("Доступ запрещен. Только администраторы могут выполнять эту операцию.")
    return wrapper

@admin_only
def delete_user(username, role='user'):
    print(f"Пользователь {username} был удален из системы.")

# Пример вызова функции с правами администратора
delete_user("Abraham", role='admin')

# Пример вызова функции без прав администратора
delete_user("Abraham")
