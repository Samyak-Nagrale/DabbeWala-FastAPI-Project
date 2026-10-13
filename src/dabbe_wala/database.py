from sqlmodel import Session, SQLModel, create_engine

DATABASE_URL = "sqlite:///dabbewala.db"

engine = create_engine(DATABASE_URL, echo=True)


def create_tables():
    """Create all  tables definedb by SQLModel Class"""
    SQLModel.metadata.create_all(engine)


def get_session():
    """Dependency that provides a database session per request."""
    with Session(engine) as session:
        yield session
