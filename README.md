# Document_Retrival_Using_TF-IDF
Ranks documents based on query relevance using cosine similarity. Expands query using association rules to include additional relevant terms.
**#OUTPUT**

Enter the number of documents: 3
Enter document 1: The quick brown fox jumps over the lazy dog
Enter document 2: A quick brown dog jumps over the lazy fox
Enter document 3: The quick brown cat jumps over the lazy dog
Enter the query: quick brown fox
Documents ranked by relevance to query:
1. Document 2 (cosine similarity: 0.74):
A quick brown dog jumps over the lazy fox

2. Document 1 (cosine similarity: 0.74):
The quick brown fox jumps over the lazy dog

3. Document 3 (cosine similarity: 0.37):
The quick brown cat jumps over the lazy dog

Frequent itemsets:
     support                              itemsets
0   0.666667                                 (fox)
1   1.000000                                (jump)
2   1.000000                                 (dog)
3   0.333333                                 (cat)
4   1.000000                               (quick)
..       ...                                   ...
90  1.000000       (jump, dog, quick, brown, lazy)
91  0.333333       (jump, cat, quick, brown, lazy)
92  0.333333        (dog, cat, quick, brown, lazy)
93  0.666667  (fox, jump, dog, quick, brown, lazy)
94  0.333333  (jump, dog, cat, quick, brown, lazy)

[95 rows x 2 columns]
Association rules:
     antecedents                      consequents  antecedent support  \
0          (fox)                           (jump)            0.666667   
1         (jump)                            (fox)            1.000000   
2          (fox)                            (dog)            0.666667   
3          (dog)                            (fox)            1.000000   
4          (fox)                          (quick)            0.666667   
...          ...                              ...                 ...   
1019       (dog)  (jump, cat, quick, brown, lazy)            1.000000   
1020       (cat)  (jump, dog, quick, brown, lazy)            0.333333   
1021     (quick)    (jump, dog, cat, brown, lazy)            1.000000   
1022     (brown)    (jump, dog, cat, quick, lazy)            1.000000   
1023      (lazy)   (jump, dog, cat, quick, brown)            1.000000   

      consequent support   support  confidence  lift  leverage  conviction  
0               1.000000  0.666667    1.000000   1.0       0.0         inf  
1               0.666667  0.666667    0.666667   1.0       0.0         1.0  
2               1.000000  0.666667    1.000000   1.0       0.0         inf  
3               0.666667  0.666667    0.666667   1.0       0.0         1.0  
4               1.000000  0.666667    1.000000   1.0       0.0         inf  
...                  ...       ...         ...   ...       ...         ...  
1019            0.333333  0.333333    0.333333   1.0       0.0         1.0  
1020            1.000000  0.333333    1.000000   1.0       0.0         inf  
1021            0.333333  0.333333    0.333333   1.0       0.0         1.0  
1022            0.333333  0.333333    0.333333   1.0       0.0         1.0  
1023            0.333333  0.333333    0.333333   1.0       0.0         1.0  

[1024 rows x 9 columns]
Expanded query:
['fox', 'jump', 'dog', 'cat', 'quick', 'brown', 'lazy']
