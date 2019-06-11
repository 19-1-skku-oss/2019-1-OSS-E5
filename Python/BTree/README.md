# 2019-1-OSS-E5
![skku](https://ecostat.skku.edu/_res/board_new/img/board/article_no_img.png)
## About BTree
Last updated: 2019-06-11

### All algorithms implemented in Python (for education)

These implementations are for demonstration purposes. They are less efficient than the implementations in the Python standard library.

## Data Structure


### BTree
![BTree](https://www.techglads.com/wp-content/uploads/2015/06/B-tree-in-C-Example-and-Implementation.gif)

**B-tree** is a self-balancing tree data structure that maintains sorted data and allows searches, sequential access, insertions, and deletions in logarithmic time. The B-tree is a generalization of a binary search tree in that a node can have more than two children. Unlike other self-balancing binary search trees, the B-tree is well suited for storage systems that read and write relatively large blocks of data, such as discs. It is commonly used in databases and file systems.

What, if anything, the B stands for has never been established.

__Properties__ <br>
Time complexity in big O notation <br>
| Algorithm | Average | Worst case |
| --- | --- | --- |
| Space | O(n) | O(n) |
| Search | O(log n) | O(log n) |
| Insert | O(log n) | O(log n) |
| Delete | O(log n) | O(log n) |

###### Source: [Wikipedia][bubble-wiki] 
###### View the algorithm in [action][bubble-toptal]
