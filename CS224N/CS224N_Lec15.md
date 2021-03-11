# [CS224n] Lecture 15. Language Generation

많은 nlp 모델에 자연어 생성이 사용되고 있음

### recap
언어 모델: 언어의 시퀀스를 생성하는 모델
컨디셔널 언어 모델링: 시퀀스 뿐만 아니라, 또다른 변수들도 인풋으로 주어 다음에 올 단어 등을 예측하는 conditional한 랭귀지 모델 -> 기계번역, 요약
기계번역에서는 
summarization:x가 원본, y는 발화자/수신자

## Decoding Algorithm
우리가 뽑고 싶은 건 분포로부터의 단어
1. greedy decoding : 매스텝마다 활률분포에서 최대가 되는 word를 output
 -> 백트래킹 불가(여러개의 시퀀스를 동시에 고려하는 것이 불가)->불안정
2. 이그저스티브 -> 실현 불가능(메모리상)
3. 빔 서치(두개절충) -> 디코딩 알고리즘

빔 서치의 특징 -> 멀티 시퀀스를 동시에 트래킹 가능

빔서치보다 일반적으로 효율적인 것 -> 샘플링 베이스드
지금까지는 


### Sampling-Based Decoding
1. 퓨어 샘플링
 : 확률분포로부터 단순하게 확률을 샘플링
2. 탑 앤 샘플링
 : top-n , 확률이 가장 높은 세 가지 중에서 랜덤 샘플링
 : n size가 클수록 다양성은 증가하지만, risk도 함께 증가
 : n size가 작다면, 보다 안정적이고 generic한 문장 생성
-> generic함이 덜하고, 다양성이 올라감 

### Softmax temperature
언어 모델에서 워드의 스코어를 구하고, 마지막에 소프트맥스에 넣어서 최종 아웃풋으로
-> 타우 값 넣어서 벡터를 만들어주면
-> 타우를 키우면 분포가 유니폼해짐
-> 조절에 따라 아웃풋되는 텍스트의 ~~를 변경 가능


## NLG task에 어떻게 신경망 적용?
1. summarization
정의: text x가 주어졌을 때, 요약본 만들어내는 task
single, multi document에 대해서 , 물론 멀티가 더 어려움
요약의 2종류
1) Extractive summarization
2) Abstractive summarization

신경망 이전은 대부분 1), 파이프라인이 명확하게 정해져 있었음
sentence를 스코어링, 그래프 기반으로 구조(문장간 연결관계 등) 찾는 알고리즘도 사용할 수 있음
컨텐츠 뽑아낼 때는? tf-idf (maybe)

*ROUGE*
BLEU와의 비교
counting 기반, 
모델의 output/인간 번역(정답) 문장 : 타겟 -> 여기의 n gram 개수
-> 매칭되는 것의 개수를 세어 rPt
-> BLEU는 recall base, 루지는 ~
-> B는 평균, 루지는 따로따로


translation - attention을 함께 활용한 모델을 활용
neoral summarization

### 1. copy mechanisms
디테일적인 부분을 카피하는 데에 좋지 않았음
희박하거나 새로 등장하는 단어들을 우리의 summarization에 녹여내는 것이 어려웠음



![](https://images.velog.io/images/yourmean/post/f0cdb507-bb7b-46e1-a9c8-16fa8910d1ab/image.png)
 마지막에 ~?? 수식 모르게씀
 
 ### Pointer-Generator Networks
 1. Pointer-Generator Networks
 : pointing 개념을 통해, ~태그로부터 새로운 단어를 카피할 수 있게 함
 2. Coverage vector
 : 반복을 효율적으로 제거함
 
 ![](https://images.velog.io/images/yourmean/post/d71e0609-5df7-480d-b3ef-52d14c789691/image.png)
 여기에서는, 기본 vocab distribution에 추가로 attention~까지 쓴다
 복사 -어텐션, 생성-현재
(이해 RE) 
지금까지도 어텐션을 많이 했는데, 현재 스텝에서도 또 어텐션을 해버리면 loss가 너무 커진다 -> 이번 단계에서 패널티를 주자(그럴싸함)
-> repeat되는 비율을 줄이자

문제점? 
1)너무 많이 copy하면 extractive 해짐
2)input이 길어질수록, 전반적 문맥 고려해서 적당한 ~selection에 어려움이 있었음

### Botton-up summarization
1) content selection
2) bottom-up attention
마스크를 씌워서 포함하지 않기로 한 애들 냅두고, 남은 애들로만 attention을 통해 최종 summary를 하는 방식..?

### Summarization vs. Reinforcement Learning
강화학습을 통해 policy 최적화
목적함수: 기존의 접근에서는 x,y가 주어졌을때 -로그가능도의 합


### Dialogue
1)task-oriented
2) social dialogue
-뉴럴넷 전에는, 매핑 딕셔너리 만들어두고 
-이제는 오픈 핸디드(미리 정해져있지 않은)
결점? ) 고질적인 문제들, 너무 generic하고, 문맥상 irrelevant한 말, 지나치게 repetition하거나, ~
-> 각각을 해결하는 방법
	1)부적절한 반응: 우리의 기존 목적함수 말고 
    2) 단순히 좀 안 등장하는 애의 웨이트를 늘려주자, sampling기반 방법쓰면 다양성 up, 좀 복잡하지만 아예 additional한 content를 가지고 디코딩 과정에서 해보자, 아예 생판 밑바닥부터 생성하기는 어려울 수 있으니, 인간이 이미 만들어 둔 대화/발화에 대해 검색/접근을 통해 다듬어서 쓰는 방법도 가능
    3) 커버리지 메커니즘(지금까지 나온 점수들 누적해서 로스로 반영), 새로운 목적함수(반복에 대해 페널티 주도록),
    4) 챗봇의 인격에 관한 일관성 부재는 -> persona embedding, 인격까지 같이 레이블링 된 데이터셋 써라
    

### Storytelling
이미지가 주어졌을 때, 스토리텔링
문제점?) 스토리텔링의 경우, 이걸로부터 생성하는 paragraph가 잘 없음, 그래서 
idea-> sentence를 인코딩하자!
일반적인 단어에 학습된 임베딩을 사용하자!
-> 먼저, 이미지 캡션 데이터셋을 사용함
일반적인 표현을 매핑 
skip-thoght vectors

![](https://images.velog.io/images/yourmean/post/dd194b1f-fe20-46cc-8baf-593034a96036/image.png)
### Callenges in storytelling
줄거리가 없음!
당연한거임. 우리 모델은 워드의 시퀀스인데, 스토리는 이벤트의 시퀀스니까
-> 추상적인 event들이 묶여있는것임
-> 앞으로 개선하려면 event를 modeling하는 것을 고려해야 함


## 4. NLG Evaluation and Difficulties

기계번역에서 그나마 나음(답이 정해져 있으니까), 그런데도 최선은 아님
근데 summarization이나 dialogue(open handed) task의 경우는 인간의 평가와는 상당히 다른 모습을 보임
1) perplexity
2) 
