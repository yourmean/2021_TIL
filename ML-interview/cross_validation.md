# Cross Validation

Cross Validation(교차검증)은 고정된 train set과 test set으로 평가와 모델튜닝을 반복하다 보면, test set에만 과적합 되어버리는 결과가 발생하게 됩니다! 이를 해결하기 위한 방법 중 하나가 Cross Validation(교차검증)이죠.

그렇다면 교차검증이 어떻게 이 문제를 해결할까요? 가장 기본적인 기법인 (k-ford cross validation)를 예시로 들어서 설명해볼까요? test set에 과적합 되는 문제는 test set이 데이터 중 일부분으로 고정되어 있기 때문에 발생합니다. 따라서 고정된 test set을 학습시키는것을 방지하기 위해 아래와 같이 test set 을 하나로 고정하지 않고 데이터 모든 부분을 활용하여 모델을 검증하는 것을 Cross Validation(교차검증)이라고 합니다. 

[ㅇ|ㅇ|ㅇ|ㅇ|X]  -> Accuracy1
[ㅇ|ㅇ|ㅇ|X|ㅇ] -> Accuracy2
[ㅇ|ㅇ|X|ㅇ|ㅇ] -> Accuracy3
[ㅇ|X|ㅇ|ㅇ|ㅇ] -> Accuracy4
[X|ㅇ|ㅇ|ㅇ|ㅇ] -> Accuracy5

먼저 데이터셋을 k개의 subset으로 나누고 k(예시에서는 5)번 평가를 시행합니다. 이때 test set을 중복없이 바꾸면서 실험하는거죠! 최종 모델성능평가는 모든 결과의 평균값으로 사용합니다.(일반적인경우)

장단점을 말해보자면 아래와 같겠죠!

장점 :
1. 모든 데이터 셋을 평가에 활용할 수 있다.
- 평가에 사용되는 데이터 편중을 막을 수 있다.
(특정 평가 데이터 셋에 overfit 되는 것을 방지할 수 있다.)
- 평가 결과에 따라 좀 더 일반화된 모델을 만들 수 있다.
2. 모든 데이터 셋을 훈련에 활용할 수 있다.
- 정확도를 향상시킬 수 있다.
- 데이터 부족으로 인한 underfitting을 방지할 수 있다.

단점: 
Iteration 횟수가 많기 때문에 모델 훈련/평가 시간이 오래 걸린다.

이외에도 Cross Validation(교차검증)에는 다양한 기법이 존재합니다. 위에서 예시로 든 k-ford cross validation을 포함하여 5가지만 간략히 소개하도록 할게요.


1. 홀드아웃 방법(Holdout method)
- Holdout method 또는 Holdout cross validation이라고 불림
- 이 방법이 교차 검증인지 아닌지에 대해서는 애매한 부분이 존재, 일부 문서에서는 교차 검증 범주에 속해져있기 때문에 소개
- 주어진 train set을 다시 임의의 비율로 train set과 test set으로 분할하여 사용
- 이 때 train : test = 9 : 1 또는 7 : 3 비율이 가장 자주 쓰이며, Iteration(훈련 및 검증)을 한 번만 하기 때문에 계산 시간에 대한 부담이 적은 것이 장점
- 반면에, test set에 관한 검증 결과 확인 후 모델 파라미터 튜닝을 하는 작업을 반복하게 되면 모델이 test set에 대해 overfit 될 가능성이 높다는 것이 단점

2. k-겹 교차 검증(k-fold cross validation)
- k-겹 교차 검증 방법은 가장 일반적으로 사용되는 교차 검증 방법
- 데이터를 k개의 데이터 폴드로 분할하고, 각 Iteration마다 test set을 다르게 할당하여 총 k개의 '데이터 폴드 세트'를 구성
- 따라서 모델을 학습 및 훈련하는데 총 k번의 Iteration이 필요한 것이 특징
- 각 데이터 폴드 세트에 대해서 나온 검증 결과들을 평균내어 최종적인 검증 결과를 도출하는 것이 일반적

3. 리브-p-아웃 교차 검증(Leave-p-out cross validation)
- 전체 데이터(서로 다른 데이터 샘플들) 중에서 p개의 샘플을 선택하여 그것을 모델 검증에 사용하는 방법
- 따라서, test set을 구성할 수 있는 경우의 수(=훈련 및 검증에 소요되는 Iteration 횟수)는 nCp
- k-겹 교차 검증 방법과 마찬가지로, 각 데이터 폴드 세트에 대해서 나온 검증 결과들을 평균내어 최종적인 검증 결과를 도출하는 것이 일반적
- 이 교차 검증 방법은 구성할 수 있는 데이터 폴드 세트의 경우의 수가 매우 크기 때문에, 계산 시간에 대한 부담이 매우 큰 방법

4. 리브-원-아웃 교차 검증(Leave-one-out cross validation)
- Leave-one-out cross validation은 줄여서 LOOCV라고도 불리우며, 앞서 언급했던 leave-p-out cross validation에서 p=1일 때의 경우를 말함
- leave-p-out cross validation 보다 계산 시간에 대한 부담은 줄어들고, 더 좋은 결과를 얻을 수 있기 때문에 더욱 선호됨
- 검증에 사용되는 test set의 갯수가 적은 만큼 모델 훈련에 사용되는 데이터의 갯수는 늘어남
- 모델 검증에 희생되는 데이터의 갯수가 단 하나이기 때문에, 나머지 모든 데이터를 모델 훈련에 사용할 수 있다는 것이 장점

5. 계층별 k-겹 교차 검증(Stratified k-fold cross validation)
- 주로 Classification 문제에서 사용되며, label의 분포가 각 클래스별로 불균형을 이룰 때 유용하게 사용
- label의 분포가 불균형한 상황에서 sample의 index 순으로 데이터 폴드 세트를 구성하는 것은 데이터를 검증하는데 치명적인 오류를 야기할 수 있음 Stratified k-fold cross validation은 이러한 데이터 label의 분포까지 고려해 주어서(그렇기 때문에 데이터 폴드 세트를 구성해주는 함수에서 데이터의 label 값이 요구됨), 각 훈련 또는 검증 폴드의 분포가 전체 데이터셋이 가지고 있는 분포에 근사하게 됨
