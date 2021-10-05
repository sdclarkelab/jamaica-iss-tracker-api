import os
import uvicorn
from urllib.parse import urljoin, urlencode
from fastapi import FastAPI

import scrapers.spot_the_station_scraper as spot_the_station_scraper

app = FastAPI()


@app.get("/api/v1/iss/sightings/")
async def sightings(country: str = 'Jamaica', region: str = 'None', city_names: str = 'Kingston,Montego_Bay'):

    city_sightings = list()
    city_urls = list()

    if city_names:
        city_names = city_names.strip().split(',')

        for city_name in city_names:
            query = "?" + urlencode(dict(country=country, region=region, city=city_name))
            base_url = os.getenv("SPOT_THE_STATION_URL")
            spot_the_station_url = urljoin(base_url, query)

            city_urls.append(dict(city=city_name, url=spot_the_station_url))

        for city_url in city_urls:
            sighting_detail = spot_the_station_scraper.get_spot_the_station_data(city_url['url'])

            city_sighting = dict(city_name=city_url['city'], sighting_detail=sighting_detail)
            city_sightings.append(city_sighting)

    return {
        "country_name": country,
        "cities": city_sightings,
        "reference_link": "https://spotthestation.nasa.gov/"
    }
