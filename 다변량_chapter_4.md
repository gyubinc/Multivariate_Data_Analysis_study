
---

본 게시글은 강필성 교수님의 [다변량 데이터 분석 강의](https://www.youtube.com/watch?v=o9uEVxzFeR0&list=PLetSlH8YjIfWKLpMp-r6enJvnk6L93wz2&index=1)를 기반으로 작성되었습니다.

---

# 4) Dimensionality Reduction
---

## 1) Dimensionality Reduction

**Data Analytics Process**

데이터 확보 - 전처리 - 학습 - 평가

확보한 데이터 X의 차원 d가 너무 많아서 학습이 잘 안될 때

성능은 저하시키지 않으며 적은 차원 d' 으로 축소

모델링의 효율성 추구

**High-dimensional Data**

**Examples**

* Document classification (BOW, Bag of Words 과도화 문제)

* REcommendation systems

* Clustering gene expression profiles

* 제조 공정 데이터 (이상치 탐지)

## Overview

**Curse of dimensionality**

변수가 늘어날 때 동일한 설명력을 갖기 위해서는 기하급수적으로 많은 수의 객체가 필요함

```
If there are various logical ways to explain a certain phenomenon, the simplest is the best
- Occam's Razor
```

**Intrinsic dimension(내재적 차원)**

실제로 우리가 가지고 있는 original dimension 보다 내재적 차원은 낮을 확률이 높다

**Problems caused by high-himensionality**

* 변수의 개수가 많아질수록 noise 증가

* Increase computational burden

* Require more number of examples to secure generalization ability

**To resolve the curse of dimensionality**

* Utilize domain knowledge

* Use a regularization term in objective function

* Employ a quantitative reduction technique

**Backgrounds**

* 변수의 수가 증가하면 model performance 증가(독립인 경우에만 성립)

**Supervised vs Unsupervised Dimensionality Reduction**

feedback 여부에 따라 분리

## 2) Variable Selection Methods

변수 선택 : 예측 모형의 외부에서 독립적인 매커니즘을 통해 선택

**Exhaustive search(전역 탐색)**

* Search all possible combinations

* Performance criteria for variable selection<br/>AIC, BIC, Adjusted R^2, Mallow's Cp...

* 변수가 조금만 늘어나도 불가능

**Forward selection**

변수를 선택하지 않고 가장 중요하다고 생각되는 변수들이 순차적으로 추가되는 방식

* 한 번 추가된 변수는 삭제되지 않는다

* 1개의 변수로 전부 돌려보고 돌릴 때마다 가장 좋은 변수 추가

* 변수의 추가가 더이상 성능향상에 유의미하지 않을 때 중지

**Backward Elimination**

Forward selection의 정반대

* 모든 변수를 포함한 모델에서 1개씩 제외해나가는 방식

* 모든 변수에 대해 특정 변수를 빼는 순간 성능의 저하가 급격히 일어난다면 중지

**Stepwise Selection**

forward selection과 backward elimination의 조합

* Takes longer time but has more chances to find the optimal set of variables

* 선택이나 제거된 변수들이 다시 후보군에 들어갈 수 있음

* 전진선택 한번, 후방소거 한번 반복하며 설정

## Performance Metrics

**Akaike Information Criteria(AIC)**

Sum of squared error(SSE) with the number of variables as a penalty term

* 같은 변수의 개수이면 performance 향상, 같은 performance라면 변수의 개수 감소할수록 성능 증가

**Bayesian Information Criteria(BIC)**

SSE, number of variables, standard deviation obtained by the model with all variables

**Adjusted R^2**

## Genetic Algorithm

진화를 모사한 알고리즘, Stepwise Selection에서 조금 더 시간을 들여 성능 향상

* Meta-Heuristic Approach

* Selection, Crossover, Mutation 활용

**Genetic Algorithm for Feature Selection**

1. Initialization

* Encoding Chromosomes(Gene의 원핫 인코딩)

* Parameter Initialization(population, fitness function, crossover mechanism, mutation rate, stopping criteria)

<br/>

2. Fitness Evaluation

* chromosomes 평가 지표

<br/>

3. Selection

* 우수한 일부만을 추출

* Deterministic selection(상위 선택), Probabilistic selection(높은 비율만큼의 확률로 선택)

<br/>

4. Crossover & Mutation

* Crossover(random)

* Mutation(local optimum 탈출)

<br/>

5. Find the Best Solution

* iteration을 반복하며 best chromosomes 선택

<br/>

## 3) Shrinkage Methods

알고리즘의 목적 함수에 같은 값이면 적은 개수의 변수 사용

**Multiple Linear Regression**

* 목적함수: OLE(Ordinary Least Square, 최소자승법)

**Logistic Regression**

## Shrinkage Methods

**Ridge Regerssion**

coefficient의 제곱합(L2 norm)을 패널티화

* 변수간 상관관계가 높을 때 잘 작동

**Lasso**

Least Absolute Shrinkage and Selection operator

coefficient의 절대값의 합(L1 norm)을 패널티화

* 변수의 coefficient가 0이 될 수 있어 변수 선택 가능

**Elastic net**

Ridge + Lasso

