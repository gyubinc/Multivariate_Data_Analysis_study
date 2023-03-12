
---

본 게시글은 강필성 교수님의 [다변량 데이터 분석 강의](https://www.youtube.com/watch?v=o9uEVxzFeR0&list=PLetSlH8YjIfWKLpMp-r6enJvnk6L93wz2&index=1)를 기반으로 작성되었습니다.

---

작성자 : KUBIG 16기 최규빈

# Chapter 1) Introduction to Multivariate
---

## Introduction to Data Science

**Data-driven Decision Making**

데이터를 기반으로, 객관적인 수치를 토대로 최적의 의사결정

<br/>

**What we want to know**

|word|description|
|:---:|---|
|Optimization|실행할 수 있는 최적이 무엇인가?|
|Predictive modeling|다음에는 무슨 일이 발생할 것인가?|
|Forecasting|현재의 트랜드가 계속될 것인가?|
|Statistical Analysis|왜 이번 일이 발생한 것인가?|
|Alerts|이 상황에 필요한 액션이 무엇인가?|
|Query drilldown|문제가 정확히 어디에 있는 것인가?|
|Ad hoc reports|얼마나 많이, 자주, 어디에서 발생한건가?|
|Standard reports|무슨 일이 일어난 것인가?|

* 위 -> 아래로 가면서 최적화, 예측, 설명의 단계

<br/>

**Analytics의 3가지 단계**

|Descriptive|Predictive|Prescriptive|
|:---:|:---:|:---:|
|설명|예측|최적화|

## Machine Learning

**Definition**

특정 task를 수행하기 위해 performance measure를 바탕으로 성능을 측정하며 경험으로부터 학습하여 지속적으로 개선되는 computer program

<br/>

**Supervised Learning**

지도학습

* 입력 **X**와 타겟 y 사이의 관계 y = f(x)를 찾는 것

<br/>

**Unsupervisesd Learning**

비지도학습

* 타겟 y가 없이 **X**로부터 얻을 수 있는 분포, 패턴을 찾는 것

<br/>

## Big Data

**4Vs**

Volume

* 방대한 데이터

Velocity

* 빠른 처리속도

Variety

* 원천이 다양해짐

Value

* 졍량적인 가치평가

## Data Mining

대량의 데이터로부터 유용한 결과물을 어떻게 뽑아낼 것인가

* meaningful patters, rules를 뽑아내자

## Artificial Intelligence

지능적 행위가 가능한 컴퓨터, 소프트웨어

* 방법론 + 행위의 결합

* 창의성을 기준으로 약인공지능 / 강인공지능 분리

<br/>

**연역적 논리**

A->B->C 의 형태로 symbolic 연산

<br/>

**귀납적 논리**

경험을 통해 학습(머신러닝 학습 방법)

## Data Science Applications

1. Visualization for intuitive understanding <br/>짧은 시간 내에 정보를 얻을 때 용이

2. Predict, Diagnosis, and Detection

3. Support decision making in everyday life <br/> (recommendation system)

## Multivariate Data Analysis in Data Science

**1**. Data Reduction/Structural Simplification

주어진 데이터들을 이용해 본질적인 *특징을 보존하며* 적은 차원의 데이터 셋으로 변환하는 것

* 해석 용이성 증가

* 주성분 분석

* 변수 축소 기법

* 중요한 변수를 찾아내는 것

<br/>

**2**. Sorting and Grouping

유사한 객체나 변수들을 묶어내는 것

* 군집간 차이를 판별

* 계층적 군집화

* K-means 군집화

<br/>

**3**. Investigation of the dependence among variables

변수들 간의 관계의 본질적 특성 평가

* Association Rule Mining

* Factor Analysis

<br/>

**4**. Prediction

목적을 가지고 하나의 변수를 다른 변수들의 관측치로부터 예측

* Discrimination and Classification

* Multivariate Linear Regression

<br/>

**5**. Hypothesis construction and testing

가설을 생성하고 검정하는 과정

* Inferences about a Mean Vector

* Comparisons of Several Multivariate Means

## Data Science Procedure

**1**. Ask an interesting question

* 풀고자 하는 문제가 무엇인가?

* 데이터를 이미 보유하고 있다면 무엇을 할 것인가?

* 무엇을 예측하고 추정하기를 원하는가?

<br/>

**2**. Get the data

* 데이터는 어떻게 샘플링할 것인가?

* 어떤 데이터와 정보가 우리 목표와 관련있는가?

* 프라이버시, 개인정보 이슈는 없는가

* data annotation : 데이터에 label을 달아주는 행위

<br/>

**3**. Explore the data

* 데이터의 속성과 구조 알아보기

* 데이터에 이상한 점은 없는가?

* 데이터에 대어떠한 패턴이 존재하는가?

<br/>

**4**. Model the data

* 모델 수립

* 모델 적합화

* 모델 검증

<br/>

**5**. Communicate and visualize the results

* 결과 요약 및 시사점 분석

* 결과가 타당한가?

* 스토리를 말할 수 있는가?