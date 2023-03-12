
---

본 게시글은 강필성 교수님의 [다변량 데이터 분석 강의](https://www.youtube.com/watch?v=o9uEVxzFeR0&list=PLetSlH8YjIfWKLpMp-r6enJvnk6L93wz2&index=1)를 기반으로 작성되었습니다.

---

작성자 : KUBIG 16기 최규빈

# Chapter 2) Multiple Linear Regression
---

## Example

차량의 가격을 어떻게 예측할 수 있을까?

<br/>

**Variable(X)**

* Age, Color, Door, Weight, HP, KM...

<br/>

**Target(y)**

* Price

<br/>

**Goal**

정량적인 종속변수 Y와 여러 개의 설명변수 X 사이의 linear relationship을 찾는 것

* Multiple은 p개의 설명변수가 존재한다는 의미

* Regression은 y가 실수값이라는 의미

* Linear은 y와 x 사이의 관계가 선형이라는 의미

$$ y = \beta_0 + \beta_1x_1 + \beta_2x_2 ... + \beta_dx_d + \epsilon $$

$$ \beta = coefficient \quad \epsilon = noise$$

<br/>

**Explanatory Regression**

설명적 회귀분석

* 설명변수(X)와 종속변수(y)간의 관계를 설명하는 데에 초점

* $R^2$을 통해 'goodness of fit' 측정

* $\beta$를 얼마나 잘 찾아냈는가

<br/>

**Predictive Regression**

* 새로운 X 데이터가 주어졌을 때 얼마나 y값을 잘 예측하는가에 초점

* predictive accuracy를 최적화

* y를 얼마나 잘 예측하는가

<br/>

## Simple Regression Models

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







