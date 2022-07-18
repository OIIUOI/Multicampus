# 파이썬 에러/예외 처리

## 디버깅

제어가 되는 시점

- branches : 모든 조건이 원하는대로 동작하는지
- for loops : 반복문에 진입하는지, 원하는 횟수만큼 실행되는지
- while loops : for loops와 동일, 종료조건이 제대로 동작하는지
- function : 함수 호출시, 함수 파라미터, 함수 결과

디버깅 방법

- print 함수 활용
- **개발 환경에서 제공하는 기능 활용 (Run and Debug)**
- python tutor 활용
- 뇌컴파일, 눈디버깅

## 에러와 예외

### 문법 에러(Syntax Error)

^ 기호를 통해 에러가 발생한 위치 표시

```python
  File "c:\Users\이주용\Desktop\python\print.py", line 1
    print("hello)
          ^
SyntaxError: unterminated string literal (detected at line 1)
```

- EOL (End of Line) 라인 끝

- EOF (End of File) 파일 끝

### ZeroDivisionError

0으로 못 나눈다

```python
  File "c:\Users\이주용\Desktop\python\print.py", line 1, in <module>
    print(10/0)
ZeroDivisionError: division by zero
```

### NameError

변수가 선언되지 않았을 때

```python
  File "c:\Users\이주용\Desktop\python\print.py", line 1, in <module>
    print(hello)
NameError: name 'hello' is not defined. Did you mean: 'help'?
```

### TypeError

자료형 불일치, 충돌

```python
  File "c:\Users\이주용\Desktop\python\print.py", line 1, in <module>
    print(1 + '1')
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

함수 argument 부족, 초과

```python
  File "c:\Users\이주용\Desktop\python\print.py", line 2, in <module>
    random.sample()
TypeError: Random.sample() missing 2 required positional arguments: 'population' and 'k'
```

### ValueError

타입은 올바르나 값이 적절하지 않거나 없는 경우

```python
  File "c:\Users\이주용\Desktop\python\print.py", line 1, in <module>
    int('3.5')
ValueError: invalid literal for int() with base 10: '3.5'

  File "c:\Users\이주용\Desktop\python\print.py", line 1, in <module>
    range(3).index(6)
ValueError: 6 is not in range
```

### IndexError

```python
  File "c:\Users\이주용\Desktop\python\print.py", line 2, in <module>
    list = []
    list[2]
IndexError: list index out of range
```

### KeyError

```python
  File "c:\Users\이주용\Desktop\python\print.py", line 2, in <module>
    list = {'사과' : 'apple'}
    list['바나나']
KeyError: '바나나'
```

### ModuleNotFoundError

```python
  File "c:\Users\이주용\Desktop\python\print.py", line 1, in <module>
    import none
ModuleNotFoundError: No module named 'none'
```

### ImportError

모듈은 있으나 존재하지 않는 클래스/함수를 가져오는 경우

```python
  File "c:\Users\이주용\Desktop\python\print.py", line 1, in <module>
    from random import samp
ImportError: cannot import name 'samp' from 'random' 
```

### IndentationError

Indentation이 적절하지 않는 경우

```python
  File "c:\Users\이주용\Desktop\python\print.py", line 2
    for i in range(3)
    print(i)
    ^
IndentationError: expected an indented block after 'for' statement on line 1
```

### KeyboardInterrupt

의도적으로 코드의 실행을 중단시켰을 시

ctrl + c 중지

```python
  File "c:\Users\이주용\Desktop\python\print.py", line 2, in <module>
    while True:
        print(1)
KeyboardInterrupt
```

### [파이썬 내장 예외](https://docs.python.org/ko/3/library/exceptions.html#exception-hierarchy)

<img src="file:///C:/Users/jin47/AppData/Roaming/marktext/images/2022-07-19-02-10-41-image.png" title="" alt="" width="713">

## 예외처리(Exception)

try문(statement) / except 절(clause)을 이용하여 예외 처리를 할 수 있음

- try 문
  
  - 오류 발생 가능성이 있는 코드를 실행
  
  - 예외가 발생되지 않으면 except 없이 실행 종료

- except 문
  
  - 예외가 발생하면 except 절이 실행
  
  - 예외 상황을 처리하는 코드를 받아서 적절한 조취를 취함

- else : try문에서 예외가 발생하지 않으면 실행함

- finally : 예외 발생 여부와 관계없이 항상 실행

![](C:\Users\jin47\AppData\Roaming\marktext\images\2022-07-19-02-15-24-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2022-07-19-02-15-48-image.png)

예외처리 예시

```python
num = input()
try:
    resul = 100/int(num)
except ZeroDivisionError as err:
    print(err) # division by zero
    print("0으로 나눌 수는 없습니다.")
except ValueError:
    print("숫자 형식을 입력해주세요")
except Exception:
    print("오류")
else:
    print(result)
finally:
    print("나누기를 종료합니다")
```

## 예외 발생 시키기

- raise를 통해 예외를 강제로 발생

```python
raise <표현식>(메시지)
```

![](C:\Users\jin47\AppData\Roaming\marktext\images\2022-07-19-02-19-31-image.png)
