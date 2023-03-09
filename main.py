import pandas as pd

# Ask the user to enter an integer value greater than 0
n = int(input("Enter a positive integer greater than 0: "))

# Use a conditional statement to check the user's entry is greater than 0
if n <= 0:
  print("Invalid input. Please enter a positive integer greater than 0.")
else:
  # Create lists for each sequence
  even_nums = [2 * i for i in range(n)]
  odd_nums = [2 * i + 1 for i in range(n)]
  fibonacci_nums = [0, 1]
  for i in range(2, n):
    fibonacci_nums.append(fibonacci_nums[i - 1] + fibonacci_nums[i - 2])

  # Combine the lists into a data frame
  data = {
    "Even Numbers": even_nums,
    "Odd Numbers": odd_nums,
    "Fibonacci Numbers": fibonacci_nums
  }
  df = pd.DataFrame(data)

  # Display the data frame
  print(df)
