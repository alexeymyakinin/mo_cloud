from databases import Database

from server.src.config import settings
from server.src.dependencies.repository import Repository
from server.src.dependencies.repository import Repository

database = Database(settings.db_url)
