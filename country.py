import pycountry


def get_country(country: str = "United States of America"):
    try:
        country_search = pycountry.countries.search_fuzzy(country)
        if len(country_search) != 1:
            raise ValueError(
                f"Multiple matches found: {[c.name for c in country_search]}"
            )
        validated_country = pycountry.countries.get(
            official_name=country
        ) or pycountry.countries.get(name=country)
        if validated_country is None:
            raise ValueError(
                f"Country '{country}' could not be validated using name or official_name."
            )
        return validated_country.name
    except LookupError:
        error_message = "No country found"
        raise LookupError(error_message)
