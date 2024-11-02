import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'RnaOAShB7kMXOOdOYPKCJNxO')  # Will be replaced with a strong, unique key
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///mydatabase.db')  # Database connection string
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disables tracking to save resources