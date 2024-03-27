import uuid

class Moto:
    motos = []

    def __init__(self, nome: str, tipo: str, descricao: str, nota: int, disponivel: bool = True, id: str = None):
        self.nome = nome
        self.tipo = tipo
        self.descricao = descricao
        self.nota = nota
        self.id = id

    def register_moto(moto):
        if Moto.find_moto(moto.nome):
            raise ValueError('Moto já foi registrada!')
        moto.id = str(uuid.uuid4())
        Moto.motos.append(moto)

    def find_moto(id):
        return next((moto for moto in Moto.motos if moto.id == id), None)
    
    def remove_moto(moto):
        if moto in Moto.motos:
            Moto.motos.remove(moto)
        else:
            raise ValueError('A moto não foi encontrada!')
        
    def lista():
        print('Lista de motos:')
        for moto in Moto.motos:
            print(moto.nome)
        
