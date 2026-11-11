from fastapi import FastAPI
from sqlalchemy import create_engine

# PostgreSQL database connection
DATABASE_URL = "postgresql://postgres:YOUR_PASSWORD@localhost:5432/YOUR_DATABASE"

# Create database engine
engine = create_engine(DATABASE_URL)

app = FastAPI()