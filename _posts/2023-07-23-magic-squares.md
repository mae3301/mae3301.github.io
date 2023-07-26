---
layout: post
title: Lab Report on Magic Squares 
---

## Summary 
The solved portions of [*Liber Primus*](https://uncovering-cicada.fandom.com/wiki/Liber_Primus_Unsolved_Pages) allow us to fill in part, but not all, of the magic squares in sections 3 and 7 of that text with words.

## Disclaimer/Warning
Nothing dangerous about this investigation, unless it is the danger posed to one's mental health by obsessing.  

Some of the history is taken from the Cicada 3301 wiki, since I did not participate in the 2012-2014 challenges.  I have tried my best to link back to the wiki where appropriate.

## Introduction 
Setting up the parameters of the problem here requires a deep dive into the world of the 3301 challenge and the puzzles leading up to the delivery of the final 58 pages of *Liber Primus*.

### 2013

In 2013, solving the puzzles included uncovering the following [jpg file](https://uncovering-cicada.fandom.com/wiki/What_Happened_Part_1_(2013)?file=Testout.jpg). Inspecting the image shows a three-column table entitled "Gematria Primus: an order and a value as revealed through 3301."  The table, reproduced below, presents 29 unfamiliar symbols labeled as "runes" in order. The table also maps the ordered runes to the series of ascending prime numbers, so that the first prime (2) is the value of the first letter ("ᚠ"), and so on. Finally the table maps each rune to a letter of the Roman alphabet. 

|Rune | Letter | Value |                  
|:------:|:----------:|:--------:|       
|ᚠ| F | 2 |				  
|ᚢ| U | 3 |                               
|ᚦ| TH | 5 |                               
|ᚩ|O|7|					  
|ᚱ|R|11|				  
|ᚳ|C/K|13|				  
|ᚷ|G|17|				  
|ᚹ|W|19|			         
|ᚻ|H|23|                                 
|ᚾ|N|29|				 
|ᛁ|I|31|                                 
|ᛄ|J|37|                                 
|ᛇ|EO|41|                                
|ᛈ|P|43|                                  
|ᛉ|X|47|
|ᛋ|S/Z|53|
|ᛏ|T|59|
|ᛒ|B|61| 
|ᛖ|E|67|
|ᛗ|M|71|
|ᛚ|L|73|
|ᛝ|NG/ING|79|
|ᛟ|OE|83|
|ᛞ|D|89|
|ᚪ|A|97|
|ᚫ|AE|101|
|ᚣ|Y|103|
|ᛡ|IA/IO|107|
|ᛠ|EA|109| 

Besides providing solvers with a mapping of sorts, the jpg introduced the idea of gematria to the puzzle. The word comes from the [] word for . Wikipedia explains that "." The runes provided by the table are of course not Hebrew letters. According to the [cicada wiki](), they were identified by a solver as a variant of the Anglo-Saxon rune set. 

Other stages of the 2013 puzzle encouraged solvers to use the values of characters to perform traditional and perhaps less traditional feats of gematria. For instance, the 2013 [telnet service]() encouraged solvers to add up the values associated with letters in a word to arrive at a larger number (henceforth referred to as a gematria sum). A second example, the poem "Parable," essentially taught solvers to associate sentences with the gematria sums of the values of the characters making them up. It even illustrated how multiplying together the gematria sums of three sentences led to a gematria product. 

### 2014
The 2014 puzzle required solvers to submit one of three magic squares to a service in order to reach the next step of the game. A magic square is an matrix of numbers whose rows, columns, and sometimes diagonals all sum to the same number. The magic squares used by 3301 had sums of 3301 and 1033. One of the squares (sum 1033) is the following:

|272|138|341|131|151|
|366|199|130|320|18|
|226|245|91|245|226|
|18|320|130|199|366|
|151|131|341|138|272|

Two of the very same magic squares then appear in the first portion of *Liber Primus*, "Intus".  The second square is simply represented as numbers, but the first square (sum 1033) is more interesting. In *Liber Primus* some of the numbers have been replaced by words whose gematria sum equals the number.

|272|138|ᛋᚻᚪᛞᚩᚹᛋ|131|151|
|ᚫᚦᛖᚱᛠᛚ|ᛒᚢᚠᚠᛖᚱᛋ|ᚢᚩᛁᛞ|ᚳᚪᚱᚾᚪᛚ|18|
|226|ᚩᛒᛋᚳᚢᚱᚪ|ᚠᚩᚱᛗ|245|ᛗᚩᛒᛁᚢᛋ|
|18|ᚪᚾᚪᛚᚩᚷ|ᚢᚩᛁᛞ|ᛗᚩᚢᚱᚾᚠᚢᛚ|ᚫᚦᛖᚱᛠᛚ|
|151|131|ᚳᚪᛒᚪᛚ|138|272|

For instance, in the first row, the number 341 has been replaced by "ᛋᚻᚪᛞᚩᚹᛋ" ("SHADOWS"), a word whose gematria sum is 53 + 23 + 97 + 89 + 7 + 19 + 53 = 341.
### 2016
In 2016, 3301 posted the following enigmatic signed message to their twitter account.

    Hello.

    The path lies empty; epiphany seeks the devoted.

    Liber Primus is the way.  Its words are the map, their
    meaning is the road, and their numbers are the direction.

    Seek and you will be found.


    Good luck.

    3301

The phrase "their numbers" calls back to the first section of "Intus," which warns: "Do not edit or change this book. Or the message contained within. Either the words or their numbers. For all is sacred." 

In both cases, 3301 refers to the "numbers" of the words.  In what sense does a word possess a number or numbers? A gematria sum of the individual letters in the word is certainly one way, and one that had been reinforced by previous puzzles.

It seemed to me that if 3301 wanted solvers to look at the numbers of the words, maybe the magic square was a clue. [say more]  Thus I set out to look for words or sentences in the solved LP whose gematria sums were in the magic squares.   

### A brief mathematical treatment of the Gematria Primus
We can treat the "value" of a rune as a mapping from each of the 29 runes in the runic alphabet to a prime number.  Thus
V: 
V is a function, insofar as each rune is associated with only one prime. It is moreover one-to-one, insofar as each prime is associated with at most one rune. 

The gematria sum (henceforth G) is a second and related mapping. Its domain is string of runes and its range is a natural number, which may or may not be prime.  The formal definition of G is: 

Like V, G is a function: each string of runes has a single gematria sum. However, it definitely is not one-to-one. Many different strings for runes have the same sum. This means that the inverse of G, G-1, is not a function. Practically speaking, any attempt to map a number back to a string of runes requires choosing which of many different runes to associate with that number. Simply requiring that the string be an English word is not enough. In fact, the magic square illustrates this property of the gematria sum by associating [] and [] with the letter .

How to restrict the universe of strings? Since the 2016 "hint" mentioned the Liber Primus in particular, I decided to focus on the solved portion of that text. Of course, conducting a "book search" didn't guarantee that I would find exactly what I was looking for: one or at most two words or sentences associated with each number in a magic squares. I was hoping that in this respect the
LP would be well-behaved. That in turn would make me feel like I was on the right track. 

## Method
My method was pretty simple.  I wrote a python program to calculate the gematria sums of the words and sentences in the solved pages. Once I had this data, I iterated through the numbers in each magic square to see if one or more word was associated with the number.
 
## Results ##
I was able to find words corresponding to all but one of the numbers in the first magic square and only one in the second magic square. No sentence in the LP corresponded to any magic square numbers.

The matches I did find are presented below.

## Discussion 
Because the map between rune strings and sums is not one-to-one, it does not have a well-defined inverse.  It is thus unclear how to match a number with a string when multiple strings can have the same sum.  Restricting the search to a small universe of string could solve that problem, but there is no guarantee that it will. It is difficult, perhaps impossible, to find a natural corpus large enough to provide strings for each number in the squares and still small enough to avoid the problem of repeats.
 
## Final Words

3301 certainly seemed to be teaching solvers how to calculate gematria sums in 2013 and 2014. The magic square in section of the LP was part of that education and remains a tantalizing clue.  Yet it is unclear if the mapping G can help to solve *Liber Primus*. 
