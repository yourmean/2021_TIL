# Weight Initialization

학습을 전혀 하지 못한 기계는 멍청이입니다. 맨 처음 기계가 가진 가중치 W0에 대해서 F(W0, X*)는 Y*와는 정말 다르겠죠. 그렇기 때문에 저번에 함께 얘기했던 back-propagation을 통해서 점점 개선시키는 것이죠.

그렇다면 W0 은 어떻게 줘도 상관이 없느냐?에 대한 이야기를 할 차례겠죠? 여기에 대한 스토리는 다음과 같습니다. (참조: 1. https://medium.com/usf-msds/deep-learning-best-practices-1-weight-initialization-14e5c0295b94, 2. https://gomguard.tistory.com/184)

1. 생각하기 싫으니까 전부 0으로 만들자! 알고리즘마냥 모든 가중치 배열을 0으로 초기화해버리면 무슨 현상이 일어날까요? 같은 layer에 있는 각 뉴런들이 서로 구별이 될까요? 이전 layer의 출력들이 모두 동일한 weight를 가지고 이번 layer에 들어오게 됩니다. 즉, 어떤 두 뉴런을 잡아도 정확히 동일한 출력을 내뱉게 됩니다. 이는 곧 gradient까지 동일하기 때문에, update도 완전 동일하게 발생합니다. 지금도 똑같은 일을 하는데, 모델이 update 되어도 똑같다면, 아무리 update를 해도 한 layer에 있는 뉴런의 종류는 결국 한 가지가 됩니다.

이걸 다른 말로 표현하면 "equivalent to linear model" 이라고 합니다. 각 layer 마다 하나의 neuron만 있는 것과 다를 게 없는 것이죠. 즉, 모든 가중치를 0으로 하는 것은(좀 더 자세히 말하면 같은 layer에 있는 weight들을 모두 동일하게 하는 것은) 좋은 시작점이 아닌 것이라는 의미가 됩니다.

2. Gaussian Random with Constant SD! 모든 가중치를 N(0, sigma^2) 에서 sampling해서 정한다고 해보죠. 이러면 어떤 sigma를 써야할 지에 대한 고민이 시작됩니다. 또 아무 생각없이 적당하게 1 로 잡아볼까요? 표준편차가 1이기 때문에 weight가 충분히 클 수 있고, act func가 sigmoid나 tanh이라고 가정해보면, weight의 절댓값이 커질수록 gradient vanishing이 일어나겠죠? 단, 이 문제는 ReLU를 쓰면 사라집니다!

3. sigma가 1이 크다면, 작은 0.01로 해봅시다! 그러면 모든 weight가 매우 유사한 값을 가지며 1. 에서 논했던 symmetric 이슈가 다시 재개되겠죠! 이것도 마땅치가 않군요.,..

4. 여기까지 왔을 때 할 수 있는 생각은, "원초적인 문제는 각 layer의 output이 Random 해보이지 않는다는 것이다!" 라는 것입니다. 가중치만 백날 랜덤으로 정해봤자 각 뉴런이 출력이 랜덤하지 않다면, 어떤 형태로든 layer가 깊어질수록 뉴런의 출력이 2, 3 과 같이 꼬이게 됩니다. 그래서 나온 것이 Xavier Initialization 입니다. 각 layer의 출력도 정규 분포에 맞게 해주는 것이죠. 방법은 강의 자료(https://cs231n.github.io/neural-networks-2/#init) 를 참조해보시면 좋을 것 같아요!

5. 이러면 ReLU와 같이 출력의 절반을 0으로 날려버리는 act func는 어떨까요? 이러면 Xavier 가 원했던, 출력이 정규 분포인 것이 깨지게 됩니다. 이런 경우에 맞는 초기화 방식은 He Normal Init 입니다. Xavier와는 살짝 다른 휴리스틱이며 목적은 동일합니다!
