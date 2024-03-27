from typing import List
from moto import Moto
from user import User

class Rent:
    rents = []

    def __init__(self, moto, user, date_from, date_to):
        self.moto = moto
        self.user = user
        self.date_from = date_from
        self.date_to = date_to

    @staticmethod
    def create(rents: List['Rent'], bike, user, start_date, end_date):
        can_create = Rent.can_rent(rents, start_date, end_date)
        if can_create:
            return Rent(bike, user, start_date, end_date)
        raise ValueError('Overlapping dates.')

    @staticmethod
    def can_rent(rents: List['Rent'], start_date, end_date):
        for rent in rents:
            if (start_date >= rent.date_from and start_date <= rent.date_to) or \
                (end_date >= rent.date_from and end_date <= rent.date_to):
                return False
        return True

    @staticmethod
    def rent_moto(moto, user, start_date, end_date):
        moto = Moto.find_moto(moto.id)
        user = User.find_user(user.email)
        reserved_motos = [rent for rent in Rent.rents if rent.moto == moto]
        Rent.rents.append(Rent.create(reserved_motos, moto, user, start_date, end_date))

    def lista1():
        print('Lista de rents:')
        for i, rent in enumerate(Rent.rents, 1):
            print(f'Rent {i}')
            print(f'Moto: {rent.moto.nome}\nLocador: {rent.user.nome}\nData de início: {rent.date_from}\nData de devolução: {rent.date_to}')