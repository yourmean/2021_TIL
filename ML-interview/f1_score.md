##  f1 score


> f1 score는 어떻게 계산되며 Precision과 Recall은 무엇인가?
> 또한 f1 score 이외에 사용할 수 있는 평가메트릭에 대해 얘기


F1 score는 Precision과 Recall의 Trade-off 관계로 인해 적용하는 식으로 종속변수 class간의 데이터 불균형이 있을 때 사용하는 평가지표입니다. 다중분류의 경우는 micro, macro, weighted의 방법으로 나뉘어지며 다중분류 경우도 class간 데이터 불균형에 따라 거의 macro, weighted 두 방법중 하나를 선택합니다. micro f1-score는 accuracy와 값이 똑같습니다.

f1은 프리시전 리콜의 조화평균 정도로 알고 있네요

프리시전: 예측을 중심으로 얼마나 잘 예측했는지 (TP / (TP+FP)
리콜: 데이터를 중심으로 얼마나 잘 맞혔는지 (TP / TP+FN)


그럼 지금 말씀하셨던 것들을 예를들어서 쉬운 언어로 풀어 말하면 어떻게 설명할수 있을까요! + 어떤 경우에 사용하면 유리할까요!
