import requests
import os
from enum import Enum
from typing import List
from dotenv import load_dotenv

load_dotenv()

maps_api_key = os.environ.get("MAPS_API_KEY")


class Fields(Enum):
    ADDRESS_COMPONENTS = "address_components"
    ADR_ADDRESS = "adr_address"
    BUSINESS_STATUS = "business_status"
    FORMATTED_ADDRESS = "formatted_address"
    GEOMETRY = "geometry"
    ICON = "icon"
    NAME = "name"
    PHOTO = "photo"
    TYPE = "type"
    CURRENT_OPENING_HOURS = "current_opening_hours"
    FORMATTED_PHONE_NUMBER = "formatted_phone_number"
    OPENING_HOURS = "opening_hours"
    WEBSITE = "website"
    DELIVERY = "delivery"
    DINE_IN = "dine_in"
    EDITORIAL_SUMMARY = "editorial_summary"
    PRICE_LEVEL = "price_level"
    RATING = "rating"
    RESERVABLE = "reservable"
    REVIEWS = "reviews"
    SERVES_BEER = "serves_beer"
    SERVES_BREAKFAST = "serves_breakfast"
    SERVES_BRUNCH = "serves_brunch"
    SERVES_DINNER = "serves_dinner"
    SERVES_LUNCH = "serves_lunch"
    SERVES_WINE = "serves_wine"
    TAKEOUT = "takeout"
    USER_RATINGS_TOTAL = "user_ratings_total"


def field_format(fields: List[Fields]):
    return "place_id," + ",".join([field.value for field in fields])


def place_search_find(place_name: str, criteria: List[Fields] = []):
    params = {
        "input": place_name,
        "inputtype": "textquery",
        "fields": field_format(criteria),
        "key": maps_api_key,
    }

    r = requests.get(
        "https://maps.googleapis.com/maps/api/place/findplacefromtext/json",
        params=params,
    )
    return r.text


def place_search_text(
    query: str,
    radius: int = 1000,
    min_price: int = 0,
    max_price: int = 4,
    open_now: bool = True,
    type: str = "",
):
    params = {
        "query": query,
        "radius": radius,
        "maxprice": max_price,
        "minprice": min_price,
        "opennow": open_now,
        "type": type,
        "key": maps_api_key,
    }
    r = requests.get(
        "https://maps.googleapis.com/maps/api/place/textsearch/json", params=params
    )
    return r.text

