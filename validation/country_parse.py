import pycountry


def get_alpha2(country_name) -> str:
    try:
        return pycountry.countries.get(name=country_name).alpha_2

    except:
        return None


def alpha2_to_string(alpha2) -> str:
    try:
        return pycountry.countries.get(alpha_2=alpha2).name

    except:
        return None
