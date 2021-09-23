from fastapi import FastAPI

import scrapers.spot_the_station_scraper as spot_the_station_scraper

app = FastAPI()


@app.get("/")
async def root():
    kingston_sighting_dates = spot_the_station_scraper.get_spot_the_station_data('Kingston')
    MoBay_sighting_dates = spot_the_station_scraper.get_spot_the_station_data('Montego_Bay')
    return {"Kingston": {"sighting_dates": kingston_sighting_dates},
            "Montego_Bay": {"sighting_dates": MoBay_sighting_dates}}
