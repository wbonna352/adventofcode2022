library(readr)
library(magrittr)

find_index <- function(input, n) {
  for (i in n:(length(input) - n)) {
    if ((input[(i - n):(i - 1)] %>% unique() %>% length()) == n) {
      return(i - 1)
    }
  }
}

input_data <- read_file_raw("input.txt")

cat("Part one: ", find_index(input_data, 4))
cat("Part two: ", find_index(input_data, 14))
