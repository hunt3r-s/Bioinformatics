# Bioinformatics Algorithms

These files provide solutions for some of the problems from [Rosalind](https://rosalind.info/problems/locations/), a website hosting bioinformatics coding problems.  
A summary of the problems is provided below.  

## [Burrows-Wheeler Matching](BWMatching.py)  
The [Burrows-Wheeler matching](https://rosalind.info/problems/ba9l/) problem is concerned with finding the number of patterns in a string (in this case, a DNA sequence)  
which result from applying a Burrows-Wheeler transform to the string.  

### Input:   
A string *BWT(Text)*, followed by a collection of strings *Patterns*.  

### Output:  
A list of integers, where the *i*-th integer corresponds to the number of substring matches of the *i*-th member of *Patterns* in *Text*.  

## [Gibbs Sampler](GibbsSampler.py)  
The [Gibbs sampler](https://rosalind.info/problems/ba2g/) problem is concerned with generating random *k*-mers from a collection of DNA strings.  

### Input:  
Integers *k*, *t*, and *N*, followed by a collection of strings *Dna*.

### Output:  
The strings *BestMotifs* resulting from running *GibbsSampler(Dna, k, t, N)* with 20 random starts.

## [Local Alignment](LocalAlignment.py)  
Although not strictly a bioinformatics problem, the [local alignment](https://rosalind.info/problems/ba5f/) problem in this case, involves finding the optimal alignment between two amino acid strings.  

### Input:  
Two amino acid strings

### Output:  
The maximum score of a local alignment of the strings, followed by a local alignment of these strings achieving the maximum score.

## [String Clumps](StringClumps.py)  
Given a DNA string, the [string clumps](https://rosalind.info/problems/ba1e/) problem seeks to instances where a substring occurs a specified number of times.

### Input:  
A string *Genome*, and integers *k*, *L*, and *t*.

### Output:  
All distinct *k*-mers forming *(L, t)*-clumps in *Genome*.

## [UPGMA](UPGMA.py)  
UPGMA stands for "unweighted pair group method arithmetic mean", it is a method of clustering entries of a matrix to form a weighted relational graph. The [UPGMA](https://rosalind.info/problems/ba7d/) problem is concerned with forming such a graph.  

### Input  
An integer *n* followed by a space-delimited *n x n* distance matrix.

### Output  
An adjacency list for the ultrametric tree output by **UPGMA**.
