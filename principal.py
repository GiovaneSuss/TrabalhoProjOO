from user import User
from moto import Moto
from rent import Rent

user1 = User('Giovane','giovane@123','1234')
user2 = User('Glauber','Glauber@123','5678')
User.register_user(user1)
#User.register_user(user1)
User.register_user(user2)
User.lista()
#User.remove_user(user1)
User.find_user('giovane@123')
User.lista()

moto1 = Moto('Motinha','Para crianças','bem pequena',5)
moto2 = Moto('Motocross','Motocross','bem resistente',4)
Moto.register_moto(moto1)
#Moto.register_moto(moto1)
Moto.register_moto(moto2)
Moto.lista()
#Moto.remove_moto(moto1)
Moto.find_moto(moto1.id)
Moto.lista()

Rent.rent_moto(moto1,user1,'27-03-2024','31-03-2024')
Rent.rent_moto(moto2,user2,'28-03-2024','30-03-2024')
Rent.lista1()





#No código, cada classe