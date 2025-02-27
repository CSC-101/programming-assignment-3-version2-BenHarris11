import unittest
from hw3 import *   # Import all functions from hw3.py
from data import CountyDemographics
from build_data import get_data

# Full and reduced data sets
full_data = get_data()

reduced_data = [
    CountyDemographics(
        {'Percent 65 and Older': 13.8, 'Percent Under 18 Years': 25.2, 'Percent Under 5 Years': 6.0},
        'Autauga County',
        {"Bachelor's Degree or Higher": 20.9, 'High School or Higher': 85.6},
        {'American Indian and Alaska Native Alone': 0.5, 'Asian Alone': 1.1, 'Black Alone': 18.7,
         'Hispanic or Latino': 2.7, 'Native Hawaiian and Other Pacific Islander Alone': 0.1,
         'Two or More Races': 1.8, 'White Alone': 77.9, 'White Alone, not Hispanic or Latino': 75.6},
        {'Per Capita Income': 24571, 'Persons Below Poverty Level': 12.1, 'Median Household Income': 53682},
        {'2010 Population': 54571, '2014 Population': 55395, 'Population Percent Change': 1.5, 'Population per Square Mile': 91.8},
        'AL'),
    CountyDemographics(
        {'Percent 65 and Older': 15.3, 'Percent Under 18 Years': 25.1, 'Percent Under 5 Years': 6.0},
        'Crawford County',
        {"Bachelor's Degree or Higher": 14.3, 'High School or Higher': 82.2},
        {'American Indian and Alaska Native Alone': 2.5, 'Asian Alone': 1.6, 'Black Alone': 1.6,
         'Hispanic or Latino': 6.7, 'Native Hawaiian and Other Pacific Islander Alone': 0.1,
         'Two or More Races': 2.8, 'White Alone': 91.5, 'White Alone, not Hispanic or Latino': 85.6},
        {'Per Capita Income': 19477, 'Persons Below Poverty Level': 20.2, 'Median Household Income': 39479},
        {'2010 Population': 61948, '2014 Population': 61697, 'Population Percent Change': -0.4, 'Population per Square Mile': 104.4},
        'AR'),
    CountyDemographics(
        {'Percent 65 and Older': 17.5, 'Percent Under 18 Years': 18.1, 'Percent Under 5 Years': 4.8},
        'San Luis Obispo County',
        {"Bachelor's Degree or Higher": 31.5, 'High School or Higher': 89.6},
        {'American Indian and Alaska Native Alone': 1.4, 'Asian Alone': 3.8, 'Black Alone': 2.2,
         'Hispanic or Latino': 22.0, 'Native Hawaiian and Other Pacific Islander Alone': 0.2,
         'Two or More Races': 3.4, 'White Alone': 89.0, 'White Alone, not Hispanic or Latino': 69.5},
        {'Per Capita Income': 29954, 'Persons Below Poverty Level': 14.3, 'Median Household Income': 58697},
        {'2010 Population': 269637, '2014 Population': 279083, 'Population Percent Change': 3.5, 'Population per Square Mile': 81.7},
        'CA')
]

class TestCases(unittest.TestCase):

    def test_population_total(self):
        self.assertEqual(population_total(reduced_data),
                         sum(county.population['2014 Population'] for county in reduced_data))

    def test_filter_by_state(self):
        ca_counties = filter_by_state(reduced_data, 'CA')
        self.assertEqual(len(ca_counties), 1)
        self.assertEqual(ca_counties[0].county, 'San Luis Obispo County')

        tx_counties = filter_by_state(reduced_data, 'TX')
        self.assertEqual(len(tx_counties), 0)

    def test_population_by_education(self):
        expected = sum(
            county.population['2014 Population'] * county.education["Bachelor's Degree or Higher"] / 100
            for county in reduced_data if "Bachelor's Degree or Higher" in county.education
        )
        self.assertAlmostEqual(population_by_education(reduced_data, "Bachelor's Degree or Higher"), expected)

    def test_population_by_ethnicity(self):
        expected = sum(
            county.population['2014 Population'] * county.ethnicities['Hispanic or Latino'] / 100
            for county in reduced_data if 'Hispanic or Latino' in county.ethnicities
        )
        self.assertAlmostEqual(population_by_ethnicity(reduced_data, 'Hispanic or Latino'), expected)

    def test_population_below_poverty_level(self):
        expected = sum(
            county.population['2014 Population'] * county.income['Persons Below Poverty Level'] / 100
            for county in reduced_data
        )
        self.assertAlmostEqual(population_below_poverty_level(reduced_data), expected)

    def test_percent_by_education(self):
        total_pop = population_total(reduced_data)
        education_pop = population_by_education(reduced_data, "Bachelor's Degree or Higher")
        self.assertAlmostEqual(percent_by_education(reduced_data, "Bachelor's Degree or Higher"),
                               (education_pop / total_pop) * 100)

    def test_percent_by_ethnicity(self):
        total_pop = population_total(reduced_data)
        ethnicity_pop = population_by_ethnicity(reduced_data, 'Hispanic or Latino')
        self.assertAlmostEqual(percent_by_ethnicity(reduced_data, 'Hispanic or Latino'),
                               (ethnicity_pop / total_pop) * 100)

    def test_percent_below_poverty_level(self):
        total_pop = population_total(reduced_data)
        poverty_pop = population_below_poverty_level(reduced_data)
        self.assertAlmostEqual(percent_below_poverty_level(reduced_data),
                               (poverty_pop / total_pop) * 100)

    def test_education_greater_than(self):
        result = education_greater_than(reduced_data, "Bachelor's Degree or Higher", 25)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].county, 'San Luis Obispo County')

    def test_education_less_than(self):
        result = education_less_than(reduced_data, "Bachelor's Degree or Higher", 25)
        self.assertEqual(len(result), 2)

    def test_ethnicity_greater_than(self):
        result = ethnicity_greater_than(reduced_data, 'Hispanic or Latino', 5)
        self.assertEqual(len(result), 2)  # Fixed for current reduced_data

    def test_ethnicity_less_than(self):
        result = ethnicity_less_than(reduced_data, 'Hispanic or Latino', 5)
        self.assertEqual(len(result), 1)  # Fixed for current reduced_data
        self.assertEqual(result[0].county, 'Autauga County')

    def test_below_poverty_level_greater_than(self):
        result = below_poverty_level_greater_than(reduced_data, 15)
        self.assertEqual(len(result), 1)

    def test_below_poverty_level_less_than(self):
        result = below_poverty_level_less_than(reduced_data, 15)
        self.assertEqual(len(result), 2)


if __name__ == '__main__':
    unittest.main()
