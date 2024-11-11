import os

class Config:
    SQLALCHEMY_DATABASE_URI = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('DATABASE_HOST')}:{os.getenv('DATABASE_PORT')}/{os.getenv('POSTGRES_DB')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    STATIC_FOLDER = '/app/static'
    MEDIA_FOLDER = '/app/media'
