# Find the sum of all the multiples of 3 or 5 below 1000.

function threeOrFive(num)
  sum([i for i in [1:num-1;] if i % 3 == 0 || i % 5 == 0])
end

threeOrFive(1000)
