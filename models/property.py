from beanie import Document
from pydantic import BaseModel, ConfigDict

from datetime import datetime
from typing import Optional, List

"""
id: string (UUID)
title: string
description: string
type: string (e.g., "house", "apartment")
price: number
location: string
latitude: number
longitude: number
images: array of strings (URLs)
virtualTourUrl: string
amenities: array of strings
ownerId: string (UUID)
createdAt: Date
updatedAt: Date
"""


class Property(Document):
    title: str
    description: str
    type: str
    price: float
    location: str
    latitude: float | None = None
    longitude: float | None = None
    images: List[str]
    virtualTourUrl: str
    amenities: List[str] = []
    ownerId: str
    createdAt: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    updatedAt: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    class Meta:
        collection = "properties"


class CreateProperty(BaseModel):
    title: str
    description: str
    type: str
    price: float
    location: str
    images: List[str]
    virtualTourUrl: Optional[str] = None
    amenities: Optional[List[str]] = []
    ownerId: str

    model_config = ConfigDict(
        extra="ignore",
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "title": "Beautiful house in the city",
                "description": "This is a beautiful house in the city",
                "type": "house",
                "price": 100000,
                "location": "City",
                "images": [
                    "https://example.com/image1.jpg",
                    "https://example.com/image2.jpg",
                ],
                "virtualTourUrl": "https://example.com/virtual-tour",
                "amenities": ["pool", "gym"],
                "ownerId": "123456789" 
            }
        },
    )



class UpdateProperty(BaseModel):
    title: Optional[str]
    description: Optional[str]
    type: Optional[str]
    price: Optional[float]
    location: Optional[str]
    latitude: Optional[float]
    longitude: Optional[float]
    images: Optional[List[str]]
    virtualTourUrl: Optional[str]
    amenities: Optional[List[str]]

    model_config = ConfigDict(
        extra="ignore",
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "title": "Beautiful house in the city",
                "description": "This is a beautiful house in the city",
                "type": "house",
                "price": 100000,
                "location": "City",
                "latitude": 12.345678,
                "longitude": 12.345678,
                "images": [
                    "https://example.com/image1.jpg",
                    "https://example.com/image2.jpg",
                ],
                "virtualTourUrl": "https://example.com/virtual-tour",
                "amenities": ["pool", "gym"],
            }
        },
    )