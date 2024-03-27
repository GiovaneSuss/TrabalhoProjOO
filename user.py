import uuid

class User:
    users = []

    def __init__(self, nome: str, email: str, senha: str, id: str = None):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.id = id

    @staticmethod
    def find_user(email):
        for user in User.users:
            if user.email == email:
                return user
        return None

    @staticmethod
    def register_user(user):
        if User.find_user(user.email):
            raise ValueError('Usuário já existe.')
        user.id = str(uuid.uuid4())
        User.users.append(user)

    @staticmethod
    def remove_user(user):
        if user in User.users:
            User.users.remove(user)
        else:
            raise ValueError('O user não foi encontrado!')
        
    def lista():
        print('Lista de usuários:')
        for user in User.users:
            print(user.nome)
