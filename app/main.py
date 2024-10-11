from services.usuario_service import usuarioService
from repositories.usuario_repository import usuarioRepository
from config.connection import Session

def main():
    session = Session()
    reporitory = usuarioRepository(session)
    service = usuarioService(reporitory)

    service.criar_usuario("Pablo Vegetti", "VegettiPablo@", "333")

    print("\nListando todos os usuários.")
    usuarios = service.listar_todos_usuarios()

    for usuario in usuarios:
        print(f"{usuario.nome} - {usuario.email}")

if __name__ == "__main__":
    main()        
