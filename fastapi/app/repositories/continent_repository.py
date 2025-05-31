from sqlalchemy.orm import Session
from app.models.location.continent import Continent
from app.schemas.continent_schema import ContinentCreate


class ContinentRepository:
    def __init__(self, db: Session):
        self.db = db

    def find_all(self):
        return self.db.query(Continent).all()

    def find_by_id(self, continent_id: int):
        return (
            self.db.query(Continent)
            .filter(Continent.continent_id == continent_id)
            .first()
        )

    def save(self, data: ContinentCreate):
        continent = Continent(name=data.name)
        self.db.add(continent)
        self.db.commit()
        self.db.refresh(continent)
        return continent

    def delete(self, continent_id: int):
        continent = self.find_by_id(continent_id)
        if continent:
            self.db.delete(continent)
            self.db.commit()
        return continent

    def save_batch(self, data_list: list[ContinentCreate]):
        continents = [Continent(name=data.name) for data in data_list]
        self.db.add_all(continents)
        self.db.commit()
        for c in continents:
            self.db.refresh(c)
        return continents
