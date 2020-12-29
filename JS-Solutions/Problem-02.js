// By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

const fib_maker = (limit) => {
  fib_arr = [1,2];
  while(fib_arr[fib_arr.length - 1] + fib_arr[fib_arr.length - 2] <= limit){
    fib_arr.push(fib_arr[fib_arr.length - 1] + fib_arr[fib_arr.length - 2]);
  }
  return(fib_arr);
}

const even_fib_summer = (fib_list) => {
  answer = 0;
  for(i=0;i<fib_list.length;i++){
    if(fib_list[i] % 2 == 0){
      answer += fib_list[i];
    }
  }
  return(answer)
}

my_list = fib_maker(4000000);
final_answer = even_fib_summer(my_list);
console.log(final_answer);