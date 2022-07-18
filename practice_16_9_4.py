# Вам необходимо написать программу, которая позволит составить список гостей.
# В класс «Клиент» добавьте метод, который будет возвращать информацию только об имени, фамилии и городе клиента.


class Client:
    def __init__(self, name, lastname, city):
        self.name = name
        self.lastname = lastname
        self.city = city

    def __str__(self):
        return f'{self.name} {self.lastname}. {self.city}'

    def get_guest(self):
        return f'{self.name} {self.lastname}, {self.city}'

client_1= Client('Иван','Петров','Москва')
client_2= Client('Владимир','Зайцев','Кострома')
client_3= Client('Олеся','Янина','Новосибирск')

# Затем создайте список, в который будут добавлены все клиенты, и выведете его в консоль.

guest_list= [client_1,client_2,client_3]

for guest in guest_list:
    print(guest.get_guest())
