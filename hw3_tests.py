class TestCases(unittest.TestCase):
    pass

    # Part 1
    # test population_total
    def test_population_total1(self):
        input = full_data
        result = hw3.population_total(input)
        expected = 318857056
        self.assertEqual(expected, result)

    def test_population_total2(self):
        input = reduced_data
        result = hw3.population_total(input)
        expected = 655813
        self.assertEqual(expected, result)

    # Part 2
    # test filter_by_state
    def test_filter_by_state1(self):
        input = reduced_data
        result = hw3.filter_by_state(input, 'CA')
        expected = [reduced_data[2], reduced_data[3]]
        self.assertEqual(expected, result)

    def test_filter_by_state2(self):
        input = full_data
        result = hw3.filter_by_state(input, 'CA')
        result2 = len(result)
        expected = 58
        self.assertEqual(expected, result2)

    # Part 3
    # test population_by_education
    def test_population_by_education1(self):
        input = [reduced_data[2]]
        result = hw3.population_by_education(input, "Bachelor's Degree or Higher")
        expected = 87911.145
        self.assertEqual(expected, result)

    def test_population_by_education2(self):
        input = [reduced_data[0], reduced_data[1]]
        result = hw3.population_by_education(input, "Bachelor's Degree or Higher")
        expected = 20400.226
        end = math.isclose(result,expected)
        self.assertEqual(True,end)

    # test population_by_ethnicity
    def test_population_by_ethnicity1(self):
        input = [reduced_data[0], reduced_data[1]]
        result = hw3.population_by_ethnicity(input, 'Two or More Races')
        expected = 2724.626
        end = math.isclose(result, expected)
        self.assertEqual(True, end)

    def test_population_by_ethnicity2(self):
        input = [reduced_data[0], reduced_data[1]]
        result = hw3.population_by_ethnicity(input, 'Hispanic or Latino')
        expected = 5629.364
        end = math.isclose(result, expected)
        self.assertEqual(True, end)

    # test population_below_poverty_level
    def test_population_below_poverty_level1(self):
        input = [reduced_data[0], reduced_data[1]]
        result = hw3.population_below_poverty_level(input)
        expected = 19165.589
        end = math.isclose(expected,result)
        self.assertEqual(True,end)

    def test_population_below_poverty_level2(self):
        input = []
        result = hw3.population_below_poverty_level(input)
        expected = 0
        end = math.isclose(expected,result)
        self.assertEqual(True,end)

    # Part 4
    # test percent_by_education
    def test_percent_by_education1(self):
        input = [reduced_data[0], reduced_data[1]]
        result = hw3.percent_by_education(input, "Bachelor's Degree or Higher")
        expected = 17.4224
        end = math.isclose(expected, result, abs_tol= 0.0001, rel_tol= 0.0001)
        self.assertEqual(end, True)

    def test_percent_by_education2(self):
        input = [reduced_data[0], reduced_data[1]]
        result = hw3.percent_by_education(input, 'High School or Higher')
        expected = 83.8085
        end = math.isclose(expected, result, abs_tol= 0.0001, rel_tol= 0.0001)
        self.assertEqual(end, True)

    # test percent_by_ethnicity
    def test_percent_by_ethnicity1(self):
        input = [reduced_data[0], reduced_data[1]]
        result = hw3.percent_by_ethnicity(input, 'Two or More Races')
        expected = 2.32691
        end = math.isclose(expected, result, abs_tol= 0.00001, rel_tol= 0.00001)
        self.assertEqual(end,True)

    def test_percent_by_ethnicity2(self):
        input = [reduced_data[0], reduced_data[1]]
        result = hw3.percent_by_ethnicity(input, 'Hispanic or Latino')
        expected = 4.80764
        end = math.isclose(expected, result, abs_tol= 0.00001, rel_tol= 0.00001)
        self.assertEqual(end,True)

    # test percent_below_poverty_level
    def test_percent_below_poverty_level1(self):
        input = [reduced_data[0], reduced_data[1]]
        result = hw3.percent_below_poverty_level(input)
        expected = 16.368
        end = math.isclose(expected, result, abs_tol= 0.00001, rel_tol= 0.00001)

    def test_percent_below_poverty_level2(self):
        input = []
        result = hw3.percent_below_poverty_level(input)
        expected = 0
        end = math.isclose(expected, result, abs_tol= 0.00001, rel_tol= 0.00001)

    # Part 5
    # test education_greater_than
    def test_education_greater_than1(self):
        input = [reduced_data[0], reduced_data[1]]
        result = hw3.education_greater_than(input, "Bachelor's Degree or Higher", 60.0)
        expected = []
        self.assertEqual(expected, result)

    def test_education_greater_than2(self):
        input = [reduced_data[0], reduced_data[1]]
        result = hw3.education_greater_than(input, 'High School or Higher', 60.0)
        expected = [reduced_data[0], reduced_data[1]]
        self.assertEqual(expected, result)

    # test education_less_than
    def test_education_less_than1(self):
        input = [reduced_data[0], reduced_data[1]]
        result = hw3.education_less_than(input, "Bachelor's Degree or Higher", 60.0)
        expected = [reduced_data[0], reduced_data[1]]
        self.assertEqual(expected, result)

    def test_education_less_than2(self):
        input = [reduced_data[0], reduced_data[1]]
        result = hw3.education_less_than(input, 'High School or Higher', 60.0)
        expected = []
        self.assertEqual(expected, result)

    # test ethnicity_greater_than
    def test_ethnicity_greater_than1(self):
        input = reduced_data
        result = hw3.ethnicities_greater_than(input, 'Hispanic or Latino', 10.0)
        expected = [reduced_data[2], reduced_data[3]]
        self.assertEqual(expected, result)

    def test_ethnicity_greater_than2(self):
        input = reduced_data
        result = hw3.ethnicities_greater_than(input, 'Two or More Races', 2.0)
        expected = [reduced_data[1], reduced_data[2], reduced_data[3], reduced_data[4], reduced_data[6]]
        self.assertEqual(expected, result)

    # test ethnicity_less_than
    def test_ethnicity_less_than1(self):
        input = reduced_data
        result = hw3.ethnicities_less_than(input, 'Hispanic or Latino', 10.0)
        expected = [reduced_data[0], reduced_data[1], reduced_data[4], reduced_data[5], reduced_data[6]]
        self.assertEqual(expected, result)

    def test_ethnicity_less_than2(self):
        input = reduced_data
        result = hw3.ethnicities_less_than(input, 'Two or More Races', 2.0)
        expected = [reduced_data[0], reduced_data[5]]
        self.assertEqual(expected, result)

    # test below_poverty_level_greater_than
    def test_below_poverty_level_greater_than1(self):
        input = reduced_data
        result = hw3.below_poverty_level_greater_than(input, 15.0)
        expected = [reduced_data[1], reduced_data[3], reduced_data[4], reduced_data[5]]
        self.assertEqual(expected, result)

    def test_below_poverty_level_greater_than2(self):
        input = []
        result = hw3.below_poverty_level_greater_than(input, 15.0)
        expected = []
        self.assertEqual(expected, result)

    # test below_poverty_level_less_than
    def test_below_poverty_level_less_than1(self):
        input = reduced_data
        result = hw3.below_poverty_level_less_than(input, 15.0)
        expected = [reduced_data[0], reduced_data[2], reduced_data[6]]
        self.assertEqual(expected, result)

    def test_below_poverty_level_less_than2(self):
        input = [reduced_data[0], reduced_data[1]]
        result = hw3.below_poverty_level_less_than(input, 15.0)
        expected = [reduced_data[0]]
        self.assertEqual(expected, result)



if __name__ == '__main__':
    unittest.main()
