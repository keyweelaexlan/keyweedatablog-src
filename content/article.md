Title: Doc2Vec for facebook page text classification
Date: 2016-02-21 10:20
Modified: 2016-02-21 19:30
Category: Text algorithms
Tags: doc2vec, nlp, facebook
Slug: doc2vec-label-classification
Authors: Alex Lan


![TSNE Visualisation of facebook page similarity]({filename}/images/tsne.png)


The original doc2vec paper has no restriciton on the number of labels per document,
yet online examples on how to use gensims doc2vec always use a single label, usually as SENT_SENTENCE_NUMBER.

Usually these methods produce a vector per document which can be used later to train a classifier for higher order categories. 
In this blog post we try to perform such high level classification by assigning multiple labels per document directly. 

We used publicly available facebook posts (/feed end point) to collect 311k facebook page posts from 188 pages. 
For each link post we open its link and collect the clean page text using jusText and store it in the content field.
We finally store all of these posts in one pandas dataframe.
 
Since pages tend to publish content which isn't purely their style we break down each page's posts into groups by share rank percentile.
For each page we rank the posts by how many shares they have and assign discreet ten percent interval bins. So a post which outperforms 93% of other posts
will be in the 90th percentile bin. 

For each document we assign two types of tags:

1. The post id as "Post_ID:[Post ID]
+  [Page name]_Share_Rank_Percentile, For eaxmple WIRED_90

## Calculating share rank percentile and building the document iterator
{% notebook notebook.ipynb cells[-5:] %}


For each label (facebook page or post) we get a vector in 300 dimensions. In order to easily visualise it and perform a sanity we do a TSNE manifold. Its a dimensionality reduction which preserves distances.


{% notebook notebook.ipynb cells[4:10] %}


