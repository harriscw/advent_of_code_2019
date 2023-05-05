
###
# Part 1
###

# Read the input from a file
input <- as.numeric(readLines("../advent.txt"))  

#I had to add as.numeric() above but also chatGPT warned me I would need to do that:
#You may need to modify the code to match the actual format of your input.

# Define a function to calculate the fuel required for a single module
fuel_for_module <- function(mass) {
  fuel <- floor(mass/3) - 2
  if (fuel <= 0) {
    fuel <- 0
  }
  return(fuel)
}

# Calculate the fuel required for each module and sum the values
total_fuel <- sum(sapply(input, fuel_for_module))

# Print the result
cat("The total fuel required is:", total_fuel)


###
# Part 2
###

# Read the input from a file
# input <- readLines("input.txt")

# Define a function to calculate the fuel required for a single module, including the fuel for the fuel
fuel_for_module <- function(mass) {
  total_fuel <- 0
  while (TRUE) {
    fuel <- floor(mass/3) - 2
    if (fuel <= 0) {
      break
    }
    total_fuel <- total_fuel + fuel
    mass <- fuel
  }
  return(total_fuel)
}

# Calculate the fuel required for each module and sum the values
total_fuel <- sum(sapply(input, fuel_for_module))

# Print the result
cat("The total fuel required, including the fuel for the fuel, is:", total_fuel)


###
# Part 2 when asked to solve with a recursive function
###

# Read the input from a file
# input <- readLines("input.txt")

# Define a recursive function to calculate the fuel required for a single module, including the fuel for the fuel
fuel_for_module <- function(mass) {
  fuel <- floor(mass/3) - 2
  if (fuel <= 0) {
    return(0)
  } else {
    return(fuel + fuel_for_module(fuel))
  }
}

# Calculate the fuel required for each module and sum the values
total_fuel <- sum(sapply(input, fuel_for_module))

# Print the result
cat("The total fuel required, including the fuel for the fuel, is:", total_fuel)

