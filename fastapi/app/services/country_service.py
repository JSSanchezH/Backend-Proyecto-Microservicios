from sqlalchemy.orm import Session
from app.schemas.country_schema import CountryCreate, CountryUpdate, CountryBatchCreate
from app.repositories.country_repository import CountryRepository


class CountryService:
    def __init__(self, db: Session):
        self.repository = CountryRepository(db)

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, country_id: int):
        return self.repository.get_by_id(country_id)

    def create(self, country_data: CountryCreate):
        return self.repository.create(country_data)

    def create_batch(self, batch_data: CountryBatchCreate):
        return self.repository.create_batch(batch_data.countries)

    def update(self, country_id: int, country_data: CountryUpdate):
        return self.repository.update(country_id, country_data)

    def delete(self, country_id: int):
        return self.repository.delete(country_id)
