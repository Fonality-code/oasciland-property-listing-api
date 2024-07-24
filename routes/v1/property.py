from fastapi import APIRouter, HTTPException

from datetime import datetime

from models.property import Property, CreateProperty, UpdateProperty
from beanie import PydanticObjectId

router = APIRouter(
    prefix="/property",
    tags=["property"],
)


@router.get("/")
async def get_properties():
    try:
        properties = await Property.find_all().to_list()
        return properties
    except Exception as e:
        return {"message": str(e)}


@router.post("/")
async def create_property(property: CreateProperty):
    try:
        new_property = Property(**property.model_dump())
        await new_property.save()
        return new_property
    except Exception as e:
        return {"message": str(e)}


@router.get("/{property_id}")
async def get_property(property_id: str):

    try:
        property_id = PydanticObjectId(property_id)
        property = await Property.get(property_id)
        return property
    except Exception as e:
        return {"message": str(e)}


@router.put("/{id}")
async def update_property(id: PydanticObjectId, property_update: UpdateProperty):
    property = await Property.get(id)
    if not property:
        raise HTTPException(status_code=404, detail="Property not found")

    update_data = property_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(property, key, value)

    property.updatedAt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    await property.save()
    return property



@router.delete("/{id}")
async def delete_property(id: PydanticObjectId):
    property = await Property.get(id)
    if not property:
        raise HTTPException(status_code=404, detail="Property not found")

    await property.delete()
    return {"message": "Property deleted successfully"}