# Необходимо создать класс «Клиент», который будет содержать данные о клиентах и их финансовых операциях.
# О клиенте известна следующая информация: имя, фамилия, город, баланс.

class Client:
    def __init__(self, name, lastname, city, balance):
        self.name = name
        self.lastname = lastname
        self.city = city
        self.balance = balance

    def get_name(self):
        return self.name

# Далее сделайте вывод о клиентах в консоль в формате:
# «Иван Петров. Москва. Баланс: 50 руб.»

    def __str__(self):
        return f'{self.name} {self.lastname}. {self.city}. Баланс: {self.balance} руб.'

clients_1= Client('Иван', 'Петров', 'Москва', 50)
print(clients_1)