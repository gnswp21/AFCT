### 링크
https://leetcode.com/problems/most-common-word/


```
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        import re, collections

        words = [word for word in re.sub("[^\w]", " ", paragraph)
        .lower().split() if word not in banned]
        counts = collections.Counter(words)
        return counts.most_common(1)[0][0]


```
## 복잡도 분석

1. 시간 복잡도 O(N)\
  리스트 컴프리핸션에서 sub나 lower()는 O(N)의 시간 복잡도가 발생한다.

## 요구 조건 분석

- n의 크기는 최대 1000

## 문제 해결 흐름
1. 조건에 맞지 않는 문자열 전처리
2. 콜렉션즈의 카운터 클래스 사용하여 가장 많이 나온 단어 찾기

## 핵심 알고리즘
- 전처리에서 활용 
  - lower()
  - re.sub()
  - in 연산자 
- 카운터 클래스
  - 내장 라이브러리 collections의 한 클래스
  - 빈도수 확인, 탐색에 탁월
