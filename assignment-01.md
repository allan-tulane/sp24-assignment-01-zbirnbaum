

# CMPS 2200 Assignment 1

**Name:** Zoe Birnbaum


In this assignment, you will learn more about asymptotic notation, parallelism, functional languages, and algorithmic cost models. As in the recitation, some of your answer will go here and some will go in `main.py`. You are welcome to edit this `assignment-01.md` file directly, or print and fill in by hand. If you do the latter, please scan to a file `assignment-01.pdf` and push to your github repository. 
  
  

1. (2 pts ea) **Asymptotic notation** (12 pts)

  - 1a. Is $2^{n+1} \in O(2^n)$? Why or why not? 
.  
.  Yes, because 2^(n+1) can be broken down into 2 * 2^n, and the constant c = 2 does not impact the runtime complexity to make it not belong to O(2^n). 
.  
.  
. 
  - 1b. Is $2^{2^n} \in O(2^n)$? Why or why not?     
.  
.  No, because the 2^n in the exponent's place is exponential in itself, not linear, therefore 2^(2^n) is not belonging to O(2^n) because it is larger.
.  
.  
.  
  - 1c. Is $n^{1.01} \in O(\mathrm{log}^2 n)$?    
.  
.  No, because log^{2}n belongs to O(log(n)) which grows slower than O(n), and n^1.01 is essentially of linear runtime complexity. 
.  
.  

  - 1d. Is $n^{1.01} \in \Omega(\mathrm{log}^2 n)$?  
.  
.  Yes, because as stated in the previous answer, n^1.01 grows at a faster rate than log^{2}n, so it belongs to Ω(log^{2}n).
.  
.  
  - 1e. Is $\sqrt{n} \in O((\mathrm{log} n)^3)$?  
.  
.  No, because the square root function asymptotically dominates the polynomial function (logn)^3.
.  
.  
  - 1f. Is $\sqrt{n} \in \Omega((\mathrm{log} n)^3)$?  

  Yes, via the previous answer, the square root functions grows at a faster rate than (logn^3), so it belongs to its best case/omega notation.


2. **SPARC to Python** (12 pts)

Consider the following SPARC code of the Fibonacci sequence, which is the series of numbers where each number is the sum of the two preceding numbers. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ... 
$$
\begin{array}{l}
\mathit{foo}~x =   \\
~~~~\texttt{if}{}~~x \le 1~~\texttt{then}{}\\
~~~~~~~~x\\   
~~~~\texttt{else}\\
~~~~~~~~\texttt{let}{}~~(ra, rb) = (\mathit{foo}~(x-1))~~,~~(\mathit{foo}~(x-2))~~\texttt{in}{}\\  
~~~~~~~~~~~~ra + rb\\  
~~~~~~~~\texttt{end}{}.\\
\end{array}
$$ 

  - 2a. (6 pts) Translate this to Python code -- fill in the `def foo` method in `main.py`  

  - 2b. (6 pts) What does this function do, in your own words?  

.  This function returns the xth (via input x) fibonacci number in the fibonacci sequence. The fibonacci sequence is a sequence of numbers where any number is the sum of the two preceding numbers, with the exception of the two base cases (first two numbers in the sequence), 0 and 1. So, this function recursively calculates the fibonacci number at index "x" in the sequence. 
.  


3. **Parallelism and recursion** (26 pts)

Consider the following function:  

```python
def longest_run(myarray, key)
   """
    Input:
      `myarray`: a list of ints
      `key`: an int
    Return:
      the longest continuous sequence of `key` in `myarray`
   """
```
E.g., `longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3`  
 
  - 3a. (7 pts) First, implement an iterative, sequential version of `longest_run` in `main.py`.  

  - 3b. (4 pts) What is the Work and Span of this implementation?  

.  The work of this function is O(n) because it is executed as a for loop with no additional/nested loops. For the same reason, the span of this function is also O(n).
.

  - 3c. (7 pts) Next, implement a `longest_run_recursive`, a recursive, divide and conquer implementation. This is analogous to our implementation of `sum_list_recursive`. To do so, you will need to think about how to combine partial solutions from each recursive call. Make use of the provided class `Result`.   

  - 3d. (4 pts) What is the Work and Span of this sequential algorithm?  
.  Both the work and span are still O(n) with the recursive version of finding the longest run. 
.  

  - 3e. (4 pts) Assume that we parallelize in a similar way we did with `sum_list_recursive`. That is, each recursive call spawns a new thread. What is the Work and Span of this algorithm?  

.  If we parallelized in that way, the work and span of this new algorithm would be O(logn), since the algorithm computes with half the work and span as the sequential version. 
.  
.  
.  
.  
.  
.  
.  

