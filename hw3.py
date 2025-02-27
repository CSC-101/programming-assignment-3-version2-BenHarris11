from data import CountyDemographics

def population_total(counties: list[CountyDemographics]) -> int:
    """
    Calculates the total 2014 population across all provided counties.
    """
    return sum(county.population['2014 Population'] for county in counties)


def filter_by_state(counties: list[CountyDemographics], state: str) -> list[CountyDemographics]:
    """
    Returns a list of counties from the given state.
    """
    return [county for county in counties if county.state == state]


def population_by_education(counties: list[CountyDemographics], key: str) -> float:
    """
    Calculates the total 2014 sub-population for a given education level.
    """
    total = 0.0
    for county in counties:
        if key in county.education:
            percent = county.education[key] / 100
            total += county.population['2014 Population'] * percent
    return total


def population_by_ethnicity(counties: list[CountyDemographics], key: str) -> float:
    """
    Calculates the total 2014 sub-population for a given ethnicity.
    """
    total = 0.0
    for county in counties:
        if key in county.ethnicities:
            percent = county.ethnicities[key] / 100
            total += county.population['2014 Population'] * percent
    return total


def population_below_poverty_level(counties: list[CountyDemographics]) -> float:
    """
    Calculates the total 2014 population below the poverty level.
    """
    total = 0.0
    for county in counties:
        percent = county.income['Persons Below Poverty Level'] / 100
        total += county.population['2014 Population'] * percent
    return total


def percent_by_education(counties: list[CountyDemographics], key: str) -> float:
    """
    Returns the percentage of the total 2014 population for a given education level.
    """
    sub_pop = population_by_education(counties, key)
    total_pop = population_total(counties)
    return (sub_pop / total_pop) * 100 if total_pop > 0 else 0.0


def percent_by_ethnicity(counties: list[CountyDemographics], key: str) -> float:
    """
    Returns the percentage of the total 2014 population for a given ethnicity.
    """
    sub_pop = population_by_ethnicity(counties, key)
    total_pop = population_total(counties)
    return (sub_pop / total_pop) * 100 if total_pop > 0 else 0.0


def percent_below_poverty_level(counties: list[CountyDemographics]) -> float:
    """
    Returns the percentage of the total 2014 population below the poverty level.
    """
    sub_pop = population_below_poverty_level(counties)
    total_pop = population_total(counties)
    return (sub_pop / total_pop) * 100 if total_pop > 0 else 0.0


def education_greater_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    """
    Returns counties where the given education percentage is greater than the threshold.
    """
    return [county for county in counties if county.education.get(key, 0) > threshold]


def education_less_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    """
    Returns counties where the given education percentage is less than the threshold.
    """
    return [county for county in counties if county.education.get(key, 0) < threshold]


def ethnicity_greater_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    """
    Returns counties where the given ethnicity percentage is greater than the threshold.
    """
    return [county for county in counties if county.ethnicities.get(key, 0) > threshold]


def ethnicity_less_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    """
    Returns counties where the given ethnicity percentage is less than the threshold.
    """
    return [county for county in counties if county.ethnicities.get(key, 0) < threshold]


def below_poverty_level_greater_than(counties: list[CountyDemographics], threshold: float) -> list[CountyDemographics]:
    """
    Returns counties where the percentage below the poverty level is greater than the threshold.
    """
    return [county for county in counties if county.income['Persons Below Poverty Level'] > threshold]


def below_poverty_level_less_than(counties: list[CountyDemographics], threshold: float) -> list[CountyDemographics]:
    """
    Returns counties where the percentage below the poverty level is less than the threshold.
    """
    return [county for county in counties if county.income['Persons Below Poverty Level'] < threshold]
