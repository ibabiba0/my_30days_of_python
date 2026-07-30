#Level 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages_sorted = sorted(ages)
min_age, max_age = ages_sorted[0], ages_sorted[-1]
if len(ages_sorted) % 2 == 0: # even number of items in list
    median_ages = [ages_sorted[len(ages_sorted)//2 - 1], ages_sorted[len(ages_sorted)//2]]
else:
    median_age = ages_sorted[len(ages_sorted)//2 + 1]
average_age = sum(ages_sorted) / len(ages_sorted)
range_age = max_age - min_age
