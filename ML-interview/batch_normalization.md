# Batch Normalization

저번에 다뤘던 Internal Covariate Shift(ICS)를 리마인드 해보면, DNN의 구조상 Layer depth가 깊어짐에 따라 앞단의 변화가 뒷단이 받는 정보에 큰 변화를 주는 것이 ICS 였습니다. Google의 두 천재(Sergey Loffe & Christian Szegedy)는 https://arxiv.org/pdf/1502.03167.pdf 논문을 통해서 ICS 현상을 줄여주는 방법을 제시합니다. 그것이 이번 주제인 Batch Normalization(BN)이죠.

Layer의 Input이 불균형하며 크게 변하는 게 문제다 => 특정 분포를 따르면서 변화량도 크지 않도록 고정하는 건 어떨까?

제가 이해한 BN의 핵심 아이디어 입니다. 그렇다면 가장 쉬운 생각으로는, "layer의 input을 항상 N(0, 1)로 바꾸면 되지 않은가?"가 있겠죠. (Q1. 여기서 왜 Normal Distribution을 가정하는 가? Uniform인지, 아니면 다른 분포일 지 모르지 않은가!)

이러한 테크닉이 Whitening 입니다. Layer의 input을 feature끼리 uncorrelated하게 해주며 variance도 1로 바꾸는 것입니다. 몇 가지 문제가 있는데요, 첫 번째는 uncorrelated를 위한 Covariance Matrix와 inverse 계산의 비용이 크다는 것입니다. 두 번째는 (x-E[x]) 를 해주는 순간 bias의 정보를 학습할 수 없게 되는 등, 학습할 수 없는 정보들이 생긴다는 것입니다.

Batch Normalization은 Whitening의 단점들을 보완하면서도 ICS 현상을 없애려고 노력한 것입니다. 항상 고정된 N(0, 1)이 아니라, learnable parameter gamma와 beta를 만들어서, Layer input을 N(gamma, beta)로 변화시키자는 것입니다. gamma와 beta의 초기값은 1, 0 이지만, 학습 과정에서 optimal value가 찾아질 것이다 라는 것이죠.

학습 과정에서 ICS가 해소된다면 어떤 장점이 있을까요? Layer Input이 Network update에 대해 robust하기 때문에 Learning Rate를 키워도 Gradient Vanishing/Exploding 현상이 억제됩니다. 이에 따라 학습이 빠르게 이뤄지겠죠!

사실 BN에 대해서는 더 많고 깊은 이야기들이 있습니다. 이후에 나오는 스토리로는 다음과 같은 것들이 있습니다.

1. Efficient For General Activation Function?
2. Transforming CNN Network With Batch Normalization
3. Why BN Assuming Gaussian Distribution?
4. What about RNN Case?
5. Small number of data?

각각에 대해 저도 잘 알지도 못할 뿐더러 넘나 먼 길 같아서, 제가 생각하는 Batch Normalization의 "필요성"과 "핵심 아이디어"를 정리해봄으로써 만족해보겠습니다. BN을 직접 사용해보신 분들의 썰(사용 후기)이나 advanced story를 정리해주실 분이 계시면 환영입니다!
