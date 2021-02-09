Back Propagation (역전파)

우리가 배움을 접하기 가장 쉬운 딥러닝 모델은 MLP(Multi Layer Perception)입니다. Input Layer -> Hidden Layers -> Output Layer 의 형태를 띄고, 각 Layer 간에는 Feed Forward 형태로 weight가 엮여 있죠. (잘 생각해보시면 cycle이 존재하지 않을 겁니다!)

그렇게 만든 모델을 함수로 표현하면 F(X, W) = Y 입니다. (우리는 언제나 딥러닝 모델이 하나의 함수라는 것을 상기해야 합니다.) X라는 입력이 들어왔을 때, W 라는 변수들을 이용해서 Y 라는 출력값을 내뱉는 모델 F 가 있는 것이죠.  하고 싶은건 결국 X를 줬을 때 Y* 라는 기댓값에 최대한 가까운 Y가 나오도록 해주는 W 를 찾는 것, 일종의 function optimization 이라는 것이죠!

함수를 원하는 형태에 맞게 최적화하는 과정, 여기서 함수의 형태가 관건이 됩니다. 만약 함수가 convex function 이라면? 스무스하게 뉴턴 메소드 같은 gradient descent(GD) 방식을 쓰면 무조건 global solution이 튀어나옵니다. 하지만 우리는 앞서 보았던 (하늘님께서 열심히 정리해주신) activaion function들이 F 안에 숨어있다는 것을 알죠? 이 함수들이 non-linear 이라는 것과 이유도 알고 있습니다.

즉, 함수 F 는 non-convex function 이라는 것이죠. 여기서 생기는 문제는, 함수의 형태가 복잡해지면서 W space에 대해서 non-convex 를 이루게 됩니다. 그렇다면 이럴 때에 GD는 어떻게 사용해야 W 가 좋은 방향으로 바뀔 것인가? 구해야 하는 것은 W가 dW만큼 찔끔 바뀔 때, 전체 출력 Y가 변하게 될 양 dY 입니다. 즉 dY/dW 를 알아야, Y가 Y*에 가까워지기 위해서는 W가 얼만큼 바뀔 지를 알 수 있는 것이죠.

여기서 나오는 게 back-propagation 입니다. F 를 깡으로 전개해서 dY/dW를 계산하는 것은 갱-장히 어렵습니다. multi-layer 인 경우에는 앞단에 있는 W의 변수 하나가 식에 엄청난 개수로 식에 등장하기 때문이죠. 여기서 쓰게 되는 아이디어가, 만약 dY/dW 를 뒷 단의 W 변수들 부터 계산한다면, 앞단의 W 변수에 대한 dY/dW를 뒷단의 결과와 chain rule을 통해서 쉽게 계산할 수 있더라~ 라는 것이죠.

이건 결국 MLP 형태의 모델을 가정했기 때문에, 입력이 출력으로 변하는 과정이 Feed Forward 라는 것 때문에 dY/dW 를 쉽게 계산할 수 있다는 것이죠.

정리하면, Back Prop은 W 를 좀 더 좋은 방향으로 바꿔나가기 위해 Gradient Descent를 하는데, 모델이 MLP인 경우에 그걸 쉽게 계산할 수 있는 방법 중 하나입니다.

이게 GD 이기 때문에 full-batch를 mini-batch로 바꿔서 SGD를 하느니 등의 이야기가 등장해도 어색함이 없게 되는 것이죠! (나중에 다뤄봅시다 ㅎㅎㅎ)

제가 면접에서 설명했던 방식은 여기까지입니다. "어떻게"보다는 "언제, 왜 필요한 지"에 집중해서 대답했던 것 같네요. 각자 자기만의 방식으로 설명해봐주셨던 @Jae/준/vision,nlp  @테리유/준/비전  두 분의 대답도 감사드립니다!
