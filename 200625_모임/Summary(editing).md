## 3주차 내용 정리

1. binary search

   먼저 정렬을 한 뒤 중간을 기준점으로 타겟이 기준점보다 작으면 중간 위의 것들은 모두 없앰

   이후 과정을 반복하며 타겟값을  찾음.

   time complexity가 적다는 장점이 있음.

2. R just - 문자열 정렬 기능 제공

3. Itertools Counter - 리스트의 갯수를 센 뒤 해당 값을 딕셔너리로 제공.

4. itertools groupby - 연속적인 문자열끼리 묶어주는 기능-> 연속적인 문자열 갯수 세기에 간편함.

5. itertools combination/permutation 은 순열에 대한 간편한 기능을 제공하지만, time complexity가 커서 효율성 검사가 존재할때는 좋지 못함. -> 다른 방법을 생각해보자!

6. heap - 리스트 내부에 존재하는 최소값을 찾기 위한 방법으로, for 문 + sort 과정이 필요할때 heap + pop(0) 을 사용하면 시간 복잡도를 최소화 하며 리스트를 소팅 + 최소값 찾기 를 할 수 있음.
