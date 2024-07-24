from beanie import Document , Indexed
from pydantic import BaseModel, ConfigDict
from typing import Annotated, Optional



"""
id: string (UUID)
userId: string (UUID)
propertyId: string (UUID)
createdAt: Date
"""


class Favorite(Document):
    userId: Annotated[str, Indexed()]
    propertyId: Annotated[str, Indexed()]
    createdAt: str

    class Meta:
        collection = "favorites"



class CreateFavorite(BaseModel):
    userId: str
    propertyId: str

    model_config = ConfigDict(
        extra="ignore",
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "userID": "12342523",
                "propertyId": "5eb7cf5a86d9755df3a6c593"`
            }
        }
    )


class UpdateFavorite(BaseModel):
    userId: Optional[str]
    propertyId: Optional[str]

    model_config = ConfigDict(
        extra="ignore",
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "userID": "12342523",
                "propertyId": "5eb7cf5a86d9755df3a6c593"
            }
        }
    )
        