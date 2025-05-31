from typing import List
from app.models.location.country import Country
from sqlalchemy.orm import Session
from app.schemas.country_schema import CountryCreate, CountryUpdate


class CountryRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(Country).all()

    def get_by_id(self, country_id: int):
        return self.db.query(Country).filter(Country.country_id == country_id).first()

    def create(self, country_data: CountryCreate):
        country = Country(**country_data.dict())
        self.db.add(country)
        self.db.commit()
        self.db.refresh(country)
        return country

    def create_batch(self, countries_data: List[CountryCreate]):
        countries = [Country(**data.dict()) for data in countries_data]
        self.db.add_all(countries)
        self.db.commit()
        return countries

    def update(self, country_id: int, country_data: CountryUpdate):
        country = self.get_by_id(country_id)
        if not country:
            return None
        for key, value in country_data.dict(exclude_unset=True).items():
            setattr(country, key, value)
        self.db.commit()
        self.db.refresh(country)
        return country

    def delete(self, country_id: int):
        country = self.get_by_id(country_id)
        if not country:
            return None
        self.db.delete(country)
        self.db.commit()
        return country
