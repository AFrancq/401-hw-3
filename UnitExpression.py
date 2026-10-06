"""
Group Members:
  Catherine Lacala (claca2)
  Ashe Francq (kfrancq2)
  Ashmit Sehgal (asehg2)
"""


def min_length(n):
  """
  Args:
    n: an integer

  Returns:
    the fewest number of 1's in an expression involving only +,*,1,(, and ) which is equal to n, 
    or -1 if no such expression is possible.
  """

  # if n < 1, it's impossible to form a unit expression so return -1
  if n < 1:
    return -1

  # min_ones_table[i] stores the minimum number of 1s needed to express the integer i
  # allocating size n+1 and initializing with infinity to track the min costs
  min_ones_table = [float('inf')] * (n+1)

  # base case: inter 1 needs exactly 1 copy of the number 1
  min_ones_table[1] = 1

  # building solution iteratively from 2 up to target integer n
  for curr_val in range(2, n+1):
    # initializing min_cost with addition from (curr_val-1)+1
    # every number can be formed by adding 1 to the previous optimal expression
    min_cost = min_ones_table[curr_val-1] + min_ones_table[1]

    # Addition: (part1 + part2 = curr_val)
    # checking all possible points up to half of curr_val to avoid repetitive parts (e.g. 2+4 and 4+2)
    # // is floor integer division that rounds down and gets rid of remainders, making sure result is a whole integer for list indexing
    for part1 in range(1, (curr_val // 2) +1):
      part2 = curr_val - part1
      cost_by_addition = min_ones_table[part1] + min_ones_table[part2]

      if cost_by_addition < min_cost:
        min_cost = cost_by_addition

    # Multiplication (factor1 * factor2 = curr_val)
    # iterating the divisors up to the square root(**0.5) of curr_val because factor pairs mirror across the square root 
    max_divisor = int(curr_val**0.5)
    for divisor in range(1, max_divisor+1):
      # checking if divisor is evenly divided into curr_val (remainder is 0)
      if curr_val % divisor == 0:
        factor1 = divisor
        # // is making sure that factor2 is calculated as an integer index for the table lookup
        factor2 = curr_val // divisor

        # excluding factor1 because multiplying by 1 doesn't help in optimizing the expression length
        if factor1 > 1:
          cost_by_multiplication = min_ones_table[factor1] + min_ones_table[factor2]

          if cost_by_multiplication < min_cost:
            min_cost = cost_by_multiplication

    # saving the found min cost for the current integer
    min_ones_table[curr_val] = min_cost
  return min_ones_table[n]


if __name__ == "__main__":
  print("TEST CASES:")

  print("Running Test: n = 6")
  # this should print out 5
  print(f"Result: {min_length(6)}")
  print("Expected: 5\n")

  # Test 1: Negative number (invalid)
  print("Running Test: n = -5")
  print(f"Result: {min_length(-5)}")
  print("Expected: -1\n")

  # Test 2: Zero (invalid)
  print("Running Test: n = 0")
  print(f"Result: {min_length(0)}")
  print("Expected: -1\n")

  # Test 3: Base case 1
  print("Running Test: n = 1")
  print(f"Result: {min_length(1)}")
  print("Expected: 1\n")

  # Test 4: Small base case 2
  print("Running Test: n = 2")
  print(f"Result: {min_length(2)}")
  print("Expected: 2\n")

  # Test 5: Composite number 4 (2 * 2)
  print("Running Test: n = 4")
  print(f"Result: {min_length(4)}")
  print("Expected: 4\n")

  # Test 6: Prime number 5
  print("Running Test: n = 5")
  print(f"Result: {min_length(5)}")
  print("Expected: 5\n")

  # Test 7: Prime number 7
  print("Running Test: n = 7")
  print(f"Result: {min_length(7)}")
  print("Expected: 6\n")

  # Test 8: Composite number 8 (2 * 4)
  print("Running Test: n = 8")
  print(f"Result: {min_length(8)}")
  print("Expected: 6\n")

  # Test 9: Composite number 9 (3 * 3)
  print("Running Test: n = 9")
  print(f"Result: {min_length(9)}")
  print("Expected: 6\n")

  # Test 10: Composite number 12 (3 * 4)
  print("Running Test: n = 12")
  print(f"Result: {min_length(12)}")
  print("Expected: 7\n")

  # ===================
  # Time Complexity: The outer loop runs n times. The inner multiplication loop runs up to sqrt{curr_val} times per iteration, yielding an overall complexity of O(nsqrt{n}) 