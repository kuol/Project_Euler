Project Euler
=============

These exercises are mainly written in python. I'm learning Scala and will put
more scala code. The directory of excercises that are coded in scala have "_sc"
surffix

The order of code I've finished:

  * _07/08/2014_: *Problem 22* (2): easy  
  * _07/09/2014_: *Problem 45* (3): easy, if you know the math  
  * _07/09/2014_: *Problem 15* (4): easy-medium, depends on if you know dynamic programming, 
                                    pure recursive too slow!
  * _07/12/2014_: *Problem 36* (5): medium, I think my algorithm is OK, since I only need to 
                                    test 1110 numbers, but I have problem to come up with a 
                                    more general code that deal with number beyond 1 million.
                                    Maybe recursive algorithm is the way to go...
  * _07/12/2014_: *Problem 31* (4): medium, Coin change problem
  * _07/15/2014_: *Problem 54* (4): Algorithm is easy, coding,testing is harder. Used unittest module to help
  * _07/16/2014_: *Problem 59* (3) easy, if you make educated guess...
  * _07/17/2014_: *Problem 67* (4) Similar to Problem 15 -- think bottom up
  * _07/18/2014_: *Problem 69* (2) It's a problem that you only need a calculator to solve
  * _08/07/2014_: *Problem 102* (1): Really easy if you know basic definition of cross product
  * _09/06/2014_: *Problem 199, 78* (5): I've partially solved Problem 199 -- by looking for reference about Descartes' theorem. It still returns some warning info, which I don't have time to fix for now. For Problem 78 -- it demonstrates that math can be very powerful. Pure dynamic programming simply can't solve it. More work needs to be done
  * _09/17/2014_: *Problem 6* (1): First scala programming exercise!
  * _11/10/2014_: *Problem 68* 5-gon ring(3): the most difficult part for me is to wirte permutation P(n,k) -- forgot how to do it
  * _11/11/2014_: *Problem 85* counting rectangles (2): Pretty straight forward -- use (a+b)>= 2*sqrt(ab) !
  * _11/14/2014_: *Problem 86* shortest path on a centroid (4): Used Euclid formula to generate primitive Pythagorean triples. 
  * _11/26/2014_: I added about 10 easy problems over the weekend.
  * _11/20/2014_: *Problem 82* Three-way path sum (3): very interesting problem. I'm happy with my solution.
  * _11/30/2014_: *Problem 83* Four-way path sum (3): got stuck for 2 days, but found it not hard after writing th 5-by-5 example matrix on paper and start to figure it out. I also added several easy problems... 
  * _11/30/2014_: *Problem 12* first triangle with over 500 divisors (2): Not trivial. Notice,triangle numbers shouldn't have very big prime number as divisors. Generate primes first (I only generated primes < 100)
  * _12/05/2014_: *Problem 14* max Collatz sequence (2): Brute force is easy to implement, but to be smart, you need to re-use all computed collatz numbers
  * _12/06/2014_: *Problem 205* dice game (3): think carefully for the boundary conditions for the recursion 
  * _12/07/2014_: *Problem 76* counting summation (3): Very similar to Problem 78, but luckily less computation is needed, thus a dynamic programming is sufficient.
  * _12/13/2014_: *Problem 34* digit factorials (3): Similar to Problem 30, but much harder. 1) has to less than 8 digits, 2) what numbers do thoses factorial digits make?
  * _12/13/2014_: *Problem 39* integer right angle sum (2): Similar to 75,86
  * _12/20/2014_: *Problem 26* Fraction to decimal (2): pretty straight forward 
  * _01/28/2015_: *Problem 21* Amicable numbers (2): no trick problem 
  * _01/30/2015_: *Problem 41* Pandigital primes (3): need to code permutation with recursion  
  * _01/30/2015_: *Problem 43* Pandigital substring divisibility (3): small modification based on Problem 41.
  * _01/30/2015_: *Problem 38* Pandigital substring divisibility (1): very easy one.
  * _01/30/2015_: *Problem 32* Pandigital multiply (1): very easy one.
  * _01/30/2015_: *Problem 71* Ordered fractions (2): for each possible denominator, what is the possible numerator?
  * _02/26/2015_: *Problem 23* Abundant numbers (3): Find a bug for prime number generator, learned variable nested loop. 
  * _03/28/2015_: *Problem 44* Pentagonal pairs (3): I don't know much math in the problem, the solution is not very perfect. 
