#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Assuming A is being incremented somehow so that the while loop ends eventually this should be O(n) since canceling out extra terms with division: n ** 3 divided by n ** 2 is n. 


b) The first loop is O(n) and the second is O(log base 2 n) so multiplied together its O(n log n)


c) This is O(n) since it is just called n times until reaching base case. 

## Exercise II

So with only one egg, we could only do the naive solution of moving it up one level each time and trying again until it fails which is:
O(N)

If we have infinite eggs, than the most easiest thing to do is a binary search. We'd start at the halfway point and then pick lower or higher depending on if it doesn't or does break. 

So it's something like:

Start at halfway point and drop egg

if it breaks, new halfway point is between old halfway and bottom

if it doesn't, new halfway point is between old halfway and top

recursively do this until:

distance between old halfway and new halfway is 1 

AND

old halfway is a break and new halfway is a save

and then 

RETURN the latest new halfway is the highest floor that eggs don't crack 