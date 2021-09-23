import utils


def get_spot_the_station_data(location):
    """
    get page based on the location provided.
    :param location:
    :return:
    """
    url = f'https://spotthestation.nasa.gov/sightings/view.cfm?country=Jamaica&region=None&city={location}'
    soup = utils.get_soup(url, 3)
    return _extract_sighting_dates(soup)


def _extract_sighting_dates(soup):
    sighting_dates = []
    sightings_table = soup.find('table')

    for row in sightings_table.find_all('tr'):
        cells = row.find_all('td')

        if len(cells) == 6:
            date = cells[0].find(text=True)
            sighting_dates.append(date)

    return sighting_dates
