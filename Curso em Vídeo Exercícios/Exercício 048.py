tot = 0
count = 0
for n in  range(0,500,3):
    if n%2 == 1:
        tot += n
        count += 1
print ('A soma de todos os {} valors citados é {}'.format(count, tot))