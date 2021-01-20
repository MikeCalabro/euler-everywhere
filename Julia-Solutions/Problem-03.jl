# What is the largest prime factor of the number 600851475143?

function isPrime(num)
  if num < 2
    return false
  elseif num == 2
    return true
  else
    return sum([1 for i in [2:Int(round(sqrt(num)));] if num % i == 0]) == 0
  end
end

function primeFactors(num)
  return [i for i in [2:Int(round(sqrt(num)));] if num % i == 0 && isPrime(i)]
end

primeFactors(600851475143)[end]
