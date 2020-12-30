// Which starting number, under one million, produces the longest Collatz chain?

collatzLength = (num) => {
  let len = 1;
  while (num > 1) {
    if (num % 2 == 0) {
      num /= 2;
    } else {
      num = num*3+1;
    }
    len += 1
  }
  return len
}

maxCollatz = (limit) => {
  let answer = 0;
  let max_len = 0;
  for (i=3;i<limit;i+=2) {
    let len = collatzLength(i);
    if (len > max_len) {
      answer = i;
      max_len = len;
    }
  }
  return [answer, max_len];
}

console.log(maxCollatz(1000000));
