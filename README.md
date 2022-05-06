![shakelogo](https://user-images.githubusercontent.com/96969568/167048056-bb3829a4-55e3-4513-8a99-7d5143d2fbe9.png)

## 한국어 가이드

#### Shake가 무엇이죠?
Shake는 파이썬으로 작성된, 일본 지진방재 모듈입니다.
<br/>
<br/>
#### Shake를 어떻게 사용하죠?
지금부터 간단한 예제를 통해 shake의 사용법을 안내해드리겠습니다.
<br/>
만약 지금 Shake를 통해 Level을 불러오려고 한다면 다음 코드를 사용해주십시오.
<br/>
```python
#shake를 import 합니다.
import shake

#level을 shake의 kel 클래스의 lv 함수로 지정합니다.
level = await shake.kel.lv()

#결과를 출력합니다.
print(level)
```
