
---

본 게시글은 강필성 교수님의 [다변량 데이터 분석 강의](https://www.youtube.com/watch?v=o9uEVxzFeR0&list=PLetSlH8YjIfWKLpMp-r6enJvnk6L93wz2&index=1)를 기반으로 작성되었습니다.

---

작성자 : KUBIG 16기 최규빈

# Chapter 3) Logistic Regression
---

## 1) Formulation

**Logistic Regression**

일반적인 회귀분석 ->  y값이 연속형

logistic regression -> classification(분류)

$$ p = {1 \over 1 + e^{-(\beta_0 + \beta_1x_1 + \beta_2x_2 ... + \beta_dx_d)}} $$

<br/>

## 2) Learning
---

선형 회귀의 beta = closed form 존재

**Likelihood Function**

해당 task에서는 정답 class로 분류될 확률

* independent하게 산출된 데이터라면, entire dataset의 likelihood는 모든 likelihood의 곱연산

* likelihood(0~1)

* 주로 log likelihood 값 이용

<br/>

**Maximum likelihood estimation(MLE)**

dataset의 likelihood를 최대화하는 coefficient를 찾는다

* Max likelihood = Max log(likelihood) = Min -log(likelihood)

* 이진분류의 경우 0과 1을 지수로 취해 likelihood function을 1개로 통합 가능

$$ P(x_i, y_i | \beta) = \sigma(x_i | \beta)^{y_i}(1 - \sigma(x_i | \beta))^{1-y_i} $$

* independent할 경우 곱연산으로 변경

$$ L(X,y|\beta) = \prod_{i=1}^N {P(x_i, y_i | \beta)} = \prod_{i=1}^N{\sigma(x_i | \beta)^{y_i}}(1 - \sigma(x_i | \beta))^{1-y_i} $$

* 그렇게 계산한 likelihood function 의 product는 log를 취해 sum 연산으로 분리가능

$$ logL(X,y|\beta) = \sum_{i=1}^n y_i log(\sigma(x_i | \beta)) + (1-y_i)log((1 - \sigma(x_i | \beta)) $$

* likelihood는 beta에 비선형 -> explicit solution(명시적 해)존재하지 않으므로 trial error를 통해 optimization algorithm 사용

<br/>

**Gradient Descent**

log likelihood function의 gradient를 빼가며 미분값 0에 도달하면 중지

**threshold(cut-off)**

분류는 확률이 아니므로 cut-off를 정해준다

$$ p = {1 \over {1 + e ^ {-(\beta_0 + \beta_1x_1 + \beta_2x_2 ... + \beta_dx_d)}}} $$

일반적으로 0.5 이지만 이상치 탐지와 같은 상황에는 변화를 줌

<br/>

## 3) Interpretation
---
**Coefficients**

* Positive value: positively correlated with the success class

* Negative value: negatively correlated with the success class

* Linear regression의 경우 beta의 변화에 대한 직관적 이해 가능

* logistic regression의 경우 직관적 이해 불가능

**Odds ratio**

특정 x가 x+1이 되었을 때 변화율

$ {odds(x_1 + 1, ..., x_d)} \over {odds(x_1, ..., x_d)} $
$ = e ^ {\beta_0 + \beta_1(x_1+1) + \beta_2x_2 ... + \beta_dx_d} \over  e ^ {\beta_0 + \beta_1x_1 + \beta_2x_2 ... + \beta_dx_d} $
$ = e ^ {\beta_1} $

x1이 1 증가할때 오즈는 $ = e ^ {\beta_1} $에 비례해서 변화

* beta가 양수이면 성공 범주와 beta 간 양의 상관관계

* beta가 음수이면 성공 범주와 beta 간 음의 상관관계

**Geometric interpretation**

Hyper-plane이 원점을 기준으로 멀어질 수록 회귀식 p가 1에 가까워진다

<br/>

**Multinomial Logistic Regression**

여러 개의 클래스가 있는 경우의 logistic regression

* 하나의 class를 base line으로 설정

* 해당 base line에 대해 각 class의 odds를 각각 계산

* odds ratio 식을 통해 각 coefficient 계산 가능

<br/>

## 4) Classification Performance Evaluation
---

### Why evaluate?

Over-fitting을 예방하기 위해

**Multiple methods**

* Classification: Naive bayes, linear discriminant, k-nearest neighbor, classification trees

* Prediction: Multiple linear regresiion, neural networks, regression trees

* To choose best model, need to assess each model's performance

* validation data를 통해 parameter 설정

<br/>

**Confusion Matrix**

정오행렬 / 혼동행렬

Summarize the correct and incorrect classifications

* n11 = 1을 1로 예측

* n01 = 0을 1로 예측

* n10 = 1을 0으로 예측

* n00 = 0을 0으로 예측

 $$ \text { Misclassification error } =  {{n_{01} + n_{10}} \over {n_{11} + n_{10} + n_{01} +n_{00}}} $$

$$ \text { Accuracy } =   { {n_{11} + n_{00}} \over {n_{11} + n_{10} + n_{01} +n_{00}}} = 1 - Misclassification Error$$ 

**BCR**

Balanced Correction Rate

* 각 class 정확도를 기하평균해서 계산

$$ \text{ Balanced correction rate (BCR) } =  \sqrt { {n_{11} \over {n_{11} + n_{10}}} * {n_{00} \over {n_{01} + n_{00} } } } $$

$$ \text{ Recall } = {n_{11} \over {n_{11} + n_{10}}} $$

$$ \text{ Precision } = {n_{11} \over {n_{11} + n_{01}}} $$

$$ \text { F1- Measure } = { {2 * Recall * Precision} \over {Recall + Precision} } $$

* cut off에 따라 Confusion Matrix의 지표값들은 달라지므로 cut-off에 독립적인 모델 생성이 필요함

**ROC Curve**

Receiver Opearting Characteristic Curve 

* P(interesting class, 주로 불량)을 기반으로 분류

* True positive rate, false positive rate 계산

* Chart를 그려 표현

**AUROC**

Area Under ROC curve

* ROC curve의 under area

* 1 for the ideal classifier

* 0.5 for the random classifier

