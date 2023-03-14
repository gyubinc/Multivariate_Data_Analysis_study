
---

�� �Խñ��� ���ʼ� �������� [�ٺ��� ������ �м� ����](https://www.youtube.com/watch?v=o9uEVxzFeR0&list=PLetSlH8YjIfWKLpMp-r6enJvnk6L93wz2&index=1)�� ������� �ۼ��Ǿ����ϴ�.

---

�ۼ��� : KUBIG 17�� ������

# Chapter 3)  Logisitic Regression
---

## 3-1 Logistic Regression: Formulation

����ȸ�ͷ� ��� ������ ����� ����/ǥ���� �� ���� �� Logisitic Regression ���
<br/>

**[Classification Task]**
<br/>

Example: �������� ����� �����鿡���� ����ȸ�� ���� ���ʰ� �������� ������ ����ġ�Ͽ� ���� �߻�


$$ y = \beta_0 + \beta_1x_1 + \beta_2x_2 ... + \beta_dx_d + \epsilon $$

$$ \beta = coefficient \quad \epsilon = noise$$

* �º��� 0 �ƴϸ� 1�� ���� �� �ִµ� �캯�� ��� �Ǽ��� ���� �� �ִ� 
* ��ǥ�� ȸ�� ���� ������ �����ϴ� �з� �� �����
<br/>

**[Goal]**

 ���� ������ ������ ���� ����� 0 �ƴϸ� 1�� binary outcome�� �ǵ��� �ϴ� �Լ� ã�� 
 * y�� logit �Լ��� output���� ���
 * logit�� ����ϸ� ���� �����鿡 ���� ���� �������μ� ������ �� ����
 * logit�� ��� Ȯ���� ����

<br/>

**[Odds]**

$$ odds = {p \over 1-p} $$
$$ p = probability of success

������ ������ 0���� ��

**������ ����**
* 0 < odds < �� (������ ���� �� ����)
* Asymmetric/���Ī

**���� �ذ�**

$$ log(odds) = log( {p \over 1-p}) $$

* -�� < log(odds) < �� 
* Symmetric/��Ī
* p ���� ���� �� ����, p ���� Ŭ �� ���*

<br/>

**[Logistic Regression Formula]**

$$ {p \over 1-p} = e^{\beta_0 + \beta_1x_1 + \beta_2x_2 ... + \beta_dx_d} $$

���� Ȯ��:

$$ p = {1 \over 1 + e^{-(\beta_0 + \beta_1x_1 + \beta_2x_2 ... + \beta_dx_d)} $$


## 3-2 Logisitic Regression: Learning


���� ������ ���� ���ֿ� ���� Ȯ���� ���� �������ִ� ���� ����

<br/>

**Likelihood Function**

Likelihood: ���� Ŭ������ �з��� Ȯ��

* ��� ��ü���� ���������� ����Ǿ�����, dataset�� likelihood�� ��� ��ü���� likelihood�� ���̴� 
* log-likelihood�� �Ϲ������� ���ȴ� 
* likelihood, log-likelihood�� Ŭ���� ������ ����
* Max likelihood = Max log(likelihood) = Min -log(likelihood)

<br/>

**Maximum likelihood estimation (MLE)**

�����ͼ��� ������ likelihood�� �ִ�ȭ�ϴ� coefficient�� ã�°� ��ǥ

$$ P(x_i, y_i | \beta) = \sigma(x_i | \beta) $$      $$   if y_i = 1$$

$$ P(x_i, y_i | \beta) = 1 - \sigma(x_i | \beta) $$      $$   if y_i = 0$$

yi�� 0 �ƴϸ� 1�̹Ƿ� �� ���� ������ ���� �� �� �ִ�:

$$ P(x_i, y_i | \beta) = \sigma(x_i | \beta)^{y_i}(1 - \sigma(x_i | \beta))^{1-y_i} $$

<br/>

��ü �����ͼ��� likelihood�� ������ ���� ǥ��:

$$ L(X,y|\beta) = \prod_{i=1}^N {P(x_i, y_i | \beta)} = \prod_{i=1}^N{\sigma(x_i | \beta)^{y_i}(1 - \sigma(x_i | \beta))^{1-y_i} $$

�α׸� �ϸ�:

$$ logL(X,y|\beta) = y_i log(\sigma(x_i | \beta)) (1-y_i)log((1 - \sigma(x_i | \beta)) $$

* ���⼭ log likelihood�� beta�� �����̱� ������ explicit solution�� ���� 
* ����, Gradient Descent ���� ����ȭ �˰����� ���� ���� �ظ� ã�� ����

**Gradient Descent**

log likelihood function�� �̺��ϸ鼭 gradient�� 0�� �� ������ weight(Beta Hat)���� �ٲٸ鼭 �õ�
* �̶� weight�� ������ �ݴ� �������� �����̸鼭 �õ�*

* ��Ÿ ���� ����ȭ�ؼ� ã�� �� ���� Ȯ�� ����� ���� ������ �Ѵ�:

$$ p = {1 \over {1 + e ^ {-(\beta_0 + \beta_1x_1 + \beta_2x_2 ... + \beta_dx_d)}} $$

���⼭ ������ Ȯ���� 0���� 1 ������ ���ε� �׷� ����� � Ŭ������ �Ҵ��� ������ ���ϴ°� cut-off (threshold) �̴�
* �Ϲ������� ���� cut-off�� 0.5������ ��Ȳ�� ���� �ٲ� �� �ִ�

<br/>

## 3-3 Logisitic Regression: Interpretation

������ x�� 1��

* Linear : y = f(x)�� �������� ����(����)

* Non-linear : r = f(x)�� �������� ����(�)

<br/>

## Multiple Regression Models

������ x�� 2���̻� ����

* Linear

* Non-linear

<br/>

**Linear Regression**

���������� �������� 1������ �������� ǥ���ȴ�

* �������� 3�� �̻��� ��� hyper-plane�� ����

<br/>

**OLS**

Ordinary least square, �ּ��ڽ¹�

* actual taget value�� regression�� ���� ������ ������ squared difference�� �ּ�ȭ

* ��� ������ �������� ǥ��

* $\hat{\beta} = (X^TX)^{-1}X^Ty$��� ����� solution ����

**���� ����**

* noise $\epsilon$ �� ���Ժ����� ������<br/>������ ���� QQ Plot�� �׷��� Ȯ�ΰ���

* �����Ͱ� ���������� ��

* ����ġ���� ��ȣ �������� ��

* Y�� �������� Ư���� ������ ��ȭ�� ������ ���� ���� �� (homoskedasticity)<br/>Residual plot�� ����

**Goodness of fit**

����ǥ

**Sum-of-Squares Decomposition**






