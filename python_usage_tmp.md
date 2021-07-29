# 코루틴(coroutine)

메인루틴 - 코루틴

## - 코루틴에 값 전달하기

next는 코루틴의 코드를 실행하지만 값을 보내지 않을 때 사용

send는 값을 보내면서 코루틴의 코드를 실행할 때 사용

```python
코루틴객체.send(값)
변수 = (yield)
```

```python
def number_coroutine():
    while True: # 코루틴을 계속 유지하기 위해 무한루프 사용
        x = (yield) # 코루틴 바깥에서 값을 받아옴.
        print(x)

co = number_coroutine()
next(co)    # 코루틴 안의 yield까지 코드 실행(최초 실행)

co.send(1)  # 코루틴에 숫자 1을 보냄
co.send(2)  # 코루틴에 숫자 1을 보냄
co.send(3)  # 코루틴에 숫자 1을 보냄
```
실행 결과
```
1
2
3
```

## - 코루틴 밖으로 값 전달

```python
def sum_coroutine():
    total = 0
    while True:
        x = (yield total)   # 코루틴 바깥에서 값을 받아오면서 바깥으로 값을 전달
        total += x

co = sum_coroutine()
print(next(co)) # 0: 코루틴 안의 yield까지 코드를 실행하고 코루틴에서 나온 값 출력

print(co.send(1)) # 1: 코루틴에 숫자 1을 보내고 코루틴에서 나온 값 출력
print(co.send(2)) # 3: 코루틴에 숫자 2를 보내고 코루틴에서 나온 값 출력
print(co.send(3)) # 6: 코루틴에 숫자 3을 보내고 코루틴에서 나온 값 출력
```
실행 결과
```
0
1
3
6
```

## - 제너레이터 vs 코루틴

제너레이터는 next함수( `__next__` 메서드 )를 반복 호출하여 값을 얻어내는 방식

코루틴은 next함수를 한번만 호출한 뒤 send로 값을 주고 받는 방식


## - 코루틴 종료

### * `close()`

코루틴은 `while True:`를 사용하여 무한 루프로 동작하지만

close() 메서드를 사용하면 강제로 종료됨

종료시 GeneratorExit 예외 발생

코루틴 안에 예외를 발생시키려면

```python
co.throw(RuntimeError, '예외로 끝내기')
```

## - 하위 코루틴 값 가져오기

### * `yield from` 사용

```python
def accumulate():
    total = 0
    while True:
        x = (yield)
        if x is None:
            return total # total을 반환하고 코루틴을 끝냄
        total += x

def sum_coroutine():
    while True:
        total = yield from accumulate() # accumulate의 반환값을 가져옴
        print(total)

co = sum_coroutine()
next(co)

for i in range(1, 11):
    co.send(i)

co.send(None)

for i in range(1, 101): 
    co.send(i) # accumulate가 끝나면 yield from으로 다시 실행

co.send(None)
```
실행 결과
```
55
5050
```

<br><br><br><br><br>
<hr>
<br><br><br><br><br>

# asyncio

## - 기본 사용법 loop

```python
async def funcName():
    code
```

```python
import asyncio

async def hello(): # async def로 네이티브 코루틴을 만듬
    print('hello, world!')

loop = asyncio.get_event_loop() # 이벤트 루프를 얻음
loop.run_until_complete(hello()) # hello가 끝날 때까지 기다림. 파라미터로 코루틴 객체
loop.close() # 이벤트 루프를 닫음
```
실행 결과
```
hello, world!
```

## - await (3.5이상)

네이티브 코루틴 안에서만 사용할 수 있음

```python
import asyncio

async def add(a, b):
    print('add: {0} + {1}'.format(a, b))
    await asyncio.sleep(1.0) # 1초 대기. asyncio.sleep도 네이티브 코루틴
    return a + b

async def print_add(a, b):
    result = await add(a, b)  #await로 코루틴 안에서 다른 네이티브 코루틴 실행하고 반환값을 저장
    print("print_add: {} + {} = {}".format(a, b, result))


loop = asyncio.get_event_loop()
loop.run_until_complete(print_add(1, 2))
loop.close()
```
실행 결과
```
add: 1 + 2
print_add: 1 + 2 = 3
```

## - blocking I/O 함수

결과가 나올 때까지 코드 실행이 중단(block)이 되는데 이러한 함수들을 블로킹 I/O 함수라고 함

네이티브 코루틴 안에서 블로킹 I/O 함수를 실행하려면 이벤트 루프의 run_in_executor 함수를 사용하여 스레드에서 병렬로 실행시켜야 함

run_in_executor의 첫번째 인수는 executor인데 함수를 실행시켜줄 스레드 풀 또는 프로세스 풀임

run_in_executor도 네이티브 코루틴이므로 await로 실행한 뒤 결과를 가져옴

### * loop.run_in_executor()
### * asyncio.ensure_future()
### * asyncio.gather


## - async with (3.5 이상)

클래스나 함수를 비동기적으로 처리한 뒤 결과를 반환

```python
async with 클래스() as 변수:
    코드
```

`__aenter__`와 `__aexit__` 메서드를 구현해야함

```python
class 클래스이름:
    async def __aenter__(self):
        code...

    async def __aexit__(self, exc_type, exc_value, traceback):
        code...
```


## - async for

비동기로 반복하는 문법

`__aiter__`와 `__anext__` 메서드 구현해야함


## - ???

```python
from time import time
from urllib.request import Request, urlopen
import asyncio

urls = ['https://www.google.co.kr/search?q=' + i
        for i in ['apple','pear','grape','pineapple','orange','strawberry']]

async def fetch(url):
    request = Request(url, header={'User-Agent':'Mozilla/5.0'})
    response = await loop.run_in_executor(None, urlopen, request)
    page = await loop.run_in_executor(None, response.read)
    return len(page)


async def main():
    futures = [asyncio.ensure_future(fetch(url)) for url in urls]

    result = await asyncio.gather(*futures)
    print(result)

begin = time()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
end = time()
print('실행 시간: {0: .3f}초'.format(end - begin))
```