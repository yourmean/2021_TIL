Vanishing Gradient

기계 학습에는 다양한 방법이 있는데, 그 중에서 Back Propagation을 통해 DNN 구조의 모델을 업데이트하며 학습하는 방식에서 생기는 이슈입니다.
Back Propagation 시에 학습해야 하는 변수가 업데이트되는 방식은 gradient, 즉 d(output)/d(param)을 계산해야만 합니다. 먄약 이 gradient가 작다면, parameter는 앵간히 발버둥 쳐봤자 output에 영향을 못 주게 됩니다.
쉽게 말하면, parameter가 가질 수 있는 값의 스펙트럼은 넓지만 output의 변화량은 좁은, squash 현상이 일어난 상태입니다.
이러면 자연스럽게 parameter가 더 이상 바뀔 의미를 못 찾게 되어서 학습이 진행되더라도 유의미하게 output을 개선시킬 수 없는 것이죠.

이론적인 얘기를 이해했다면, Sigmoid function을 쓰면 왜 Vanishing Gradient가 발생할 수 있는 지를 이해하기 쉽습니다. sigmoid(x)의 미분 그래프는 다들 아시다시피 상한이 0.25에 불과합니다. 그렇다면 다중 레이어가 쌓인다면, 맨 앞 layer에 대한 gradient는 최대 0.25 ^ K (K층이라고 하면)이 되고, 0에 한없이 가깝게 됩니다. 즉, 맨 앞의 parameter가 아무리 크게 바뀌더라도 Output의 gradient는 조금밖에 안 바뀌게 되는 것이죠.

따라서 Activation function의 Squashing effect가 있다면 Multi Layer Structure의 초반에 놓으면 그만큼 학습에 영향을 주기 때문에, Squashing issue가 없는 Relu등을 쓰면 Vanishing Gradient 현상이 사라진다고 표현하는 것입니다.
