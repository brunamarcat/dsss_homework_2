import unittest
from math_quiz import generate_random_integer, generate_random_operator, calculate_result


class TestMathGame(unittest.TestCase):

    def test_generate_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)
            self.assertIsInstance(rand_num,int) # Test if the random numbers generated are integers


    def test_generate_random_operator(self):
        # Test if random operator chosen is a valid operator for the quiz
        valid_operators = ["+","-","*"]
        random_operator = generate_random_operator()
        self.assertIn(random_operator, valid_operators)

    def test_calculate_result(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (1, 6, "+", "1 + 6", 7),
                (4, 2, "-", "4 - 2", 2),
                (2, 5, '-', '2 - 5', -3),
                (3, 8, "*", "3 * 8", 24),
                (-2, 7, "*", "-2 * 7", -14)
                ]
            # Test with test cases the calculations from math_quiz
            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                result = calculate_result(num1,num2,operator)
                right_result = (expected_problem,expected_answer)
                # Test if the result from the math_quiz is the same as the expected from test_cases
                self.assertEqual(result,right_result) 

if __name__ == "__main__":
    unittest.main()
