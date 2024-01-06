from itertools import count

given_year = int(input())

print(next(year for year in count(given_year + 1) if len(set(str(year))) == 4))
