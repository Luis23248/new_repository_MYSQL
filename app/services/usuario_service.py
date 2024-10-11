from models.usuario import Usuario
from repositories.usuario_repository import usuarioRepository

class usuarioService:
    def __init__(self, repository: usuarioRepository):
        self.repository = repository

    def criar_usuario(self, nome: str, email: str, senha: str):
        try:
            usuario = Usuario(nome=nome, email=email, senha=senha)
            self.repository.salvar_usuario(usuario)
            print("Usuário salvo com sucesso!")
        except TypeError as error:
            print(f"Erro ao salvar o arquivo: {error}")
        except Exception as error:
            print(f"Ocorreu um erro inesperado {error}.")

    def listar_todos_usuarios(self):
        return self.repository.listar_todos_usuarios()        
