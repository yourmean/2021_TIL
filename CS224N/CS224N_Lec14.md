[CS224n] Lecture 14. Transformer & Self-attention

![](https://images.velog.io/images/yourmean/post/e2b385df-d58d-47b5-93f3-a3d2e9099833/image.png)

## 0. Attention Mechanism
어텐션 메커니즘은 자연어 기계번역을 위한 seq2seq 모델에 처음으로 도입되었다.
먼저 seq2seq 모델에서의 attention mechanisim에 대해 간략하게 짚고 넘어가자.

![](https://images.velog.io/images/yourmean/post/402056aa-a6b1-41db-bc47-021c49e57625/image.png)

## RNN, CNN, Self-attention의 비교
![](https://images.velog.io/images/yourmean/post/80519986-18c3-40d0-9411-8aa2477373d8/image.png)
Sequemce Modeling에서는 가변 길이의 data를 고정된 길이로 맞춰줘야 하는데, 이는 매 단계마다의 빠른 계산을 위해서이다.

![](https://images.velog.io/images/yourmean/post/8dda5544-bad0-4114-bbca-e4ecff77e0bc/image.png)
1. RNN 계열 Model
일반적으로 많이 쓰이는 모델 형태
단점?
	1. 병렬화(Paralleization) X
    	이전 토큰의 값이 hidden state로 넘어가야만 다음 토큰에 대한 계산이 가능하기 때문
	2. 여전히 long-tern dependency 반영 X
    
    
![](https://images.velog.io/images/yourmean/post/63fe36f8-1df6-49dd-bb30-afcb86b01b5c/image.png)
2. CNN 계열 Model
특징?
	1. 병렬화 O
    2. long-tern dependency 잘 반영 X
    	하지만 많은 layer를 필요로 한다. 

3. 그렇다면, Self-Attention은?
![](https://images.velog.io/images/yourmean/post/ab38643d-583a-4c65-bb81-ed8d04741553/image.png)
	1. 병렬화 O
    2. long-tern dependency 반영 O 
	    (why?각 token을 최단거리로 연결)
-> CNN, RNN을 대체할 수 있는 러닝 메커니즘!

4. RNN vs. CNN vs. Self-attention
![](https://images.velog.io/images/yourmean/post/df392f0c-b3bc-4500-910c-8dffe6467344/image.png)


## 1. Transformer
Transformer?
: self-attention mechanism을 극대화한 모델!
: sequential한 토큰을 sequential하게 처리하지 않기 때문에 병렬처리가 가능하다.

## 2. Image transformer & Local Self-attention
## 3. Music transformer & Relative Positional Self-attention








> ### Reference
https://medium.com/platfarm/%EC%96%B4%ED%85%90%EC%85%98-%EB%A9%94%EC%BB%A4%EB%8B%88%EC%A6%98%EA%B3%BC-transfomer-self-attention-842498fd3225 (seq2seq)
