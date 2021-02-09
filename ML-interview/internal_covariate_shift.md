# Internal Covariate Shift

현실에서 데이터 분석이 얼마나 잘 될까요? 데이터를 모아서 분석을 통해 미래 데이터를 예측하는 행위는, 실제로는 (논문을 포함해서) 온갖 장애물을 요리조리 피하며 이겨내야 합니다. 장애물 중 하나가 Dataset Shift 입니다. 입력으로 들어오는 Dataset이 항상 고정된 분포를 가지고 주어지는 것이 아니라, 분석하는 시점과 활용하는 시점 사이에서 데이터 분포가 변화하는 경우 등, 제어하지 못하는 부분이 많이 있습니다. 분석한 데이터는 3~5월 데이터의 옷 판매 추이를 학습하고 6월에 이걸 이용해서 옷 판매 추이를 예상해본다? 날씨라는 큰 변화가 생기기 때문에 올바르게 동작하지 않을 것이겠죠.

좀 더 세밀하게 표현하면 Covariate Shift, Prior Probability Shift, Concept Shift 등이 있습니다. 각각을 짧게 표현하면, Covariate Shift는 독립 변인의 shift, Prior Probability Shift는 종속 변인의 shift, Concept Shift는 독립 변인과 종속 변인 사이의 관계의 shift 입니다.

Covariate shift는 Deep Learning에서도 발생합니다. 각 Layer를 Input과 Output이 존재하는 함수라고 생각해보겠습니다. K번째 Layer의 output이 K+1번째 Layer의 Input이 되는 것이죠. 이 때 각 Layer가 해야하는 일은, Input에 대한 적절한 Output을 학습해야 하는 것입니다. 근데 하나의 Layer는 Input이 계속 고정된 분포로 주어져도 성공적으로 학습하기 힘든데, 한 번 Update마다 앞쪽 Layer의 Output이 바뀌면 Input의 분포가 바뀌는 것 때문에 더 공부하기 힘든거죠. 쉽게 말하면, 오늘 A라는 문제집을 조금 풀고, 내일은 B라는 새로운 문제집을 조금 풀고, 등등 매일매일 서로 다른 문제집을 푸니까 공부에 집중을 못하는 것입니다.

이렇게 학습이 진행되면서 한 번의 Update가 다음 공부를 방해하는 현상이 Internal Covariate Shift입니다. 중간 Layer들마다 Shift가 조금씩 누적되어서 뒤쪽 Layer의 Weight가 학습되는 속도에 엄청난 저하가 일어나게 되는 것입니다. 이걸 고치는 방법으로 제안됐던 게 BatchNorm, Whitening, InstanceNorm 등인데 실제로는 Internal Covariate Shift는 별로 안 줄어든다는 논문이 있다고 합니다. 다음의 두 자료를 첨부합니다. https://arxiv.org/abs/1805.11604, https://kw94.tistory.com/103  (Special Thanks to @오휘)

저는 저걸 읽고 설득을 절반쯤 당했습니다. BN이 Internal Covariate Shift에 별 영향이 없다?는 general case에 대해 대답하긴 쉽지 않고, 새로운 영향을 제안하는 것들은 의미가 있다고 생각합니다. 여러분의 생각은 어떠신가요!!!
