import GradeCalculator


# Test script for 'Final Grade Calculation' User Story


def test_1():
    # TEST 1 - Max Attributes
    # Tests the calculator when maximum skill level and awareness (confidence) has been reached
    # Expected Result: Prediction and Score will both be 100%
    # Actual Result: PASS
    GradeCalculator.run(None, 10, 1.0)


def test_2():
    # TEST 2 - Min Attributes
    # Tests the calculator when minimum skill level and awareness (confidence) has been reached
    # Expected Result: Prediction will be 5-10%, Score will be 10-15%
    # Actual Result: PASS
    GradeCalculator.run(None, 1, 0.5)


def test_3():
    # TEST 3 - High Skill Level, Low Awareness
    # Tests the calculator when maximum skill level and minimum awareness (confidence) has been reached
    # Expected Result: Prediction will be 50-55%, Score will be 100%
    # Actual Result: PASS
    GradeCalculator.run(None, 10, 0.5)


def test_4():
    # TEST 4 - Low Skill Level, High Awareness
    # Tests the calculator when maximum skill level and minimum awareness (confidence) has been reached
    # Expected Result: Prediction will be 10-15%, Score will be 10-15%
    # Actual Result: PASS
    GradeCalculator.run(None, 1, 1.0)


def test_5():
    # TEST 5 - Medium Skill Level, Medium Awareness
    # Tests the calculator when a medium skill level and awareness (confidence) has been reached
    # Expected Result: Prediction will be 45-50%, Score will be 60-65%
    # Actual Result: PASS
    GradeCalculator.run(None, 6, 0.75)
