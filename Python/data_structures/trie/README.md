# 트라이(Trie)

트라이는 문자열을 빠르게 검색할수 있도록 하는 트리이다.  
영어를 예로들면 알파벳 하나당 한계의 노드를 가지며 그 다음 알파벳은 그 자식노드에 저장된다.

[CAR,CARD,DESK,DESKTOP,DOOR] 를 담는 트라이 자료구조를 예로들면 아래 그림처럼 나타난다.

![TRIE 그림](https://cdn-images-1.medium.com/max/800/1*objieo3WOHHKcR8sa7_iqA.png)

<트라이(Trie) 그림>
<br>
여기서 CAR 를 검색하면 왼쪽노드로 이동하면 CAR을 세번만에 찾을수 있다.  
이처럼 트라이는 매우높은 검색 속도(낮은 시간 복잡도)를 가지고 있다. 반면에 메모리를 많이 사용(높은 공간복잡도)한다.
따라서 프로그래머는 사용 목적에 맞추어 trie를 변형하여 사용한다.