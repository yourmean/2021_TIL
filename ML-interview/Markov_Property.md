# Markov Property, Markov Decision Property

Markov Property는 무엇인가요?
: 현재가 주어졌을 때, 과거와 미래가 독립적임
: (t+1)번째의 state는 오직 t번째 state 및 action에만 의존
: ex) 내일 얻을 시험점수는 오직 현재 내 상태와 오늘 내가 공부하는 양에만 의존

Markov Decision Property(MDP)는 어떻게 정의되며, Markov 라는 표현이 쓰이는 이유를 어떻게 설명할 수 있을까요?
: MDP - 마르코프 의사결정 과정
:구성요소 - state의 집합, action의 집합, transition function, reward function

우리의 목적 : 기대되는 미래 보상의 합을 최대로 하는 최적 정책함수를 찾는것, but 현재 행동을 통해 얻어지는 보상뿐만 아니라 미래에 얻어지는 보상도 함께 고려해야 함

현실 속의 사건, 문제를 MDP로 표현해보는 예시를 들어볼 수 있을까요?
: 바둑
