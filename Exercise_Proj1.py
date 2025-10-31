import matplotlib.pyplot as plt
fhand = open("StudentExercise1.csv")
def average(ls):
    avg = sum(ls)/len(ls)
    return avg
def prop_above(scores):
    avg_scr = sum(scores)/len(scores)
    abv_avg = sum(1 for score in scores if score > avg_scr)
    proportion = abv_avg / len(scores)
    return proportion
def median(ls):
    if not ls:
        return None
    sorted_ls = sorted(ls)
    n = len(sorted_ls)
    if n% 2==1:
        return sorted_ls[n//2]
    else:
        mid1 = sorted_ls[n//2-1]
        mid2 = sorted_ls[n//2]
        return (mid1 + mid2)/2
next(fhand)
nums = []
for line in fhand:
    pieces = line.split(",")
    hours = pieces[0]
    if hours != '':
        hr = float(hours)
        nums.append(hr)
n_bins = 20
fig, ax = plt.subplots()
ax.hist(nums, bins=n_bins)
ax.set(xlabel='counts',
    title = 'hours of exercise')
plt.show()
print(average(nums))
print(prop_above(nums))
print(median(nums))
        
