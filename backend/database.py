
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:210601@localhost/todoapp"


# Veritabanı motorunu oluşturma
engine = create_engine(DATABASE_URL)

# SQLAlchemy taban sınıfını oluşturma
Base = declarative_base()

# Veritabanı oturumunu oluşturma
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
