## 복잡도 분석

- 시간복잡도 : O(N* KlogK)\
  문자열 리스트의 길이 N, 문자열의 평균 길이 k\
  문자열을 정렬하고 키를 만드는 과정 KlogK가 N번 발생한다.
  


## 요구 조건 분석
- 전체 리스트의 길이는 10000 이하
- 한 문자열의 크기는 100이하

## 문제 해결 흐름
1. 한 문자를 정렬한 뒤에 이를 키로 하는 리스트 디폴트 딕셔너리에 넣는다.
2. 딕셔너리의 벨류를 리스트로 만들어 리턴

## 핵심 알고리즘
1. 디폴트 딕셔너리
   - 같은 키 값을 갖는 벨류들을 리스트에 추가한다. (해쉬의 콜리전을 리스트로 해결하는것과 유사)