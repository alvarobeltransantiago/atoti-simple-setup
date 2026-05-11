import atoti as tt

from .create_and_join_tables import create_and_join_tables
from .create_cubes import create_cubes
from .load_tables import load_tables

def main() -> None:
    #1. Creamos la sesión (con configuración para elegir el puerto)
    session = tt.Session.start(tt.SessionConfig(port=9090))

    #2. Creamos las tablas y hacemos los joins.
    create_and_join_tables(session)

    #3. Creamos el cubo, definimos las hierarchies y las measures.
    create_cubes(session)

    #4. Cargamos los datos en las tablas.
    load_tables(session)
    
    print(f"Session ready at {session.url}")
    session.wait()

if __name__ == "__main__":
    main()
