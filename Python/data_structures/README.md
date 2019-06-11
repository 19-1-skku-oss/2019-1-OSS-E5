# Data structure

**'자료구조' :**<br>
알고리즘을 공부하는데 단연컨데 자료구조는 필수적이다. 자료구조를 일상에 비유하자면 상자이다. 
왜냐하면 수 많은 물건들(Data)을 상자에 담아서 관리한다면 효율적으로 사용할 수 있기 때문이다.

**<자료구조의 특징>**<br>
이러한 자료구조를 사용하는 이유는 자료구조가 효율성(efficiency)과 추상화(efficiency) 그리고 재사용성(reusability)의 특징을 가지고 있다.
(1) 효율성(efficiency)

자료를 구조화하여 사용함으로써 조금 더 효율적으로 알고리즘을 구성할 수 있다. 자료에 대한 알고리즘을 사용하는 데 있어 자료를 구조화하여 사용함으로써 최악의 경우(처리시간, 처리하는 기억 용량) 등을 고려하여 알맞은 알고리즘을 선택하여 사용할 수 있다.

(2) 추상화(abstraction)

자료를 구조화하는 데 있어 자료를 표현하고 조작하는 방법을 추상화하여 사용함으로써 프로그램의 의존적 상황을 탈피할 수 있다. 그래서 다양한 프로그램 언어 사용이 가능하며, 어떻게 구현할 것인가가 아닌 어디에 어떻게 사용할 것인가에 대해 초점을 두게 된다.

(3) 재사용성(reusability)

자료구조는 모듈화 되어 있고 문맥에 자유롭기 때문에 재사용이 가능하다. 문맥에 자유롭기 때문에 다양한 자료에 상황에 따라 다양하게 사용할 수 있고, 규정된 자료구조를 모듈화하여 사용함으로써 다양한 프로그램에서 재사용할 수 있도록 접근해야한다.

