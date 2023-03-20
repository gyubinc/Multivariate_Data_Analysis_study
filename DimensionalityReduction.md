
---

�� �Խñ��� ���ʼ� �������� [�ٺ��� ������ �м� ����](https://www.youtube.com/watch?v=o9uEVxzFeR0&list=PLetSlH8YjIfWKLpMp-r6enJvnk6L93wz2&index=1)�� ������� �ۼ��Ǿ����ϴ�.

---

�ۼ��� : KUBIG 17�� ������

# Chapter 4) Dimensionality Reduction
---

## 4-1 Dimensionality Reduction

�̷л�, �������� �������� �����Ͽ�, ������ �����Ҽ��� �� ���ɵ� ���
* ���ǿ����� ������ �������� ��찡 ���� ����, noise ���� ������ ������ �����Ҽ��� �� ������ �������� �ʴ´�

����: ���� ȿ���� �߱� -> ���� n���� ������ ����� ������ ���� ����� n`���� ������ ����� ������ ����ϴ�
* ���� �𵨿� ���� �� �´� subset of variable ã��

���� ����� ȿ��:
* ���� ������ ����� ���� -> ���� ����
* ���� processing �ܼ�ȭ
* �ߺ��ǰų� ���ʿ��� ���� ����
* �ð�ȭ ����

<br/>

**[Curse of Dimensionality]**
<br/>

���� ������ �����ϸ� �������� �����ϴ� �� �ʿ��� ����ġ�� ���ϱ޼������� �����Ѵ�

���� ��Ҹ� �� �� �ִ� ����: ������ ������ ���� ������ �ִ� �������� ���� Ȯ���� ����

���� �������� �߻��ϴ� ������:
* �����Ϳ� Noise�� ���� Ȯ���� �����Ѵ� -> ���� ������ ��������
* ��� �ð��� �����Ѵ�
* ���� ���� �𵨸��� �ϱ� ���ؼ� �� ���� ���� example�� �ʿ��ϴ�

������ ���ָ� �ذ��ϱ� ���� ���:
* Domain Knowledge ��� (������)
* ���� ���� ������ ��ȣ�ϴ� regularization term�� �߰�
* �������� ���� ��� technique ���

<br/>

**[Dimensionality Reduction]**

Supervised vs Unsupervised Dimensionality Reduction

[Supervised]
��/�˰��� �����Ͽ� �ǵ������ ���� ���� ���� ã��

[Unsupervised]
��/�˰��� �����Ͽ� �ǵ���� ����

�� ���� ���� ��Ҹ� �����Ѵ�

[Dimensionality Reduction Technique]

1. Variable/Feature Selection
* �����ϴ� ���� �߿��� �κ� �������� ���� �� ���� �̴� ��

2. Variable/Feature Extraction
* �����ϴ� ������ ����ؼ� ���ο� ������ ������ ��


## 4-2 Variable Selection Methods

**[Exhaustive Search]**

��� ������ ���� �׽�Ʈ

ex) x1���� x3�� ������ �� 7������ �õ�

����: �ð� �ҿ䰡 ��ϴ�

**[Forward Selection]**

���� �ƹ��͵� ������� �ʴ� �𵨺��� �����ؼ� �߿��� ���� �����Ǵ� �������� ���������� �߰��ȴ�
* ������ �ѹ� �߰��Ǹ� ���ŵ��� �ʴ´�
* �߰� ������ Ž������ �� ���� ����� ���ǹ����� ���� �� ����

**[Backward Elimination]**

��� ������ ���� �𵨺��� �����ؼ� �߿����� ���� �������� �������� ���ŵȴ�
* �ѹ� ���ŵǸ� �߰����� �ʴ´�
* � ������ ���� ������ ���ϰ� �ް��ϰ� �Ͼ�ٸ� ���� �������� ����

Backward Elimination, Forward Selection �� �� �ӵ��� ��������, ���� �϶��� �� �ִ�


**[Stepwise Selection]**

������ ���� �𵨺��� �����ؼ� forward selection, backward elimination ������ ���鼭 ����
* Forward selection�� backward elimination���� �ð��� �� �ɸ����� ���� �ö� ���ɼ��� Ŀ����
* ����/�߰��� ������ �ٽ� �߰�/���ŵ� �� �ִ�


Forward, Backward, Stepwise Selection ��� ȿ���������� search space�� �����Ǿ� ������ ���� optimal �� ������ ã�� Ȯ���� ����


**[Performance Metrics]**

1. Akaike Information Criteria (AIC)

$$ \text { Sum of squared error (SSE) } =  \sum_{i=1}^n (y_i - \hat{y_i})^2 $$

$$ AIC = n * ln({SSE \over n}) + 2k $$

k = ���� ����,
n = ����ġ ����

ù ��Ʈ�� ���� ������ ������� ������ ���, �� ��° term�� ���� �����̶�� ������ ������ ���� -> AIC�� �������� ����


2. Bayesian Information Criteria (BIC)

$$ BIC = n * ln({SSE \over n}) + {2(k+2)n\sigma^2 \over SSE} - {2n^2\sigma^4 \over SSE^2} $$

AIC�� �Ȱ��� ����, ������ ǥ������ �߰�

3. Adjusted $$R^2$$


**[Genetic Algorithm]**

Meta-Heuristic Approach: ������ ������ ȿ������ ���������� ���� Ǯ����� ��

Genetic Algorithm: ��ȭ�� ����� �˰���

* Selection: ������ ��ü �߿��� ��������� ����� �� ã��
* Crossover: ���� ��ü�� ������ ���ο� ��� ã��
* Mutation: local optima�� Ż���� �� �ִ� �������� ����


1. Initialize chromosomes
* Binary encoding�� ���� ���� ���δ�
* ������ binary encoding �� ���� chromosome
* ���� �ϳ��� �ش��ϴ� binary encoding�� gene
* 1�̸� ���� ���, 0�̸� ���� ��� X
2. Model training based on chromosomes
* Chromosome ���� - Population
* Population�� ������ ���� (���� 50-100)
* Fitness function ����
* Crossover Mechanism ����
* Rate of Mutation ����
* Stopping Criteria ����
3. Fitness evaluation
* � chromosome�� ������ �˷��ִ� ��ǥ
* Fitness ���� Ŭ���� chromosome�� ����
* Fitness ���� ���� chromosome�� ������, ������ �� ���� �� ����
* ���� ������ ������ ������, ���� ������ �� ���� chromosome ����
* Linear Regression ���� ��쿡�� Adjusted $$R^2$$, AIC, BIC�� fitness function

4. Selection good chromosomes
* ���� population���� ����� �Ϻθ� ����

[Deterministic Selection]
���� n % �� chromosome ����, ���� (100-n)% �� ���� X

[Probabilistic Selection]
* �� chromosome�� fitness ���� ���� ������ �ο�
* ����� chromosome�� ���� Ȯ���� ������ ���� chromosome�� ���� ��ȸ�� �ش�

5. Create next generation: Crossover & Mutation
[Crossover]
* �� ���� �θ� chromosome���� �� ���� child chromosome�� �����ȴ�
* crossover point�� 1���� total number of genes ������ ����

40:30 ĸ��

[Mutation]
* local optima�� �ɷ� ������ mutation�� ���ؼ� global optima�� ã�� ��ȸ ����
* mutation rate ���� 0.01 ����

6. Select the final variable set
* 2-5�ܰ踦 ��� �ݺ��ϸ鼭 Stopping Criteria�� ������Ű�� Fitness ���� ū chromosome�� ����
* �ʹݿ� fitness ���� ���� �������� ������ �̹�������

## 4-3 Shrinkage Methods

**[Ridge Regression]**

Linear, Logistic�� �� �� ��� ����

�� objective function�� $$ + \lambda \sum_{j=1}^d \hat{\beta}_j^2 $$

* L2 norm penalty
* �� ���� ������ ���ٸ� regression coefficient�� ���� ���� ��ȣ
* �����̱⿡ 0�� �� �� ���� -> variable selection���� ��� ����
* ���� ���̿� ���� ������谡 �ִٸ� ȿ����

**[LASSO]**

Least Absolute Shrinkage and Selection Operator

$$ + \lambda \sum_{j=1}^d |\hat{\beta}_j| $$

* L1 norm penalty
* �� �߿��� ȸ�� ����� 0���� ���� �� �ִ� -> Variable selection �� ��� ����
* Selected �� ���� ������ $$\lambda$$ ���� ���� �޶�����
* ���ٰ� Ŭ���� �� ���� ��Ÿ ������ 0�� ������ �����
* ���ٰ� ������ ��Ÿ ���� �������� 0�� �ƴ� ���� ����


**[Elastic Net]**

Ridge�� ���� (���� ������ ������踦 ������ �� �ִ�), LASSO�� ���� (Variable Selection) ����

$$ + \lambda_1 \sum_{j=1}^d |\hat{\beta}_j| + \lambda_2 \sum_{j=1}^d \hat{\beta}_j^2$$

$$\lambda_1$$�� Ŀ���� ������ ���� ����

$$\lambda_2$$�� Ŀ���� ������ ���ÿ� ���� impact ����



* Backward Selection�� ���� ��Ȯ����, ���� ������, ��� ȿ�������� �׻� ���� �ô� ���� ���� ��� �߿��� Top 3�ȿ� �����


  




