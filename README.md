# jam-iss-tracker

This API https://jam-iss-tracker.herokuapp.com/api/v1/iss/sightings shows the International Space Station (ISS) sightings dates and times in Jamaica cities (Kingston, Montego Bay) by default.

## How to run
Enter the following command to run the project on your local machine:
```sh
$ pip install -r requirements.txt
$ uvicorn main:app --reload
```

## Query Format
To filter on other countries use the following query parameters:
* country
* region
* city_names

See the following examples:
> Example #1
>
> https://jam-iss-tracker.herokuapp.com/api/v1/iss/sightings?country=Canada&region=Ontario&city_names=Toronto

> Example #2
>
> https://jam-iss-tracker.herokuapp.com/api/v1/iss/sightings?country=Jamaica&region=None&city_names=Kingston,Montego_Bay

