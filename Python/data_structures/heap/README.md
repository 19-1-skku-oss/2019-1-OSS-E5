# 힙(Heap)
힙(heap)은 최댓값 및 최솟값을 찾아내는 연산을 빠르게 하기 위해 고안된 완전이진트리(complete binary tree)를   
기본으로 한 자료구조(tree-based structure)이다. 그 방법론으로 힙은 이진 트리 형태로 윗쪽의 원소들이 아래쪽의  
원소보다 작은 형태로 저장한다.
아래 그림은 heap sort를 이용하여 원소를 Insert 할때 일어나는 상황을 그림으로 나타낸 것이다.

![HEAP 과정](https://postfiles.pstatic.net/20100429_287/hachn_12725103998110rYr7_png/heap_insert_hachn.png?type=w3)

힙은 일반 이진 트리에 비해 최대 최소를 찾는 시간복잡도가 줄어든다. 대신 Insert 할때의 시간은 조건문이 늘어남에 따라 늘어난다.

Source : [](https://blog.naver.com/hachn/103871306)
