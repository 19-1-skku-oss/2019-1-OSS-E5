# 연결 리스트(Linked List)
<br>
데이터와 다음 노드를 가리키는 변수로 구성된 노드를 이어 붙여서 리스트를 만든다.
<br>

**단순 연결 리스트(Singly_linked_list)**
<br>
단순 연결리스트는 가장 단순한 형태이다.  
두개의 변환된 형태이가 존재하지만 여기서는 한개의 코드만 썼다.

![단순](http://blogfiles.naver.net/20130422_250/charmdepp_1366629345614TORJS_PNG/%BF%F8%C7%FC%BF%AC%B0%E1%B8%AE%BD%BA%C6%AE.PNG)

<단순 연결 리스트 그림>


**원형 연결 리스트(Circular_linked_list)**
<br>
연결리스트의 마지막 노드의 next 값을 첫번째 노드를 가르키도록 하여 원형의 연결리스트를 만들수있다.
장점은 모든 노드에서 다른 모든 노드를 접근 할수 있게된다.
<br>
![원형 연결리스트](http://blogfiles.naver.net/20141226_7/jak500_1419542914792XPyKL_PNG/%BF%F8%C7%FC_%BF%AC%B0%E1_%B8%AE%BD%BA%C6%AE.png)

<원형 연결 리스트 그림>

**이중 연결 리스트(Doubly_linked_list)**
<br>
연결리스트의 마지막 노드의 변수(prev)를 더하여 next의 반대 방향으로도 추적가능하게 만든다.
원형리스트와 다른점은 [1,2,3,4,5,6,7,8,9] 가 있을때 current 가 5에있을때 4를 접근하기 위해  
5-->6-->7-->8-->9-->1-->2-->3-->4  
가 아니라  
5-->4 로 접근할수 있다.
<br>
![이중](http://blogfiles.naver.net/20151204_254/vsky712_1449191284011xgQvE_PNG/14.png)
<br>
<이중 연결리스트>

**이중 원형 연결 리스트(Doubly linked curcular list)**
<br>
이중리스트의 마지막 노드가 첫 노드랑 이어지게끔한다.
<br>
![이중원형](http://blogfiles.naver.net/20150419_207/kiminhovator_1429445388697rlBGX_PNG/%C0%CC%C1%DF_%BF%F8%C7%FC_%BF%AC%B0%E1%B8%AE%BD%BA%C6%AE.png)
<br>
<이중 원형 연결 리스트>
<br>
위에 설명했던 원형리스트와 이중연결리스트 모두의 장점을 가져올수 있다.
하지만 이 알고리즘을 사용하는것이 항상 가장 좋은것은 아니다.  
상황에따라 필요한 자료구조와 알고리즘을 선택할 수 있어야 한다.
