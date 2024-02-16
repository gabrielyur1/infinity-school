'''
Criar uma aplicação de gerenciamento de biblioteca com

Classe Livro:
    A classe Livro deve conter atributos como título, autor, ID,
    estatus de empréstimo (disponível ou emprestado).

Classe Membro:
    A classe Membro deve conter atributos como nome,
    número de membro e histórico de livros emprestados.

Classe Biblioteca:
    A classe Biblioteca deve conter um catálogo de livros
    disponíveis, um registro de membros e métodos para
    empréstimo, devolução e pesquisa de livros.
'''

from random import randint


class Biblioteca:
    def __init__(self) -> None:
        '''
        Iniciaizar a biblioteca com os atributos necessários
        catalogo e membros vazio
        '''
        self.catalogo_livros = []
        self.registro_membros = []

    def adicionarLivro(self, livro: dict) -> None:
        '''
        Adicionar um novo livro(class: Livro) ao catalogo de livros
        disponíveis da biblioteca.
        '''
        if livro:
            # Verifica se há um livro com os mesmos atributos no catálogo
            if not any(livro['titulo'] == l['titulo'] and livro['autor'] == l['autor']
                       and livro['id'] == l['id'] for l in self.catalogo_livros):
                self.catalogo_livros.append(livro)
            else:
                raise Exception('Livro já existe na biblioteca')
        else:
            raise Exception('Livro inválido')

    def emprestimoLivro(self, livro: str) -> None:
        '''
        Pegar livro disponíveis da biblioteca(catalogo_livros).
        Registrar emprestimo no histórico do usuário
        '''
        if livro:
            if any(livro == l['titulo'] and l['status'] == 'disponivel' for l in self.catalogo_livros):
                for l in self.catalogo_livros:
                    if livro == l['titulo']:
                        l['status'] = 'indisponivel'
                        user.historico.append(livro)
                        print('Emprestimo concluido!')
            else:
                raise Exception('Livro indisponivel')

    def pesquisaLivro(self):
        pass

    def devolucaoLivro(self, livro: str):
        '''
        Verificar se livro está emprestado, caso seja verdade,
        registrar a devolução do livro
        '''
        if any(livro == l['titulo'] and l['status'] == 'indisponivel' for l in self.catalogo_livros):
            for l in self.catalogo_livros:
                if livro == l['titulo']:
                    l['status'] = 'disponivel'
                    print('Livro devolvido!')
        else:
            raise Exception('Livro não encontrado ou já Devolvido!')

    def adicionarMembro(self, membro: dict) -> None:
        '''
        Adicionar um novo membro(class: Membro) ao registro de membros
        cadastrados na biblioteca
        '''
        if membro:
            # Verifica se há um membro com o mesmo ID no registro
            if not any(membro['id'] == m['id'] for m in self.registro_membros):
                self.registro_membros.append(membro)
            else:
                raise Exception('Membro já existe na biblioteca')
        else:
            raise Exception('Membro inválido')


class Livro:
    def __init__(self, titulo: str, autor: str) -> None:
        '''
        Iniciaizar um livro com os atributos necessários
        Adicionar a lista de livros da biblioteca
        '''
        self.titulo = titulo
        self.autor = autor
        self.ID = self.gerarID()

        '''Parâmetro para adicionar o livro à biblioteca'''
        self.livro = {
            'titulo': self.titulo,
            'autor': self.autor,
            'id': self.ID,
            'status': 'disponivel'
        }
        biblioteca.adicionarLivro(self.livro)

    def gerarID(self) -> str:
        valores = [str(randint(0, 9)) for i in range(8)]
        id_livro = ''.join(valores)

        return id_livro


class Membro:
    def __init__(self, nome: str) -> None:
        '''
        Iniciaizar um membro com os atributos necessários
        Adiciona a lista de membros da biblioteca
        '''
        self.nome = nome
        self.ID = self.gerarID()
        self.historico = list()

        '''Parâmetro para adicionar o membro à biblioteca'''
        self.dados = {
            'nome': self.nome,
            'id': self.ID,
            'histórico de livros': self.historico
        }
        biblioteca.adicionarMembro(self.dados)

    def definirNome(self, novo_nome: str):
        if novo_nome:
            self.nome = novo_nome

    def gerarID(self) -> str:
        valores = [str(randint(0, 9)) for i in range(4)]
        id_user = ''.join(valores)

        return id_user


# Criando as instâncias necessárias para o código funcionar
try:
    #   . Instânciando a Biblioteca para criar o sistema
    biblioteca = Biblioteca()

    #   . Usuário definido como visistante por padrão
    user = Membro('Visitante')

except Exception as e:
    print(f'ERRO: {e}')
