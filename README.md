Problem Description:


It’s the ber-months so Jose Mari Chan and his friends want to buy a lot of candies to give out for Christmas. But the candy store owner wants to maximize his number of new customers and the money he makes. To do this, he decides he’ll multiply the price of each candy by the number of that customer’s purchase. This means that the first candy purchase will be original price, (1)(ORIGINAL PRICE) , the second purchase will be (2)(ORIGINAL PRICE), the third will be (3)(ORIGINAL PRICE) and so on. 

Given the size of the group of friends, the number of candies they want to purchase and the original prices of the candies, determine the minimum cost to purchase all of the candies.

For example, if there are k = 3 friends that want to buy n = 4 candies that cost c = [1,2,3,4] , each will buy one of the candies priced [2,3,4]at the original price. Having each purchased 1 candy, the first candy in the list, c[0], will now cost (purchase number) x c[0] = 2 x 1 = 2. The total cost of all the purchases will be 2 + 3 + 4 + 2 = 11 .


Function Description

Implement the getMinimumCost function which should return an integer representing the minimum cost it takes to purchase all the candies. This function will have the following parameter(s):

 - k: an integer, the number of friends
 - c: a sorted array of integers representing the original price of each candy


 Sample input:

 - 3 3
 - 2 5 6

 Output:

 - 13


 Sample input:

 - 3 2
 - 2 5 6

 Output:

 - 15


 