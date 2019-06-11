# 트리

**트리란?**
<br>
트리 회로. 나무가 하나의 뿌리(root)에서 줄기(trunk)가 나와 가지(branch)로 나누어지는 것처럼, 어떤 하나의 집합(레코드나 디렉토리 등)으로부터 하위 레벨(lower level)로 가지가 나오는 집합 관계를 갖는 계층 구조(hierarchic structure)를 말한다.
<br>
![트리의 구조](https://dthumb-phinf.pstatic.net/?src=%22https%3A%2F%2Fdbscthumb-phinf.pstatic.net%2F0805_000_1%2F20111121125604990_2MOOUFZIZ.jpg%2FT1137_i1.jpg%3Ftype%3Dm4500_4500_fst_n%26wm%3DY%22&twidth=520&theight=366&opts=17)
<br>
<트리의 구조>

Source : [네이버 지식백과](https://terms.naver.com/entry.nhn?docId=840166&cid=42344&categoryId=42344)

대표적인 일반 트리에는 가계도가 있다.([family tree](https://github.com/19-1-skku-oss/2019-1-OSS-E5/blob/master/Python/data_structures/tree/family%20tree.py))

**이진트리**
<br>
이진트리는 자식노드가 두개 이하인것을 말하며, 완전 이진트리는 자식노드가 2개아니면 0개인 트리이다. 이진트리는 데이터를 반으로 쪼개어 트리형식으로 저장한다는 점에서 다양한 형태로 활용되고 있다.
세부적인 내용은 [binary tree 폴더안 README.md](https://github.com/19-1-skku-oss/2019-1-OSS-E5/blob/master/Python/data_structures/tree/binary%20tree/README.md) 를 읽기를 바란다.

**트라이(Trie)**
<br>
트라이는 문자열을 빠르게 검색할수 있도록 하는 트리이다.  
영어를 예로들면 알파벳 하나당 한계의 노드를 가지며 그 다음 알파벳은 그 자식노드에 저장된다.

[CAR,CARD,DESK,DESKTOP,DOOR] 를 담는 트라이 자료구조를 예로들면 아래 그림처럼 나타난다.

![TRIE 그림](https://cdn-images-1.medium.com/max/800/1*objieo3WOHHKcR8sa7_iqA.png)
<br>


자세한 내용은 [Trie.py 설명 링크](https://github.com/19-1-skku-oss/2019-1-OSS-E5/blob/master/Python/data_structures/trie/README.md)를 사용하길 바란다.
