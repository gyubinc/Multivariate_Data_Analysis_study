
---

본 게시글은 강필성 교수님의 [다변량 데이터 분석 강의](https://www.youtube.com/watch?v=o9uEVxzFeR0&list=PLetSlH8YjIfWKLpMp-r6enJvnk6L93wz2&index=1)를 기반으로 작성되었습니다.

---

# 5) Decision Tree
---

Decision Tree(의사결정 나무)는 분류와 회귀가 모두 가능한 모델이다.

**왜 Classifier의 종류는 다양할까?**

We cannot guarantee that a single classifier is always better than the others

* Decision Tree

* Logistic Regression

* Random Forest

* SVM

* Neural Network

## 1) Classification Tree

**목적**

* 변수들의 조합을 통해 분류 규칙을 생성

* output = set of rules

**Tree**

최상단 노드(Root Node)부터 최하단 노드(leaf Node)까지의 모임

## 강점

**예측 결과물에 대해 사람의 언어로 설명 가능**

**용어**

* Parent Node: 분기 전 노드

* Child Node: 분기 후 노드

* Root Node: child node만 존재하는 node

* Leaf Node: parent node만 존재하는 node

* Split criterion: 자식 노드로 분리되는 기준

## Why Cart?

Cart(Classification and Regression Tree)

* 이해와 해석이 쉽다

* 데이터 전처리 불필요(현실적 유용성 높다)

* numerical data와 categorical data 모두 handling 가능

**다른 종류의 Decision Tree**

* CHAID(Chi-squared Automatic Interaction Detection)

* C4.5, C5.0

**Key Ideas**

Recursive Partitioning

* 부모로부터 자식으로 분기

Pruning the Tree

* 가지치기를 통해 간결하게 표현

**Recursive Partitioning**

Maximize the purity of the child nodes

**불순도 측정(Impurity Measuer)**

1. Gini Index

$$I(A) = 1 - \displaystyle\sum_{k=1}^{m} p^2_k$$

p = proportion of cases in rectangle A that belong to class k

* I(A) = 0, 모든 case가 same class일 경우

* Max value=0.5 in binary case

**영역이 여러개일 경우**

해당 영역개수 / 전체 영역의 개수 $R_i$를 곱한 후 더해서 계산

**Information gain**

분기 전 Gini Index - 분기 후 Gini Index

* Information gain이 가장 큰 split 기준을 찾아서 영역을 분할

2. Deviance

$$D_i = -2\displaystyle\sum_{k}^{}n_{ik}log(p_{ik})$$

i = node index, k = class index, $p_{ik} = probability of class k in node i$

$n_{ik}$ = i번째 영역에 해당하는 k class 범주의 수

* Deviance = 0, 모든 객체가 하나의 class에 속할 때

**Information gain**

분기 전 Deviance - 분기 후 Deviance

* Gini index와 동일하게 클 수록 좋음

**Classification Tree는 각 축에 수직으로 선을 그어 나눈다**

* 설명력 확보에 유리

1. 특정 변수에 대해 정렬

2. 모든 변수, 모든 point를 기준으로 split해보며 information gain이 가장 높은 최적의 split point 확정

3. 해당 과정을 영역마다 반복(정량적으로 계산, 한 변수가 계속 나뉠 수도 있음)

4. 더이상 분기할 수없는 impurity 0인 영역은 leaf node로 종료

5. full tree가 되면 전체 과정 종료

## Pruning

noise까지 모두 학습한 full tree가 항상 좋은 것은 아님

* overfitting의 risk를 가지고 있음

* poor generalization ability

tree 단순화가 필요함

**post-pruning**

full tree 완성 후 뒤로 돌아오는 방식

**pre-pruning**

tree를 split하다가 일정 지점에서 멈추는 방식

* 원래 post-pruning이 원조이지만, 현재는 pre-pruning이 더 효율적

**Cost complexity(비용 복잡도)**

leaf node 들을 병합할 때 사용하는 기준

$$CC(T) = Err(T) + \alpha  L(T) $$

CC(T) = cost complexity of a tree

ERR(T) = proportion of misclassified records in the validation data

Alpha = penalty factor attached to the tree size(set by the user)

L(T) = number of leaf node

* 같은 error rate라면 leaf node가 적은 단순한 tree 선택

* 복잡도가 같다면 error rate가 낮은 tree 선택

**pruning tree의 classification**

기존 Full tree의 경우 확률이 존재하지 않지만 pruning tree의 경우 해당 class에서 가장 많은 종류의 class를 선택하고 해당 class일 확률을 P(해당 class 개수 / 영역 내 전체 node 개수)로 표현

* 실제 활용 시 완성된 rule을 이용해 분류

## 2) Regression Tree

regression tree의 예측값 = 해당 영역의 종속변수들 간의 평균

* 계단 식의 형태로 함수 형성

## Impurity

Classification Tree와의 차이점

평균과의 차이를 통해 Impurity 계산

Sum of squared error(SSE: $\displaystyle\sum_{i=1}^{n}(y_i - \hat{y})^2$)

SSE(Parent) = 300, SSE(Left) = 10, SSE(Right) = 40, Gain = 250

## 3) Summary

## CART

**Advantages**

* 직관적 이해가 쉽다

* 이해와 활용이 쉬운 rule을 생성할 수 있다

**Disadvantages**

* horizontal, vertical split만 가능하다

* 변수간 interaction을 찾을 수 없다.(한 번에 한 변수만 선택)

