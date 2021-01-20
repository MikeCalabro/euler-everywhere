# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

function fibListMaker(limit)
  list = [1,2]
  while list[end] + list[end-1] < limit
    push!(list, list[end] + list[end-1])
  end
  list
end

function evenFibSummer(limit)
  sum([i for i in fibListMaker(limit) if i % 2 == 0])
end

evenFibSummer(4000000)
