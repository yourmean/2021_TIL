# Optimizer

Optimizer란 무엇일까요? 바로 Loss function을 통해 구한 차이를 이용해 기울기를 구하고 Network의 parameter(W, b) 학습에 어떻게 반영할 것인지 결정하는 방법입니다! 유명한 그림으로는 위와 같은 Optimizer 발달계보가 있죠ㅎㅎ. 그럼 하나씩 살펴보도록 할까요?

- Gradient Descent(GD): 1회의 학습 step 시에 현재 모델의 모든 데이터에 대해서 예측 값에 대한 loss의 미분을 learning rate만큼 보정하여 반영합니다.

- Stochastic Gradient Descent(SGD): 1회의 학습 step 마다 모든 데이터의 계산이 너무 느리기 때문에 적은 수의 데이터 샘플이 전체 데이터 set의 gradient와 유사할 것이라고 가정하고 계산합니다.

- Momentum: 이전 step의 방향(=관성)과 현재 상태의 gradient를 더해 현재 학습할 방향과 크기를 정합니다. Local minima를 빠져나올 수 있기 때문에 SGD의 Oscilation현상을 해결할 수 있습니다.

- Nesterov Accelerated Gradient(NAG): Momentum과 비슷한 개념으로 이전까지의 moment step과 moment step 만큼 이동한 위치에서의 gradient를 더합니다.

- Adaptive Gradient(Adagrad): parameter 별로 gradient를 다르게 주는 방식입니다. 네트워크의 파라미터 수가 k일 때, gradient값은 time step t까지 각 변수가 이동한 gradient의 sum of squares를 저장하는 k*k dimension diagonal matrix입니다. 많이 변화한 변수들은 gradient에 저장된 값이 커지기 때문에 step size가 작은 상태로, 적게 변화한 변수들은 상대적으로 step size가 큰 상태로 학습에 반영 됩니다. 학습이 오래 진행되는 경우 gradient값이 너무 커져서 학습이 제대로 되지 않는 경우도 발생합니다.

- RMSProp: 학습이 오래 진행되면 step size가 너무작아지는 Adagrad의 단점을 보완하기 위한 방법입니다. 각 변수에 대한 gradient의 제곱을 계속 더하는 것이 아니라, 지수 평균으로 바꾸어 gradient값이 무한정으로 커지지 않도록 방지하면서 변화량의 상대적인 크기 차이를 유지합니다.

- Adaptive Delta(AdaDelta): RMSProp와 유사한 점은 gradient를 저장할 때 지수 평균을 사용한다는 점입니다. 차이점은 parameter update를 할 때 step size의 변화 값의 제곱을 가지고 지수 평균 값을 구하여 learning rate를 대체한다는 것이죠. 

- Adaptive Moment Estimation(Adam): Momentum방식과 유사하게 지금까지 계산해온 기울기의 지수 평균을 저장합니다. RMSProp와 유사하게 기울기의 제곱 값의 지수평균을 저장합니다. 학습 초반부에 m과 v가 0에 가깝게 bias되어 있을 것이라고 판단해 unbiased 작업을 거친 후에 계산을 진행합니다.
