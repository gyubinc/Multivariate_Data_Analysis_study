
---

본 게시글은 강필성 교수님의 [다변량 데이터 분석 강의](https://www.youtube.com/watch?v=o9uEVxzFeR0&list=PLetSlH8YjIfWKLpMp-r6enJvnk6L93wz2&index=1)를 기반으로 작성되었습니다.

---

# 6) Artificial Neural Networks
---

## Perceptron

<br/>

**Brain Structure**

인간의 뇌는 뉴런 사이의 전기신호를 통해 메시지를 전달

* 여러 뉴런으로부터 신호를 받아 다른 뉴런으로 보내는 형식

사람의 뇌를 모사해서 컴퓨터에 표현하자!

<br/>

## Perceptron

An organism with only 1 neuron

<img src='https://github.com/gyubinc/Multivariate_Data_Analysis_study/blob/7ef41087bbab0e1b2752ad6e0989da21c7ff1623/image_folder/6_2.png'/>

$x_0$ = 상수

$x_1, x_2$ = 변수

$w_0, w_1, w_2$ = 가중치(학습 대상)

$h$ = 활성화함수

$y$ = 추정치

$t$ = 실제값(target)

$L$ = loss function

<br/>

## 진행 과정

**전반부**

가중치와 변수를 곱한 후 더해 스칼라 값으로 만들어 줌

**후반부**

해당 값을 활성화 함수에 통과시켜 변환 후 넘겨줌

* Perceptron의 핵심

* 비선형(non-linear)을 거쳐야만 함

<br/>

## Perceptron의 관점

**Input node**

Input variables

* $x_0, x_1, x_2$ 각각을 Input node, 전체를 layer로 표현

**Hidden node**

Take the weighted sum of input values and perform a non-linear activation

* 여러 변수들의 정보를 가중합으로 더한 후 다음 단계로 전달할 양을 정함

**Role of activation**

previous layer의 정보들이 다음 단계로 넘길 때 전달할 양을 결정해준다

* non-linaer function을 사용하는 순간 다중선형회귀와 일치하게 됨

<br/>

## 활성화 함수의 종류

<img src ='https://github.com/gyubinc/Multivariate_Data_Analysis_study/blob/61936a4d06e626a721689963172e7d51e8cdd315/image_folder/6_3.png'>

1. Sigmoid

Logistic / Logit 함수라고도 표현

* [0, 1]의 range, 학습속도가 느림

* 미분 시 0에 가깝게 나올 수 있음

2. Tanh

* [-1, 1]의 range, 학습속도 상대적으로 빠름

* 미분 시 0에 가깝게 나올 수 있음

3. ReLU(Rectified linear unit)

* max(0,a)

* 속도가 빠름 0으로 수렴X

<br/>

## Purpose of perceptron

input x와 target t 사이의 관계를 잘 설명하는 weight w를 찾는 과정

<br/>

**측정 방법**

**loss function**을 통해 확인

<br/>

**Regression**

주로 squared loss 사용

<br/>

**Classification**

주로 cross-entropy 사용

* label을 더 높을 확률로 추정할수록 적은 loss

<br/>

**Cost function**

loss는 개별적인 값, cost는 모델 전체적인 값에 대한 설명

<br/>

## Gradient Descent


