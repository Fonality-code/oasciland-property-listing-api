from fastapi import APIRouter, HTTPException

from beanie import PydanticObjectId

from models.favorite import Favorite, CreateFavorite, UpdateFavorite



router = APIRouter(
    prefix="/favorite",
    tags=["favorite"],
)


@router.get("/")
async def get_favorites():
    try:
        favorites = await Favorite.find_all().to_list()
        return favorites
    except Exception as e:
        return {"message": str(e)}
    

@router.post("/")
async def create_favorite(favorite: CreateFavorite):
    try:
        new_favorite = Favorite(**favorite.model_dump())
        await new_favorite.save()
        return new_favorite
    except Exception as e:
        return {"message": str(e)}
    

@router.get("/{favorite_id}")
async def get_favorite(favorite_id: PydanticObjectId):
    try:    
        favorite = await Favorite.get(favorite_id)
        return favorite
    except Exception as e:
        return {"message": str(e)}
    

@router.put("/{id}")
async def update_favorite(id: PydanticObjectId, favorite_update: UpdateFavorite):
    favorite = await Favorite.get(id)
    if not favorite:
        raise HTTPException(status_code=404, detail="Favorite not found")
    
    update_data = favorite_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(favorite, key, value)
    
    await favorite.save()
    return favorite


@router.delete("/{id}")
async def delete_favorite(id: PydanticObjectId):
    favorite = await Favorite.get(id)
    if not favorite:
        raise HTTPException(status_code=404, detail="Favorite not found")
    
    await favorite.delete()
    return {"message": "Favorite deleted successfully"}