Source: [네이버 지식백과](https://terms.naver.com/entry.nhn?docId=2073345&cid=44414&categoryId=44414)


# 자료구조의 종류

**연결 리스트(Linked List)**
- 단순 연결 리스트
- 양방향 연결 리스트
- 단순 원형 연결 리스트
- 양방향 원형 연결 리스트


**큐(Queue)**
- 큐
- 원형 큐
- 우선순위 큐
- 덱

**스택(Stack)**<br>
- 기본 스택
- Infix (related with tree) 
- Postfix (related with tree)

**트리(tree)**
1. 일반 트리
- 가계도 트리
- 트라이 구조
2. 이진트리
- 이진트리
- 탐색 트리
- AVL 트리
- 세그먼트 트리
- 세그멘트 트리(lazy)
- 팬윅 트리

**그래프(Graph)**
1. 탐색법
- BFS
- DFS

**해쉬(Hash)**
- 테이블
- 해쉬
- 확장 해쉬

**힙(Heap)**
- 힙의 사용

# 자료구조 설명

**연결 리스트(Linked List)** <br>
다른 자료구조를 공부하는데 기본이 된다. 따라서 가장 먼저 공부하는 것을 권장한다. 연결리스트는 연결 리스트는 각 데이터들을 포인터로 연결하여 관리하는 구조다. 연결 리스트에서는 노드라는 새로운 개념이 나오는데, 각 노드는 데이터를 저장하는 데이터 영역과 다음 데이터가 저장된 노드를 가리키는 포인터 영역으로 구성된다.

![노드의 구조](https://dbscthumb-phinf.pstatic.net/3523_000_1/20141020113246729_417K1H83I.jpg/ka7_111_i1.jpg?type=w107_fst&wm=N) <br>

<노드의 구조>

![연결리스트의 구조](https://dbscthumb-phinf.pstatic.net/3523_000_1/20141020113253165_UZ3S6YSCP.jpg/ka7_111_i6.jpg?type=w492_fst_n&wm=Y)<br>

<연결리스트의 구조> <br>
Source : [네이버지식백과](https://terms.naver.com/entry.nhn?docId=2270421&cid=51173&categoryId=51173)


**큐(Queue)**<br>
큐(queue)는 리스트의 한 쪽 끝에서는 자료가 삽입되고 다른 한 쪽에서는 자료가 삭제되는 구조를 말한다. 쉽게 말해서, 가장 먼저 보관한 자료부터 먼저 꺼내는 구조이다. 이를 FIFO라고 하는데 Fitst In First Out 이라는 뜻이다. 자료의 삽입이 일어나는 곳을 rear, 삭제가 일어나는 곳을 front 라고 부른다.

![큐의 자료구조](http://blogfiles.naver.net/20140212_111/4717010_13921672692581ENDc_GIF/queues1.gif)
<br>
<큐의 구조>

Source : [네이버 지식백과](https://terms.naver.com/entry.nhn?docId=3607509&cid=58598&categoryId=59316)

**스택(Stack)**<br>
스택(Stack)는 병안에 구슬을 넣는 것과 비슷하다. 오직 꼭대기(Top) 만을 추적하여 아래를 연결리스트로 이어주는 자료구조이다. 이는 나중에 다른 자료구조들을 사용하는데 기반이 되기도 한다(Ex. 계산기 만들기). 꼭대기로 넣고 빼고를 반복하기 때문에 가장 마지막에 들어간 노드가 가장 먼저나온다. 이를 LIFO 라고 하는데 Last In First Out 이라는 뜻이다. 

![스택](http://blogfiles.naver.net/20160710_69/kkhipp_1468122289760bUGmu_JPEG/%BD%BD%B6%F3%C0%CC%B5%E518.JPG)

**트리(tree)**
<br>
트리 회로. 나무가 하나의 뿌리(root)에서 줄기(trunk)가 나와 가지(branch)로 나누어지는 것처럼, 어떤 하나의 집합(레코드나 디렉토리 등)으로부터 하위 레벨(lower level)로 가지가 나오는 집합 관계를 갖는 계층 구조(hierarchic structure)를 말한다.
<br>
![트리의 구조](https://dthumb-phinf.pstatic.net/?src=%22https%3A%2F%2Fdbscthumb-phinf.pstatic.net%2F0805_000_1%2F20111121125604990_2MOOUFZIZ.jpg%2FT1137_i1.jpg%3Ftype%3Dm4500_4500_fst_n%26wm%3DY%22&twidth=520&theight=366&opts=17)
<br>
<트리의 구조>

Source : [네이버 지식백과](https://terms.naver.com/entry.nhn?docId=840166&cid=42344&categoryId=42344)


**그래프(Graph)**
<br>
그래프란 비선형(non-linear) 자료구조이며 노드(node)와 엣지(edge)로 구성되어 있습니다.
노드(Node)는 꼭짓점(vertex)으로 표현됩니다. 엣지(Edge)는 두 노드를 연결하는 선(line)으로 표현됩니다.
일상 생활에서 가장흔히 보는 그래프는 지하철 노선도이다.
<br>
![그래프의 그림](http://cafefiles.naver.net/data26/2007/9/16/222/%B1%D7%B7%A1%C7%C1_%BF%B9_mskyt.jpg)

<그래프 그림>

Source : [열코의 프로그래밍 일기](https://yeolco.tistory.com/66)

**해시(Hash)**
<br>
해시 테이블 알고리즘은 데이터를 담을 테이블을 미리 크게 확보해 놓은 후, 입력받은 데이터를 해시하여 테이블 내의 주소를 계산하고, 이 주소에 데이터를 담는 것이다. 성능이 좋은 탐색 알고리즘이다. 해시 테이블의 성능은 공간을 대가로 주고 얻어낸 것이다.

![해시 테이블](https://t1.daumcdn.net/cfile/tistory/1330FB335027FA4620)

<해쉬 그림>

Source : [해쉬 관련 설명](https://luyin.tistory.com/191)

**힙(Heap)**
<br>
힙(heap)은 최댓값 및 최솟값을 찾아내는 연산을 빠르게 하기 위해 고안된 완전이진트리(complete binary tree)를 기본으로 한 자료구조(tree-based structure) 이다.

![Heap](https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Max-Heap.svg/1024px-Max-Heap.svg.png)

<힙 그림>

그림을 간단히 설명하자면 root 인 100 을 기준으로 작은것은 left 큰것은 right로 가게 끔하여 정렬된 이진트리를 얻는것이다. 이런 트리를 얻기위해서는 insert시 대소비교를 통해 원하는 위치에 값을 넣어준다.
