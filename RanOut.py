#Drake Pierce-Demski
#

def calculate_interest(principal, rate, time):
    """
    Calculate simple interest.

    Parameters:
    principal (float): The principal amount (initial sum of money).
    rate (float): The rate of interest as a percentage.
    time (float): The time the money is invested or borrowed for, in years.

    Returns:
    float: The calculated simple interest.
    """
    # Calculate simple interest using the formula: (Principal Amount × Rate of Interest × Time) / 100
    interest = (principal * rate * time) / 100
    
    # Return the calculated interest
    return interest

def compound_interest(principal, rate, time, compounded_per_year):
    """
    Calculate compound interest.

    Parameters:
    principal (float): The principal amount (initial sum of money).
    rate (float): The rate of interest as a percentage.
    time (float): The time the money is invested or borrowed for, in years.
    compounded_per_year (int): The number of times the interest is compounded per year.

    Returns:
    float: The calculated compound interest.
    """
    # Calculate compound interest using the formula: P * (1 + (r / n))^(n * t)
    # Convert rate from percentage to a decimal by dividing by 100
    amount = principal * (1 + (rate / 100) / compounded_per_year) ** (compounded_per_year * time)
    
    # The interest is the total amount minus the principal
    interest = amount - principal
    
    # Return the calculated interest
    return interest

# Example usage
principal = 1000  # Initial amount of money
rate = 5  # Annual interest rate as a percentage
time = 3  # Time in years
compounded_per_year = 4  # Number of times interest is compounded per year

# Calculate simple interest
simple_interest = calculate_interest(principal, rate, time)

# Calculate compound interest
comp_interest = compound_interest(principal, rate, time, compounded_per_year)

# Print the results
print(f"Simple Interest: {simple_interest}")
print(f"Compound Interest: {comp_interest}")
