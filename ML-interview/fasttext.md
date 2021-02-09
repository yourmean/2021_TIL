# Fasttext

오늘은 Fasttext에 대해 알아봅시다! Fasttext는 앞서 Word2Vec에서 설명했던 것과 같이 "단어"수준 임베딩 기법입니다. Fasttext가 Word2Vec과 다른 점은 각 단어 단위를 문자 단위 n-gram으로 표현한다는 점이죠! 이 밖의 내용은 Word2Vec과 같습니다. (이 말이 무슨 뜻이냐! 단어를 Bag-of-characters로 보고 개별 단어가 아닌 n-gram의 character들을 embedding(skip-gram) 하는겁니다.)

그렇다면, 모델 기본 구조에 대해 하나씩 알아볼까요? 위에서 "단어를 Bag-of-characters로 보고 개별 단어가 아닌 n-gram의 character들을 embedding(skip-gram) 하는것"이라고 했죠! Bag-of-characters란 무엇일까요? 하나의 단어를 character단위 여러개로 잘라서 벡터를 계산하는 것을 말합니다. 그럼 n-gram의 character는 무엇이냐 예를 들어볼게요. n=3일 때, hello를 표현하면, <he, hel, ell, llo, lo> 로 표현 됩니다. 이 때, <와 >는 단어의 경계를 나타내기 위해 Fasttext모델이 사용하는 특수 기호입니다. 

Fasttext 모델에서는 임베딩을 문자단위 n-gram의 합으로 표현합니다. Fasttext모델 역시 negative sampling기법을 씁니다. 조건부 확률을 최대화 하는 과정에서 학습이 되는 것이죠. 여기까지는 Word2Vec과 같은 내용입니다. 하지만 Fasttext는 여기서 타겟 단어, 문맥 단어 쌍을 학습 할 때 타겟 단어에 속한 문자 단위 n-gram 벡터를 모두 업데이트 하게 됩니다. 

Fasttext 모델은 negative sample 단어 쌍에 대해 정의된 조건부 확률을 최대화 해야합니다. 다시 말해서, negative sample을 모델에 입력하면 모델은 이 데이터가 정말로 negative sample이라고 맞춰야 하는 것이죠. 예를 들어, hello가 타깃 단어 fork가 문맥의 네거티브 샘플이라면 <he, hel, ell, llo, lo>같은 n-gram 벡터들 각각을 fork에 해당하는 단어 벡터와 유사도를 낮추는 것이죠!

더 자세한 내용과 수식에 대해서는 한번씩 찾아봅시당!!
