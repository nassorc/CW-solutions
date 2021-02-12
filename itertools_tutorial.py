import itertools as i, collections

a = [1,2,3,4]
z = ['ABC','DEF']
confusedName = ['M','Z','A','T','T','X','C','H','E','W',]
nameFinder = [1,0,1,1,1,0,0,1,1,1]

numberGroup1 = [1,2,3]
numberGroup2 = [4,5]

accu = i.accumulate(a)
print(list(accu))

chain = i.chain.from_iterable(z)
print(list(chain))

compress = i.compress(confusedName, nameFinder)
print(list(compress))

# equivalent to a nested for-loop
product = i.product(numberGroup1, numberGroup2)
print(list(product))

# all possible orderings, no repeated elements
perm = i.permutations(numberGroup1, 3)
print(list(perm))

# in sorted order, no repeated elements
combi = i.combinations(numberGroup1, 2)
print(list(combi))