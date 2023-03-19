
---

�� �Խñ��� ���ʼ� �������� [�ٺ��� ������ �м� ����](https://www.youtube.com/watch?v=o9uEVxzFeR0&list=PLetSlH8YjIfWKLpMp-r6enJvnk6L93wz2&index=1)�� ������� �ۼ��Ǿ����ϴ�.

---

�ۼ��� : KUBIG 17�� ������

# Chapter 3)  Logisitic Regression
---

## 3-1 Logistic Regression: Formulation

����ȸ�ͷ� ��� ������ ����� ����/ǥ���� �� ���� �� Logistic Regression ���
<br/>

**[Classification Task]**
<br/>

Example: �� ������ ����� �����鿡���� ����ȸ�ͽ��� ���ʰ� �������� ������ ����ġ�Ͽ� ���� �߻�


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

p = probability of success	

������ ������ 0���� ��

**������ ����**
* 0 < odds < �� (������ ���� �� ����)
* Asymmetric/���Ī

**���� �ذ�**

$$ log(odds) = log( {p \over 1-p}) $$

* -�� < log(odds) < �� 
* Symmetric/��Ī
* p ���� ���� �� ����, p ���� Ŭ �� ���

<br/>

**[Logistic Regression Formula]**

$$ {p \over 1-p} = e^{\beta_0 + \beta_1x_1 + \beta_2x_2 ... + \beta_dx_d} $$

���� Ȯ��:

$$ p = {1 \over 1 + e^{-(\beta_0 + \beta_1x_1 + \beta_2x_2 ... + \beta_dx_d)}} $$


## 3-2 Logisitic Regression: Learning


���� ������ ���� ���ֿ� ���� Ȯ���� ���� �������ִ� ���� ����

<br/>

**Likelihood Function**

Likelihood: ���� Ŭ������ �з��� Ȯ��

* ��� ��ü�� ���������� ����Ǿ�����, dataset�� likelihood�� ��� ��ü�� likelihood�� ���̴�
* log-likelihood�� �Ϲ������� ���ȴ�
* likelihood, log-likelihood�� Ŭ���� ������ ����
* Max likelihood = Max log(likelihood) = Min -log(likelihood)

<br/>

**Maximum likelihood estimation (MLE)**

�����ͼ��� ������ likelihood�� �ִ�ȭ�ϴ� coefficient�� ã�� �� ��ǥ

$$ P(x_i, y_i | \beta) = \sigma(x_i | \beta) $$      $$   if y_i = 1$$

$$ P(x_i, y_i | \beta) = 1 - \sigma(x_i | \beta) $$      $$   if y_i = 0$$

yi�� 0 �ƴϸ� 1�̹Ƿ� �� ���� ������ ���� �� �� �ִ�:

$$ P(x_i, y_i | \beta) = \sigma(x_i | \beta)^{y_i}(1 - \sigma(x_i | \beta))^{1-y_i} $$

<br/>

��ü �����ͼ��� likelihood�� ������ ���� ǥ��:

$$ L(X,y|\beta) = \prod_{i=1}^N {P(x_i, y_i | \beta)} = \prod_{i=1}^N{\sigma(x_i | \beta)^{y_i}}(1 - \sigma(x_i | \beta))^{1-y_i} $$

�α׸� �ϸ�:

$$ logL(X,y|\beta) = \sum_{i=1}^n y_i log(\sigma(x_i | \beta)) + (1-y_i)log((1 - \sigma(x_i | \beta)) $$

* ���⼭ log likelihood�� beta�� �����̱� ������ explicit solution�� ���� 
* ����, Gradient Descent ���� ����ȭ �˰����� ���� ���� �ظ� ã�ư���

**Gradient Descent**

log likelihood function�� �̺��ϸ鼭 gradient�� 0�� �� ������ weight(Beta Hat)���� �ٲٸ鼭 �õ�

* �̶� weight�� ������ �ݴ� �������� �����̸鼭 �õ�

* ��Ÿ ���� ����ȭ�ؼ� ã�� �� ���� Ȯ�� ����� ���� ������ �Ѵ�:
 

 ## Sigma �߰�

$$ p = {1 \over {1 + e ^ {-(\beta_0 + \beta_1x_1 + \beta_2x_2 ... + \beta_dx_d)}}} $$

���⼭ ������ Ȯ���� 0���� 1 ������ ���ε� �׷� ����� � Ŭ������ �Ҵ��� ������ ���ϴ� �� cut-off (threshold)�̴�
* �Ϲ������� ���� cut-off�� 0.5������ ��Ȳ�� ���� �ٲ� �� �ִ�

<br/>

## 3-3 Logisitic Regression: Interpretation

[Odds Ratio]

**Odds Ratio** input ������ 1 ������ ���� ���� ���� 

x�� �� ���� �����Ѵٰ� ��������:

$$ {odds(x_1 + 1, ..., x_d)} \over {odds(x_1, ..., x_d)} $$

$$ = e ^ {\beta_0 + \beta_1(x_1+1) + \beta_2x_2 ... + \beta_dx_d} \over  e ^ {\beta_0 + \beta_1x_1 + \beta_2x_2 ... + \beta_dx_d} $$

* x<sub>1</sub>�� 1 ������ ��, ����� e<sup>��</sup><sup>^1</sup> �踸ŭ ���� �ƴϸ� �����Ѵ� 
* �Ⱑ ����� coefficient�� success class�� positively correlated = ���� ���ֿ� ���� ���ɼ� ����
* �Ⱑ ������ coefficient�� success class�� negatively correlated = ���� ���ֿ� ���� ���ɼ� ����

<br/>

[Multinomial Logistic Regression]

1. baseline class�� �����
2. baseline class�� �и�� �ϴ� ��� ���� ȸ�ͽ� ���� �� �����
* class 1 vs class 3, class 1 vs class 2, class 2 vs class 3 --> �� ��� ���� ȸ�ͽ�

K class�� �ִµ� k-1 ��ŭ �𵨸� �ϴ� ������ likelihood�� ���� 1�̹Ƿ� k-1 likelihood�� �˸� ������ Ŭ������ �ڵ����� ��� ����

## 3-4 Classification Performance Evaluation

�� �򰡰� �ʿ��� ����: �н��� �����͸� �н��� ���ϴ� ���� �ƴ϶� ���ο� �����͵� ���� ������ �� �� ������ ��

Validation Set�� ���ؼ� �Ķ���Ͱ� ����ȭ

Test set�� ���ؼ� ������ ���� �� ã�� 

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
* BCR�� �� ������ ��Ȯ���� ���� ���


Recall = $$ {n_{11} \over {n_{11} + n_{10}}} $$

Precision = $$ {n_{11} \over {n_{11} + n_{01}}} $$

F1- Measure = $$ {2 * Recall * Precision} \over {Recall + Precision} $$ 

* �� metrics ���� cut-off ���ؿ� ���� ���� �� �޶����� --> Cut off dependent


[Cut-off for classification]

�з� �˰����� �� class�� ���� likelihood�� Ȯ��, degree of evidence�� �����ش�
* ���⼭ �з� ���� ������ �˰����� cut-off�� ���� ������ �޴´�
* ����, �� ���� �� cut-off�� ���ؼ� �������� ��ǥ ���
* cut-off�� ���ؼ� ���������� ������ ��� ���� �ٸ� �𵨺��� ���� ���̰� ���� �� �ִ�


**Receiver Opearting Characteristic Curve (ROC Curve)**

 AUROC = Area Under ROC Curve

 ROC Curve:
 * P(�з� Ŭ����)�� ������������ ����
 * ��� cut-off ���ؿ��� true positive rate�� false positive rate�� ���� ���
 * ����� ���� �ð�ȭ*

 True positive rate = $${True Positive} \over {True Positive  + False Negative} $$

 False positive rate = $${False Positive} \over {False Positive  + True Negative} $$


 *true positive, false positive�� �ð�ȭ�� �� ROC curve �Ʒ��� ���̰� AUROC
 *AUROC�� 1�� �������� ������ ���� �� (ideal classifier), 0.5�� �������� ���� �з� (random classifier)








