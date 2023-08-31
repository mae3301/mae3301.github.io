---
layout: post
title: Lab Report on Unsolved Word Lengths 
---

## Summary
The unsolved portion of Liber Primus has far fewer words of length two than normal English written in 3301's runic alphabet (hereafter "runeglish"). It also has more words of length three than runeglish.  Other reasonably-chosen metrics reflecting word length show it as typical runeglish.

## Introduction
My goal was to reject or fail to reject the null hypothesis that unsolved LP had the word lengths of runeglish.

## Method
I used mortlach's [first Project Runeberg corpus](https://github.com/mortlach/project-runeberg) for my runeglish baseline.   This consists of [Project Gutenberg](https://www.gutenberg.org/) texts transcribed into 3301's runic alphabet.  From each text, I drew a sample consisting of the same number of words as unsolved LP,  namely 2902  words.  I discarded texts that were less than 2902 words in length.  For each sample, I calculated a variety of basic statistics, including mean, standard deviation, and others.  In this way I collected an array of length 25,566 for each sample statistic. 

I then calculated the same set of statistics for the unsolved Liber Primus.
I compared the test statistics of the unsolved LP to its sampling distribution under the null hypothesis, represented by the array collected from analyzing Project Runeberg.

I calculated the following one-sided p-value using the python function:

```python
def empirical_p_value(distribution, val):
    result = sum(distribution < val) / len(distribution)
    return result
```

This function simply calculates the fraction of the sample distribution less than or equal to the test statistic.

The full code is available in my [github repository](https://github.com/mae3301/).

## Results
The following table summarizes my results. 

|statistic|project_runeberg_average|liber_primus_value|one_sided_left_p_value|
|:------:|:------:|:------:|:------:|
|length_1|0.046|0.031|0.202|
|length_2|0.244|0.154|0.005|
|length_3|0.19|0.248|0.947|
|length_4|0.151|0.177|0.854|
|length_5|0.105|0.109|0.636|
|length_6|0.086|0.088|0.609|
|length_7|0.066|0.074|0.739|
|length_8|0.044|0.054|0.788|
|length_9|0.032|0.027|0.361|
|length_10|0.018|0.018|0.562|
|length_11|0.01|0.011|0.654|
|length_12|0.004|0.006|0.795|
|length_13|0.002|0.001|0.505|
|length_14|0.001|0.001|0.812|
|max|14.767|14.0|0.517|
|mean|4.24|4.467|0.794|
|median|3.731|4.0|omitted|
|min|1.0|1.0|omitted|
|percentile_25|2.055|3.0|omitted|
|percentile_75|5.653|6.0|omitted|
|std|2.373|2.321|0.43|

Note that I have omitted the p_values for statistics that do not have very many values, like the median. In these case, inspection shows that the LP value was not unusual.  For the continuous statistics, when the p_value is near 50%, this means that the LP value was like runeglish.  When it is far away, it means that it is unusual.

The most extreme deviations from runeglish are in the proportion of words of length two and the portion of words of length three.   The following graphs show the sampling distributions of the statistics and the position of the LP value.

There are relatively few two rune words and a relatively greater number of three rune words.

![my_graph]({{site.url}}/images/rune-words-len-two.png)
![my_graph]({{site.url}}/images/rune-words-len-three.png)


## Discussion

Well, folks, we have rejected the null hypothesis.  Unsolved LP looks pretty different from runeglish when we examine the number of two-rune words and to a lesser extent, three-runes words.

The analysis here was fairly simple. The question is just how to interpret the results.  First of all, there is the issue of the choice of baseline.  The Project Runeberg dataset may not be the best baseline for runeglish. Solver ether8unny suggests the proportion of one-rune words is too high.  Solver mortlach suggests an alternative dataset, namely his [google n-grams dataset](https://github.com/mortlach/google_ngrams_Version-20200217).

Second, we can of course conjecture what has caused this deviation from normal runeglish.  Some conjectures so far have been:
* stylistic choice on the part of 3301
* 3301 choosing to spell 'the' 't-h-e' instead of 'th-e' in the unsolved portion
* a cipher that changes the number of characters in a subset of runeglish words
* word length actually don't mean anything
* a second gematria entirely

This analysis also suggests various analyses on word lengths. For instance, solved LP is different from unsolved LP and I'm pretty sure like runeglish (i.e. one would fail to reject the null hypothesis given these statistics.)  But I did not actually establish that here and to do so one would need to repeat the analysis with Project Runeberg texts.

Second, it would be a good idea to repeat the analysis using the google n-gram dataset.

Third, I should probably use a two-sided p-value and make my criterion for acceptance/rejection rigorous.

And many more . . . 

I'm a bit tired but do encourage other people to take up the baton.



## Final Words
