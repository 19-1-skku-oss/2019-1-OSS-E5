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
What, if anything the  stands for has never been established.

---
전산학에서 B-트리(B-tree)는 데이터베이스와 파일 시스템에서 널리 사용되는 트리 자료구조의 일종으로, 이진 트리를 확장해 하나의 노드가 가질 수 있는 자식 노드의 최대 숫자가 2보다 큰 트리 구조이다.

방대한 양의 저장된 자료를 검색해야 하는 경우 검색어와 자료를 일일이 비교하는 방식은 비효율적이다. B-트리는 자료를 정렬된 상태로 보관하고, 삽입 및 삭제를 대수 시간으로 할 수 있다. 대부분의 이진 트리는 항목이 삽입될 때 하향식으로 구성되는 데 반해, B-트리는 일반적으로 상향식으로 구성된다.

n개의 키 (s1,s2,s3...,sn)가 있는 한 노드를 생각해 보자. 키집합은 정렬되어 있다고 한다. (즉, s1<s2<s3...<sn) 그 노드는 n+1자식노드를 가리키는 포인터로 구성된다. 즉, t0,t1,t2...tn.

B-트리의 기본 개념은 내부 노드의 자식 노드의 수가 미리 정해진 범위 내에서 변경가능하다는 것이다. 항목이 삽입되거나 삭제될 때, 내부 노드는 해당 범위의 자식 노드의 수를 만족시키기 위해 분리되거나 혹은 다른 노드와 합쳐지게 된다. 자식 노드의 수가 일정 범위 내에서만 유지되면 되므로 분리 및 합침을 통한 재균형 과정은 다른 자가 균형 이진 탐색 트리만큼 자주 일어나지 않지만, 저장 공간에서의 손실은 있게 된다. 자식 노드의 최소 및 최대수는 일반적으로 특별한 구현에 대해서 결정되어 있다. 예를 들어, 2-3 B-트리(혹은 단순히 2-3 트리)에서 각 내부 노드는 2 또는 3개의 자식 노드를 가질 수 있다. 만약 허용되지 않은 수의 자식 노드를 가질 경우, 해당 내부 노드는 부적절한 상태에 있다고 한다.

B-트리는 노드 접근시간이 노드에서의 연산시간에 비해 훨씬 길 경우, 다른 구현 방식에 비해 상당한 이점을 가지고 있다. 이는 대부분의 노드가 하드디스크와 같은 2차 저장장치에 있을 때 일반적으로 일어난다. 각 내부 노드에 있는 자식 노드의 수를 최대화함으로써, 트리의 높이는 감소하며, 균형맞춤은 덜 일어나고, 효율은 증가하게 된다. 대개 이 값은 각 노드가 완전한 하나의 디스크 블록 혹은 2차 저장장치에서의 유사한 크기를 차지하도록 정해진다.<br><br>

#### Definition of B-tree ####
1. Every node has at most m children (m: B-tree of order).
2. Every non-leaf node (except root) has at least ⌈m/2⌉ children.
3. A non-leaf node with k children contains k−1 keys.
4. All leaves appear in the same level
---
1. 모든 Node는 최대 m개의 Children Nodes를 가질 수 있다. (단, m은 B-tree의 차수)
2. Root node를 제외한 모든 non-leaf node는 최소 ⌈m/2⌉ Children Nodes를 가져야 한다.
3. k개의 Children Nodes를 가지는 non-leaf node는 k-1개의 keys를 가진다.
4. 모든 leaf nodes는 같은 Level에 존재해야 한다.<br><br>
#### Implementation(function) ####
1. class BTree<br><br>
class BTree has information of degree and root node.<br><br>
class BTree는 degree와 root node에 관한 정보를 가집니다.

---
2. class BTreeNode<br>
BTreeNode is a basic component of BTree. It is consisted with keys, childs, parent. It also has a boolean variable 'leaf' that notices it is leaf node or not.<br><br>
BTreeNode는 BTree의 기본 구성 요소입니다. BTreeNode는 keys, childs, parent에 관한 정보를 가집니다. 또한, variable 'leaf'는 현재 node가 leaf인지 아닌지를 나타내는 boolean variable 입니다.

---
3. function traverse<br>
traverse is a funcation that traverse BTree by Inorder traversal. If you want some information of Inorder-traversal, please click this [link](https://en.wikipedia.org/wiki/Tree_traversal).<br><br>
traverse function은 Inorder 방식으로 BTree를 traverse하는 function입니다. Inorder traverse에 관한 정보는 [링크](https://ko.wikipedia.org/wiki/%ED%8A%B8%EB%A6%AC_%EC%88%9C%ED%9A%8C)를 참고해주시기 바랍니다.

---
4. function search<br>
search is a function that return node that has target key. serach is implemented by binary search method.<br><br>
search function은 BTree 내에 찾고자하는 key를 가지는 node가 존재할 경우, 그 node를 return합니다. search 방식은 binary search 방식을 이용해 구현되었습니다.

---
5. function insertElement<br>
insertElement is a function that insert target key to proper location that satisfies the definition of BTree. After insert, it reorganizes Tree by using balancing function to satisfy the definition of BTree.<br><Br>
insertElement function은 BTree의 정의를 만족하는 위치에 key를 삽입하는 function입니다. insert를 수행하고 난 뒤에는, balancing function을 통해 BTree의 정의를 만족하도록 Tree를 재구성합니다.

--- 
6. function balancing, splitChild<br>
balancing, splitChild are functions that reorganize nearby nodes from a node that has inserted key. They are executed during insertElement function.<br><br>
balancing, splitChild function은 insertElement function의 단순히 element를 삽입하는 시행 다음에 시행되며, BTree의 정의에 따라 node를 최적화된 위치로 재배치시키는 역할을 수행합니다.

---
7. function remove<br>
remove is a function that remove element of BTree. After running remove function, tree is reorganized by balancingAfterDel function to satisfy the definition of BTree.<br><br>
remove function은 BTree에 존재하는 element를 삭제할 때 사용하는 function입니다. remove를 수행하고 난 뒤에는, balancingAfterDel을 통해 BTree의 정의를 만족하도록 Tree를 재구성합니다.

---
8. function balancingAfterDel, borrowFromLeft, borrowFromRight, merge<br>
balancingAfterDel, borrowFromLeft, borrowFromRight, merge are functions that reorganize nearby nodes from a node that had deleted key. They are executed during remove function.<br><br>
balancingAfterDel, borrowFromLeft, borrowFromRight, merge function은 remove를 통해 key를 제거한 뒤 시행되며, BTree의 정의에 따라 node를 최적화된 위치로 재배치시키는 역할을 수행합니다.

#### Properties ####
Time complexity in big O notation <br>

Algorithm | Average | Worst case
|---|---|---|
| Space | O(n) | O(n) |
| Search | O(log n) | O(log n) |
| Insert | O(log n) | O(log n) |
| Delete | O(log n) | O(log n) |

###### Source: [Wikipedia](https://en.wikipedia.org/wiki/B-tree)
###### Source: [위키백과](https://ko.wikipedia.org/wiki/B_%ED%8A%B8%EB%A6%AC)
