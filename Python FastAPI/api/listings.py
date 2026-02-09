from fastapi import APIRouter, HTTPException '''аналог Blueprint у Flask'''
from typing import List

from models import (
    get_all_listings,
    get_listing,
    add_listing,
    update_listing,
    delete_listing,
)

from schemas import Listing, ListingCreate, ListingUpdate

router = APIRouter(prefix="/api/listings", tags=["Listings"])


@router.get("/", response_model=List[Listing])
def api_get_listings():
    return get_all_listings()


@router.get("/{listing_id}", response_model=Listing)
def api_get_listing(listing_id: int):
    listing = get_listing(listing_id)
    if not listing:
        raise HTTPException(status_code=404, detail="Listing not found")
    return listing


@router.post("/", status_code=201)
def api_add_listing(data: ListingCreate):
    listing_id = add_listing(
        data.title,
        data.description,
        data.price
    )
    return {"message": "Listing created", "id": listing_id}


@router.put("/{listing_id}")
def api_update_listing(listing_id: int, data: ListingUpdate):
    update_listing(
        listing_id,
        data.title,
        data.description,
        data.price
    )
    return {"message": "Listing updated"}


@router.delete("/{listing_id}")
def api_delete_listing(listing_id: int):
    delete_listing(listing_id)
    return {"message": "Listing deleted"}
