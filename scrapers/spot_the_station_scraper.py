import utils


def get_spot_the_station_data(url):
    """
    get page based on the location provided.
    :param url:
    :return:
    """
    sighting_info = {}
    soup = utils.get_soup(url, 3)

    sighting_info['sighting_period'] = _extract_sighting_period(soup)
    sighting_info['sighting_dates'] = _extract_sighting_dates(soup)

    return sighting_info


def _extract_sighting_period(soup):
    sighting_info = soup.find('div', class_="table-responsive")
    sighting_period_p_tag = sighting_info.find('p')

    return sighting_period_p_tag.get_text()


def _extract_sighting_dates(soup):
    sighting_dates = []
    sightings_table = soup.find('table')

    if sightings_table:
        for row in sightings_table.find_all('tr'):
            cells = row.find_all('td')

            if len(cells) == 6:
                date = cells[0].find(text=True)
                sighting_dates.append(date)

    return sighting_dates
