
---

본 게시글은 강필성 교수님의 [다변량 데이터 분석 강의](https://www.youtube.com/watch?v=o9uEVxzFeR0&list=PLetSlH8YjIfWKLpMp-r6enJvnk6L93wz2&index=1)를 기반으로 작성되었습니다.

---

작성자 : KUBIG 17기 송지훈

# Chapter 3)  Logisitic Regression
---

## 3-1 Logistic Regression: Formulation

선형회귀로 어느 현상을 제대로 설명/표현할 수 없을 때 Logisitic Regression 사용
<br/>

**[Classification Task]**
<br/>

Example: 참거짓이 결과인 문제들에서는 선형회귀 식의 왼쪽가 오른쪽의 범위가 불일치하여 문제 발생


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
$$ p = probability of success

오즈의 범위는 0부터 ∞

**오즈의 단점**
* 0 < odds < ∞ (음수를 가질 수 없다)
* Asymmetric/비대칭

**단점 해결**

$$ log(odds) = log( {p \over 1-p}) $$

* -∞ < log(odds) < ∞ 
* Symmetric/대칭
* p 값이 작을 때 음수, p 값이 클 때 양수*

<br/>

**[Logistic Regression Formula]**

$$ {p \over 1-p} = e^{\beta_0 + \beta_1x_1 + \beta_2x_2 ... + \beta_dx_d} $$

성공 확률:

$$ p = {1 \over 1 + e^{-(\beta_0 + \beta_1x_1 + \beta_2x_2 ... + \beta_dx_d)} $$


## 3-2 Logisitic Regression: Learning


모델의 성능은 정답 범주에 속할 확률을 높게 산출해주는 것이 좋다

<br/>

**Likelihood Function**

Likelihood: 정답 클래스로 분류될 확률

* 모든 객체들이 독립적으로 산출되었으면, dataset의 likelihood는 모든 객체들의 likelihood의 곱이다 
* log-likelihood도 일반적으로 사용된다 
* likelihood, log-likelihood이 클수록 성능이 좋다
* Max likelihood = Max log(likelihood) = Min -log(likelihood)

<br/>

**Maximum likelihood estimation (MLE)**

데이터셋이 가지는 likelihood를 최대화하는 coefficient을 찾는게 목표

$$ P(x_i, y_i | \beta) = \sigma(x_i | \beta) $$      $$   if y_i = 1$$

$$ P(x_i, y_i | \beta) = 1 - \sigma(x_i | \beta) $$      $$   if y_i = 0$$

yi가 0 아니면 1이므로 위 식을 다음과 같이 쓸 수 있다:

$$ P(x_i, y_i | \beta) = \sigma(x_i | \beta)^{y_i}(1 - \sigma(x_i | \beta))^{1-y_i} $$

<br/>

전체 데이터셋의 likelihood는 다음과 같이 표현:

$$ L(X,y|\beta) = \prod_{i=1}^N {P(x_i, y_i | \beta)} = \prod_{i=1}^N{\sigma(x_i | \beta)^{y_i}(1 - \sigma(x_i | \beta))^{1-y_i} $$

로그를 하면:

$$ logL(X,y|\beta) = y_i log(\sigma(x_i | \beta)) (1-y_i)log((1 - \sigma(x_i | \beta)) $$

* 여기서 log likelihood는 beta와 비선형이기 때문에 explicit solution이 없다 
* 따라서, Gradient Descent 같은 최적화 알고리즘을 통해 최종 해를 찾아 간다

**Gradient Descent**

log likelihood function을 미분하면서 gradient가 0이 될 때까지 weight(Beta Hat)값을 바꾸면서 시도
* 이때 weight를 기울기의 반대 방향으로 움직이면서 시도*

* 베타 값을 최적화해서 찾은 뒤 성공 확률 계산은 다음 식으로 한다:

$$ p = {1 \over {1 + e ^ {-(\beta_0 + \beta_1x_1 + \beta_2x_2 ... + \beta_dx_d)}} $$

여기서 나오는 확률은 0에서 1 사이의 값인데 그럼 몇부터 어떤 클래스로 할당할 것인지 정하는게 cut-off (threshold) 이다
* 일반적으로 쓰는 cut-off는 0.5이지만 상황에 따라서 바꿀 수 있다

<br/>

## 3-3 Logisitic Regression: Interpretation

설명변수 x가 1개

* Linear : y = f(x)가 선형임을 가정(직선)

* Non-linear : r = f(x)가 비선형임을 가정(곡선)

<br/>

## Multiple Regression Models

설명변수 x가 2개이상 존재

* Linear

* Non-linear

<br/>

**Linear Regression**

독립변수는 설명변수간 1차항의 결합으로 표현된다

* 설명변수가 3개 이상일 경우 hyper-plane의 형태

<br/>

**OLS**

Ordinary least square, 최소자승법

* actual taget value와 regression을 통해 추정된 값과의 squared difference를 최소화

* 행렬 벡터의 연산으로 표현

* $\hat{\beta} = (X^TX)^{-1}X^Ty$라는 명시적 solution 존재

**성립 조건**

* noise $\epsilon$ 은 정규분포를 따른다<br/>잔차에 대한 QQ Plot을 그려서 확인가능

* 데이터가 선형관계일 때

* 관측치들이 상호 독립적일 때

* Y의 변동성이 특정한 변수의 변화에 영향을 받지 않을 때 (homoskedasticity)<br/>Residual plot을 찍어본다

**Goodness of fit**

평가지표

**Sum-of-Squares Decomposition**






