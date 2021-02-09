# Reward Function

Loss function에 대해서 @하늘  님께서 상세하게 설명해주실 것입니다!! 여기서 중요한 점은 "정답"이 있는 경우에만 "틀린 정도(Loss)"를 알 수 있다는 점입니다. 강화 학습은 Agent가 스스로 환경을 이해하고 최적의 행동을 해야 합니다. 즉, "정답"은 없고 "목표"가 있죠.

추천 링크: https://opentutorials.org/course/4548/28949

기계 입장에서 지도 학습이 "배우는 것"이라면, 강화 학습은 "경험하는 것"입니다. 둘의 차이는 "배우는 것"은 못 배우면 패널티(Loss)를 받고, "경험하는 것"은 더 좋은 경험일수록 더 높은 보상(Reward)을 받는다는 것이죠.

1. Loss(대답) = Func(대답, 정답)
2. Reward(상태) = Func(상태)

정답이 없어도 Reward가 최대화되는 쪽으로 학습을 할 것이기 때문에, 연구자는 "Agent가 학습했으면 좋겠는 방향"을 Func(상태)로 잘 표현해야 합니다.

다음 영상(https://www.youtube.com/watch?v=Crw1jztbVIc)을 보시면 어떤 캐릭터가 걷거나 달리거나 뛰는 것을 볼 수 있습니다. 하지만 "사람다움"을 내포하진 않죠. 이런 경우의 Reward function은 "흉부가 특정 높이 이상이라면 시작점으로부터의 거리가 멀수록, 상체가 하늘을 바라볼수록 고득점, 특정 높이 이하라면 -100점"이라고 상상해볼 수 있습니다. 일단 멀리 갔으면 좋겠으니 거리에 비례한 보상을 돌려주되, 최소한의 사람다움을 위해서 흉부의 높이와 방향에 제한을 둔 것이죠. 팔과 다리의 경우는 자유롭게 냅둔 것으로 보입니다.

이렇게 Reward Function을 어떻게 design하느냐가 연구자가 원하는 형태를 포함할 뿐, "정답"이 무엇인지 모른다는 점에서 Loss Function과 다르다고 봅니다!