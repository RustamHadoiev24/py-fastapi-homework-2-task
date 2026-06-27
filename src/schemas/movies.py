from pydantic import BaseModel, ConfigDict
from datetime import date
from typing import List, Optional


class CountrySchema(BaseModel):
    id: int
    code: str
    name: Optional[str] = None
    model_config = ConfigDict(from_attributes=True)


class GenreSchema(BaseModel):
    id: int
    name: str
    model_config = ConfigDict(from_attributes=True)


class ActorSchema(BaseModel):
    id: int
    name: str
    model_config = ConfigDict(from_attributes=True)


class LanguageSchema(BaseModel):
    id: int
    name: str
    model_config = ConfigDict(from_attributes=True)


class MovieListItemSchema(BaseModel):
    id: int
    name: str
    date: date
    score: float
    overview: str
    model_config = ConfigDict(from_attributes=True)


class MovieDetailSchema(MovieListItemSchema):
    status: str
    budget: float
    revenue: float
    country: CountrySchema
    genres: List[GenreSchema]
    actors: List[ActorSchema]
    languages: List[LanguageSchema]


class MovieCreateSchema(BaseModel):
    name: str
    date: date
    score: float
    overview: str
    status: str
    budget: float
    revenue: float
    country: str
    genres: List[str]
    actors: List[str]
    languages: List[str]


class MovieUpdateSchema(BaseModel):
    name: Optional[str] = None
    date: Optional[date] = None
    score: Optional[float] = None
    overview: Optional[str] = None
    status: Optional[str] = None
    budget: Optional[float] = None
    revenue: Optional[float] = None
    country: Optional[str] = None
    genres: Optional[List[str]] = None
    actors: Optional[List[str]] = None
    languages: Optional[List[str]] = None


class MovieListResponseSchema(BaseModel):
    movies: List[MovieListItemSchema]
    total_items: int
    page: int
    per_page: int
    total_pages: int
    prev_page: Optional[str]
    next_page: Optional[str]
    model_config = ConfigDict(from_attributes=True)
