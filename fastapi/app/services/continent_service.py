from sqlalchemy.orm import Session
from app.repositories.continent_repository import ContinentRepository
from app.schemas.continent_schema import ContinentCreate
from app.models.location.continent import Continent


class ContinentService:
    def __init__(self, db: Session):
        self.repo = ContinentRepository(db)

    def get_all(self):
        return self.repo.find_all()

    def get_by_id(self, continent_id: int):
        return self.repo.find_by_id(continent_id)

    def create(self, data: ContinentCreate):
        return self.repo.save(data)

    def delete(self, continent_id: int):
        return self.repo.delete(continent_id)

    def create_batch(self, data_list: list[ContinentCreate]):
        return self.repo.save_batch(data_list)
