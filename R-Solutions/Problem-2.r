# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

fib_maker <- function(limit){
  fib_arr <- c(1,2)
  while(fib_arr[length(fib_arr)] + fib_arr[length(fib_arr) - 1] <= limit){
    fib_arr <- append(fib_arr, fib_arr[length(fib_arr)] + fib_arr[length(fib_arr) - 1])
  }
  return(fib_arr)
}

even_fib_summer <- function(fib_list){
  answer = 0
  for(i in fib_list){
    if(i %% 2 == 0){
      answer <- answer + i
    }
  }
  return(answer)
}

my_list <- fib_maker(4000000)
final_answer <- even_fib_summer(my_list)
print(final_answer)
