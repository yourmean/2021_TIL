Activation function(활성화 함수)

Activation function(활성화 함수)란 무엇일까요? 알고계시겠지만, 인공신경망은 사람의 뉴런을 모방하여 만들어졌습니다. 즉, 이 개념은 단일 퍼셉트론에서 출발했죠. 퍼셉트론은 여러개의 신호가 들어오면 이를 조합하여 다음으로 신호를 보낼지 말지 결정합니다. 이것을 발전시킨 neural network에서는 하나의 단일 뉴런에 여러 신호가 들어오면 다음 뉴련에 보낼 신호의 강도를 결정합니다. 즉, 단일 퍼셉트론이 multi layer perceptron으로 발전해나가는 과정에서 뉴런은 신호의 전달 유무 외에 전달 강도를 정해야 합니다. 이 때, 전달하는 신호의 세기를 정하는 방법이 Activation function(활성화 함수)입니다. 

그럼 Activation Function(활성화 함수)로 Step Function 부터 Linear Activation Function 등 많이 알고 있는 함수를 쓰는 것이 좋을까요? 이 두 함수는 좋은 Activation Function(활성화 함수)은 아닙니다. 왜냐하면 Step Function 같은 경우 0, 1 두 가지 값으로만 출력이 가능합니다. 즉, 다중 출력을 할 수 없죠. 다음으로 Linear Activation Function은 Step Fucntion과 달리 다중 출력은 가능하지만, Backpropagation이 불가능하고 Hidden Layer를 무시하는 결과를 출력합니다. h(x) = ax일 때, Hidden Layer를 여러 겹 쌓아올려도 출력이 h(x) = a'x로 같기 때문이죠!

그러면, 이외에 7개의 Activation Function(활성화 함수)에 대해 정리해 볼게요! (Reference: cs231n Lecture6. Training Neural Network Part I)

Activation Function? - 위 내용을 짧게 정리하면, 입력 신호의 총합을 출력신호로 변환하는 함수

- Sigmoid

  출력 값을 0에서 1로 변경해 주고, 가장 많이 사용되었던 Activation Function 중 하나입니다. 하지만, 단점도 존재하죠! 첫번째, Saturation 두번째, Sigmoid outputs are not zero-centered 이렇게 두가지입니다.

  Saturated 되었다는 것은 Activation Function의 구간에서 기울기(gradient)가 0에 가까워지는 현상을 말합니다. 이 것은 Vanishing gradient 문제를 발생시킵니다. 그런데 Sigmoid 함수의 출력 그래프를 보면 입력 신호의 총합이 크거나 작을 때 기울기가 0에 가까워 지는 것을 볼 수 있죠! 즉, Staturation이라는 문제점이 생깁니다.

  그럼 두번째 단점인 Zero-centerd하지 않다는 점은 왜 단점이 될까요? 이것을 설명하려면, Backprop를 해보면서 확인해 봐야하는데 그러기엔 너무 길어지니, 짧게 결론만 정리하겠습니다. gradient 항상 Positive or Negative인 경우는 비효율적으로 최적해를 탐색하게 됩니다. 직선으로 해를 탐색하는 것이 아닌 지그재그로 왔다갔다 하며 해를 탐색하게 되는 거죠! 여러 번 탐색을 해야 하기 때문에 비효율적인 weight update방법이 됩니다. 이것이 바로 우리가 일반적으로 zero-mean data를 원하는 이유입니다. 입력 X가 양수/음수를 모두 가지고 있으면 gradient w가 전부 Positive/Negative로 움직이는 것을 막을 수 있습니다.

- tanh

  tanh는 출력값을 -1에서 1로 압축시켜주며 zero-centerd합니다. 이말은 sigmoid의 단점 중 하나를 해결해 준다는 말이겠죠! 하지만, 여전히 gradient가 소멸하는 구간이 있습니다. (Positive/Negative 구간 모두 존재합니다.)

- ReLU

  ReLU의 특징은 양의 값에서 Saturated 되지 않습니다. 그리고 계산 효율이 뛰어나기 때문에  tanh와 sigmoid보다 약 6배 정도 빠릅니다. 하지만 non-zero centered가 다시 발생하며 음수 영역에서 saturated되는 문제도 다시 발생합니다. 또한 Dead ReLU가 발생할 수 있습니다. Dead ReLU는 초기화를 잘못했거나 Learning rate가 높은 경우에 발생하게 됩니다. 초기화를 잘못한 것은 가중치 평면이 data cloud에서 멀리 떨어져 있는 경우로, 이럴 때는 어떤 입력 데이터도 activate 되지 않습니다. Learning rate가 높은 경우는 ReLU가 데이터의 manifold를 벗어나게 됩니다. 이 경우가 더 흔한 경우겠죠. Dead ReLU를 피하기 위해서 ReLU를 초기화할 때 positive biases를 추가해 주는 경우가 있습니다. Weight Update시에 active ReLU가 될 가능성을 조금이라도 늘려주기 위함인데, 이 방법이 도움이 된다는 주장도 있고 도움이 되지 않는다는 주장도 있다네요.

- LeakyReLU

  ReLU 이후 수정된 버전들이 나오고 있는데 그 중 하나가 바로 Leaky ReLU입니다. ReLU와 유사하지만 Negative 영역에서 더 이상 0이 아니며, saturated 되지 않습니다. 하지만, 여전히 계산이 효율적이며 빠르고 더 이상 Dead ReLU현상이 없게 됩니다.

- PReLU

  ReLU 수정본의 또 다른 예시로는 prametric rectifier, PReLU가 있습니다. PReLU는 negative space에 기울기가 있다는 점에서 Leaky ReLU와 유사한 것을 알 수 있습니다. 다만 여기에서는 기울기가 alpha라는 파라미터로 결정이 됩니다. alpha를 딱 정해놓는 것이 아니라 backprop으로 학습시키는 파라미터로 만든 것입니다.

- ELU

  이번엔 ReLU 수정본의 또 다른 예시로 Exponential Linear Units(ELU)를 보도록 하겠습니다. ELU는 zero-mean에 가까운 출력 값을 보입니다. (그래프를 보면 0을 기준으로 조금 부드러움) 앞선 ReLU 시리즈들이 zero-mean 출력 값을 갖지 못하는 것에 비해 상당한 이점을 가지고 있습니다. 하지만 Leaky ReLU와 비교해보면 ELU는 negative에서 "기울기"를 가지는 것 대신에 또다시 Saturated 되는 문제를 나타냅니다. ELU는 이런 Saturation이 좀 더 noise에 강인할 수 있다고 주장 합니다. (논문을 봐야 자세히 알거같아요. 안 읽어봄.)

- Maxout

  마지막으로 Maxout Neuron입니다. 지금까지 본 활성화 함수들과는 조금 다르게 생겼습니다. 입력을 받아들이는 특정한 기본 형식을 미리 정의하지 않습니다. 대신에 w1에 x를 내적 한 값 + b1과 w2에 x를 내적 한 값 + b2의 최댓값을 사용합니다. Maxout은 두 값 중 최댓값을 선택합니다. Maxout은 ReLU와 Leaky ReLU의 좀 더 일반화된 형태입니다. 왜냐하면 Maxout은 두 개의 선형 함수를 취하기 때문입니다. Maxout 또한 선형이기 때문에 Saturation 되지 않으며 gradient가 소멸하지 않습니다. 여기서 문제점은 뉴런당 파라미터의 수가 두 배가 된다는 것이죠.
