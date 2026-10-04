from sqlmodel import create_engine, Session, SQLModel

url = "sqlite:///./base_de_datos.db"

engine = create_engine(url, connect_args={"check_same_thread":False})

def get_db():
    with Session(engine) as session:
        yield session

