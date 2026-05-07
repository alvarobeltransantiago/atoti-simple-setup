import atoti as tt

from .create_and_join_tables import create_and_join_tables
from .create_cubes import create_cubes
from .load_tables import load_tables


def main() -> None:
    session = tt.Session.start(tt.SessionConfig(port=9090))
    create_and_join_tables(session)
    create_cubes(session)
    load_tables(session)
    print(f"Session ready at {session.url}")
    session.wait()


if __name__ == "__main__":
    main()
