
---

본 게시글은 강필성 교수님의 [다변량 데이터 분석 강의](https://www.youtube.com/watch?v=o9uEVxzFeR0&list=PLetSlH8YjIfWKLpMp-r6enJvnk6L93wz2&index=1)를 기반으로 작성되었습니다.

---

작성자 : KUBIG 17기 송지훈

# Chapter 3)  Logisitic Regression
---

## 3-1 Logistic Regression: Formulation

선형회귀로 어느 현상을 제대로 설명/표현할 수 없을 때 Logistic Regression 사용
<br/>

**[Classification Task]**
<br/>

Example: 참 거짓이 결과인 문제들에서는 선형회귀식의 왼쪽과 오른쪽의 범위가 불일치하여 문제 발생


$$ y = \beta_0 + \beta_1x_1 + \beta_2x_2 ... + \beta_dx_d + \epsilon $$

$$ \beta = coefficient \quad \epsilon = noise$$

* 좌변은 0 아니면 1만 나올 수 있는데 우변은 모든 실수가 나올 수 있다 
* 목표는 회귀 모델의 장점을 유지하는 분류 모델 만들기
<br/>

**[Goal]**

 설명 변수를 가지고 최종 결과가 0 아니면 1인 binary outcome이 되도록 하는 함수 찾기 
 * y의 logit 함수를 output으로 사용
 * logit을 사용하면 설명 변수들에 대한 선형 모형으로서 추정될 수 있음
 * logit은 어느 확률을 산출

<br/>

**[Odds]**

$$ odds = {p \over 1-p} $$

p = probability of success	

오즈의 범위는 0부터 ∞

**오즈의 단점**
* 0 < odds < ∞ (음수를 가질 수 없다)
* Asymmetric/비대칭

**단점 해결**

$$ log(odds) = log( {p \over 1-p}) $$

* -∞ < log(odds) < ∞ 
* Symmetric/대칭
* p 값이 작을 때 음수, p 값이 클 때 양수

<br/>

**[Logistic Regression Formula]**

$$ {p \over 1-p} = e^{\beta_0 + \beta_1x_1 + \beta_2x_2 ... + \beta_dx_d} $$

성공 확률:

$$ p = {1 \over 1 + e^{-(\beta_0 + \beta_1x_1 + \beta_2x_2 ... + \beta_dx_d)}} $$


## 3-2 Logisitic Regression: Learning


모델의 성능은 정답 범주에 속할 확률을 높게 산출해주는 것이 좋다

<br/>

**Likelihood Function**

Likelihood: 정답 클래스로 분류될 확률

* 모든 객체가 독립적으로 산출되었으면, dataset의 likelihood는 모든 객체의 likelihood의 곱이다
* log-likelihood도 일반적으로 사용된다
* likelihood, log-likelihood이 클수록 성능이 좋다
* Max likelihood = Max log(likelihood) = Min -log(likelihood)

<br/>

**Maximum likelihood estimation (MLE)**

데이터셋이 가지는 likelihood를 최대화하는 coefficient를 찾는 게 목표

$$ P(x_i, y_i | \beta) = \sigma(x_i | \beta) $$      $$   if y_i = 1$$

$$ P(x_i, y_i | \beta) = 1 - \sigma(x_i | \beta) $$      $$   if y_i = 0$$

yi가 0 아니면 1이므로 위 식을 다음과 같이 쓸 수 있다:

$$ P(x_i, y_i | \beta) = \sigma(x_i | \beta)^{y_i}(1 - \sigma(x_i | \beta))^{1-y_i} $$

<br/>

전체 데이터셋의 likelihood는 다음과 같이 표현:

$$ L(X,y|\beta) = \prod_{i=1}^N {P(x_i, y_i | \beta)} = \prod_{i=1}^N{\sigma(x_i | \beta)^{y_i}}(1 - \sigma(x_i | \beta))^{1-y_i} $$

로그를 하면:

$$ logL(X,y|\beta) = \sum_{i=1}^n y_i log(\sigma(x_i | \beta)) + (1-y_i)log((1 - \sigma(x_i | \beta)) $$

* 여기서 log likelihood는 beta와 비선형이기 때문에 explicit solution이 없다 
* 따라서, Gradient Descent 같은 최적화 알고리즘을 통해 최종 해를 찾아간다

**Gradient Descent**

log likelihood function을 미분하면서 gradient가 0이 될 때까지 weight(Beta Hat)값을 바꾸면서 시도

* 이때 weight를 기울기의 반대 방향으로 움직이면서 시도

* 베타 값을 최적화해서 찾은 뒤 성공 확률 계산은 다음 식으로 한다:
 

 ## Sigma 추가

$$ p = {1 \over {1 + e ^ {-(\beta_0 + \beta_1x_1 + \beta_2x_2 ... + \beta_dx_d)}}} $$

여기서 나오는 확률은 0에서 1 사이의 값인데 그럼 몇부터 어떤 클래스로 할당할 것인지 정하는 게 cut-off (threshold)이다
* 일반적으로 쓰는 cut-off는 0.5이지만 상황에 따라서 바꿀 수 있다

<br/>

## 3-3 Logisitic Regression: Interpretation

[Odds Ratio]

**Odds Ratio** input 변수가 1 증가할 때의 오즈 비율 

x가 한 단위 증가한다고 가정하자:

$$ {odds(x_1 + 1, ..., x_d)} \over {odds(x_1, ..., x_d)} $$

$$ = e ^ {\beta_0 + \beta_1(x_1+1) + \beta_2x_2 ... + \beta_dx_d} \over  e ^ {\beta_0 + \beta_1x_1 + \beta_2x_2 ... + \beta_dx_d} $$

* x<sub>1</sub>이 1 증가할 때, 오즈는 e<sup>β</sup><sup>^1</sup> 배만큼 증가 아니면 감소한다 
* β가 양수면 coefficient와 success class가 positively correlated = 성공 범주에 대한 가능성 증가
* β가 음수면 coefficient와 success class가 negatively correlated = 성공 범주에 대한 가능성 감소

<br/>

[Multinomial Logistic Regression]

1. baseline class를 만든다
2. baseline class를 분모로 하는 오즈에 대한 회귀식 여러 개 만든다
* class 1 vs class 3, class 1 vs class 2, class 2 vs class 3 --> 각 오즈에 대한 회귀식

K class가 있는데 k-1 만큼 모델링 하는 이유는 likelihood의 합이 1이므로 k-1 likelihood를 알면 마지막 클래스는 자동으로 계산 가능

## 3-4 Classification Performance Evaluation

모델 평가가 필요한 이유: 학습용 데이터만 학습을 잘하는 것이 아니라 새로운 데이터도 높은 예측을 할 수 있을지 평가

Validation Set을 통해서 파라미터값 최적화

Test set을 통해서 성능이 좋은 모델 찾기 

<br/>

**Confusion Matrix**

|        | Predicted |     |
|--------|-----------|-----|
| Actual | 1         | 0   |
| 1      | n11       | n10 |
| 0      | n01       | n00 |

|

Misclassification error =  $${n_{01} + n_{10}} \over {n_{11} + n_{10} + n_{01} +n_{00}} $$

Accuracy =  $${n_{11} + n_{00}} \over {n_{11} + n_{10} + n_{01} +n_{00}} $$ 

= 1 - Misclassification Error

Balanced correction rate (BCR) = $$ \sqrt { {n_{11} \over {n_{11} + n_{10}}}   * {n_{00} \over {n_{01} + n_{00} }   }  } $$
* BCR은 각 범주의 정확도를 따로 계산


Recall = $$ {n_{11} \over {n_{11} + n_{10}}} $$

Precision = $$ {n_{11} \over {n_{11} + n_{01}}} $$

F1- Measure = $$ {2 * Recall * Precision} \over {Recall + Precision} $$ 

* 위 metrics 들은 cut-off 기준에 따라 값이 다 달라진다 --> Cut off dependent


[Cut-off for classification]

분류 알고리즘은 각 class에 대한 likelihood를 확률, degree of evidence로 보여준다
* 여기서 분류 모델의 성능은 알고리즘의 cut-off에 높은 영향을 받는다
* 따라서, 모델 평가할 때 cut-off에 대해서 독립적인 지표 사용
* cut-off에 대해서 독립적이지 않으면 어느 모델을 다른 모델보다 좋게 보이게 만들 수 있다


**Receiver Opearting Characteristic Curve (ROC Curve)**

 AUROC = Area Under ROC Curve

 ROC Curve:
 * P(분류 클래스)를 내림차순으로 정렬
 * 모든 cut-off 기준에서 true positive rate와 false positive rate를 각각 계산
 * 계산한 값을 시각화*

 True positive rate = $${True Positive} \over {True Positive  + False Negative} $$

 False positive rate = $${False Positive} \over {False Positive  + True Negative} $$


 *true positive, false positive를 시각화한 뒤 ROC curve 아래의 넓이가 AUROC
 *AUROC가 1에 가까울수록 성능이 좋은 것 (ideal classifier), 0.5에 가까울수록 랜덤 분류 (random classifier)








