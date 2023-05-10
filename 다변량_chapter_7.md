
---

본 게시글은 강필성 교수님의 [다변량 데이터 분석 강의](https://www.youtube.com/watch?v=o9uEVxzFeR0&list=PLetSlH8YjIfWKLpMp-r6enJvnk6L93wz2&index=1)를 기반으로 작성되었습니다.

---

# 7) Ensemble Learning Overview
---

**최고의 알고리즘이 있는가?**

각각의 데이터셋에 적합한 알고리즘은 정해져 있지 않다

## No Free Lunch Theorem

* 좋은 generalization performance를 위해서는 직접 적용해봐야 한다

## Motivation

만약 여러 모델들이 적절히 조합된다면 개별적 best 알고리즘보다 좋은 성능을 가질 수 있다

<br/>

## Theoretical Backgrounds: Bias-Variance Decomposition

$y = F^*(x) + \epsilon, \epsilon \sim N(0, \sigma^{2})$

* $F^*(x)$는 target function

* error는 i.i.d

각각의 예측 function F에 대해

$\bar{F}(x) = E[\hat{F_D}(x)]$

$Err(x_0) = Bias^2(\hat{F}(x_0)) + Var(\hat{F}(x_0)) + \sigma^2$

**Bias**

average estimator와 truth 사이의 차이

**Variance**

spread of the individual estimations

<br/>

## Purpose of Ensemble

**Goal**

Reduce the error through constructin gmultiple learners to

1. Reduce the variance : Bagging, Random Forests

2. Reduce the bias : AdaBoost, GBM

3. Both : Mixture of experts

<br/>

## Ensemble Diversity

**Key**

1. 앙상블에 사용하는 모델의 다양성(매우 중요)

* Ensemble에 동일한 모델을 사용하는 것은 의미가 없다

* 또한, 각각의 모델들은 어느정도 준수한 성능이 보장되어야 한다

2. 어떻게 결합할 것인가

## 방식

## Independent(implicit)

독립적으로 만든 모델을 사용

* 모델 의존성 X

* 병렬화 가능

## Model guided(explicit)

순차적으로 모델 사용

<br/>

## Theoretical Backgrounds : Why Ensemble

$y_m(x) = f(x) + \epsilon_m(x)$

$E_x[\{y_m(x) - f(x)\}^2] = E_x[\epsilon_m(x)^2]$

The average error made by M individual models vs Expected error of the ensemble

$E_{Ensemble} = \frac{1}{M}E_{Avg}$

* 가정 : error term 이  zero mean, uncorrelated

* In reality, by the Cauchy's inequality

$E_{Ensemble} \leq E_{Avg}$

---

# 1. Aggregating

## Sampling without Replacement

**K-fold data split**

데이터를 k개의 block으로 분할한 후 k-1 개의 block으로 학습을 진행하며 총 k개의 서로 다른 모델을 만든 후 앙상블(Aggregation)

* 이렇게 학습 할 경우 최대 k-2개의 block을 데이터로 공유하는 모델이 존재함

* error term의 i.i.d는 만족하지 않지만 E(e)는 0, 따라서 각각의 Error보다는 작거나 같음

* 잘 사용하지는 않음

<br/>

# Bootstrap Aggregating : Bagging

## Main Idea

랜덤 복원 추출(Random sampling with replacement)을 통해 original 데이터 셋과 개수는 똑같지만 데이터는 다른 Bootstrap 생성(중복된 데이터 존재)

* 약간 변형된 분포를 가지는 데이터셋들을 생성

* 그렇게 생성된 각 모델의 예측 값들을 aggregating하여 prediction

* Bias는 작지만 Variance는 큰, 즉 complexity가 큰 모델에 주로 사용

* 어떠한 형태의 알고리즘에도 적용 가능

## Result Aggregating

**Majority voting**

$\hat{y}Ensemble = argmax_i(\displaystyle\sum_{j=1}^{n}\delta(\hat{y_j = i}), i\in \{0,1\})$

다수결, 가장 많이 나오는 Predicted class label로 선택

**Weighted voting**

각 label에 해당하는 probability의 합이 더 큰 label 선택

**Stacking**

예측된 결과물을 입력으로 받아 예측하는 Meta-Classifier 생성

* Input : Predictions made by ensemble members

* Target : Actual true label

**Out of bag error(OOB Error)**

Bagging은 복원 추출이기 때문에 각 모델의 validation set은 선택되지 않은 OOB data를 validation set으로 사용한다

---

# 2. Random Forests

Decision tree algorithms(의사결정나무)을 위한 bagging 기법

**Two ways to increase the diversity of ensemble**

1. Bagging

2. Randomly chosen predictor variables

## Algorithm

1. Bootstrap(Sample with replacement)

2. p variables 중 m개의 variables에 대해서만 분리하는 Decision tree 구성 후 tree 형태로 연결

* ex) 25 dimensions 중 Randomly selected variables 10 dimension에 대해서만 모델 구성

**Generalization Error**

pruning이 되지 않아 각 tree는 over-fitting

충분한 population size가 보장된다면,

$Generalization Error \leq \frac{\bar{\rho(1-s^2)}}{s^2}$

$\bar {\rho}$ = mean value of the correlation coefficients between individual trees

$s^2$ = margin function

**Variable Importance**

1. Compute the OOB error for the original dataset (e)

2. Compute the OOB error for the dataset in which the variable x is permuted (p)

3. Compute the variable importance based on the mean and standard deviation of (p-e) over all trees in the population

즉, 변수의 중요도를 계산할 수 있다

**변수의 중요도가 높다면**

1. Random permutation 전-후의 OOB Error 차이가 크게 나타남

2. 그 차이의 편차가 적어야 함
