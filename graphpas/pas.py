import subprocess
import tkinter as tk
from tkinter import messagebox

# Функция для изменения пароля
def change_password():
    username = username_entry.get().strip()
    new_password = password_entry.get().strip()

    if not username or not new_password:
        messagebox.showerror("Ошибка", "Пожалуйста, заполните все поля!")
        return

    if " " in username or " " in new_password:
        messagebox.showerror("Ошибка", "Имя пользователя и пароль не должны содержать пробелов!")
        return

    try:
        # Используем subprocess для выполнения команды
        command = ["net", "user", username, new_password]
        result = subprocess.run(command, capture_output=True, text=True, shell=True)

        # Отладочный вывод
        print(f"Команда: {command}")
        print(f"Код возврата: {result.returncode}")
        print(f"Вывод: {result.stdout}")
        print(f"Ошибка: {result.stderr}")

        if result.returncode == 0:
            messagebox.showinfo("Успех", f"Пароль для {username} успешно изменен!")
        else:
            messagebox.showerror("Ошибка", f"Не удалось изменить пароль: {result.stderr}")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")

# Создание окна Tkinter
app = tk.Tk()
app.title("Изменение пароля администратора")
app.geometry("400x200")

# Метки и поля ввода
tk.Label(app, text="Имя пользователя:").pack(pady=5)
username_entry = tk.Entry(app)
username_entry.pack(pady=5)

tk.Label(app, text="Новый пароль:").pack(pady=5)
password_entry = tk.Entry(app, show="*")
password_entry.pack(pady=5)

# Кнопка для изменения пароля
change_btn = tk.Button(app, text="Изменить пароль", command=change_password)
change_btn.pack(pady=20)

# Запуск приложения
app.mainloop()
