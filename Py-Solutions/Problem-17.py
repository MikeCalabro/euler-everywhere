# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

arr =  [["one",       191],
        ["two",       190],
        ["three",     190],
        ["four",      190],
        ["five",      190],
        ["six",       190],
        ["seven",     190],
        ["eight",     190],
        ["nine",      190],
        ["ten",        10],
        ["eleven",     10],
        ["twelve",     10],
        ["thirteen",   10],
        ["fourteen",   10],
        ["fifteen",    10],
        ["sixteen",    10],
        ["seventeen",  10],
        ["eighteen",   10],
        ["nineteen",   10],
        ["twenty",    100],
        ["thirty",    100],
        ["forty",     100],
        ["fifty",     100],
        ["sixty",     100],
        ["seventy",   100],
        ["eighty",    100],
        ["ninety",    100],
        ["hundred",   900],
        ["and",       891],
        ["thousand",   1]]

def main():
  print(sum([len(arr[i][0])*arr[i][1] for i in range(0,len(arr))]))

if __name__ == '__main__':
  main()
