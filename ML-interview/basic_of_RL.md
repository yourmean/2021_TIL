# Agent, Environment, State, Observation, Action, Reward, Policy

강화 학습은 기계 학습의 한 종류입니다. 풀고자 하는 문제는 "Agent가 Environment안에서 Reward를 최대화 하는 최적의 Action을 수행하는 것" 입니다.

Agent: 문제 공간 안에서 Action을 취하는 본체입니다. 때로는 여러 명일 때가 있죠.

Environment: Agent의 법칙을 제어하며, Agent가 행동할 수 있는 환경 전체를 의미합니다.

State: Environment와 Agent의 상태를 나타내는 값입니다. 움직이는 물체라면 위치와 속도 정보 등이 될 것입니다.

Observation: Environment가 바라본 Agent와 그의 주변 State를 의미합니다.

Action: Agent가 지금 이 순간 할 수 있는 행동을 의미합니다. 문제 형태에 따라 Finite/Infinite & Discrete/Continuous 성질이 나뉩니다.

Reward: Agent가 어떤 State에서 어떤 Action을 취했을 때의 순간 보상입니다. 이걸 먼 미래까지 누적시킨 값은 Return이라고 부릅니다.

Policy: Agent의 "뇌" 입니다. 현재 State를 통해서 Action을 판단하는 친구입니다.

여러 용어가 나와서 헷갈리시죠! 이걸 알파고에 빗대서 바라보죠. Agent는 "바둑 기사"가 될 것입니다. Environment는 바둑의 규칙 세계관인 "바둑판"이 될 것입니다. State는 바둑판의 현재 상태와 그 순간의 플레이어가 자신인지, 상대방인지를 표현할 것입니다.
Observation은 바둑판이 무슨 상태인지, 누가 몇 집을 땄는 지 등을 의미하죠. Action은 기사가 바둑알을 놓는 행위 자체를 의미합니다. 이 때 가능한 행동들에는 "바둑 세계관"을 어기지 않는 곳들에 한정되겠죠? 이것을 Action Space라고 합니다. Reward 같은 경우는 승리에 가까워 지는 정도가 될 수 있을 것입니다. Policy는 결국 "바둑 기사가 바둑판을 바라보면서 이번에 어디에 놓을 지를 결정"해주는 역할을 할 것입니다.

강화학습은 이런 개념을 가장 기본적으로 가지고 있으며, 결국 최적의 Policy, 즉 최고의 Reward를 받을 수 있도록 하는 방법을 찾는 것이 목표라고 할 수 있습니다.

문제의 성격에 따라서 때로는 Observation이 partial할 수도 있으며, State나 Action이 discrete하거나 continuous할 수 있고, Agent가 여러 명일 수도 있습니다. 이런 것들에 대해 하나씩 배워나가보도록 하죠 ㅎㅎㅎ

