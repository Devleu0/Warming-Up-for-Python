# python 문자열 다루기
**[요약](#요약)**

## 1. 문자열 선언 및 초기화

문자열은 작은따옴표(`'`), 큰따옴표(`"`), 또는 삼중따옴표(`'''` 또는 `"""`)로 감싸서 선언한다. 삼중따옴표는 여러 줄에 걸친 문자열을 만들 때 유용하다.

```python
s1 = "Hello"
s2 = 'Python'
s3 = """This is a
multi-line string."""
s4 = str() # 빈 문자열
```

-----

## 2. 문자열 입력과 출력

  * **입력:** `input()` 함수를 사용하며, 입력받은 모든 것은 문자열로 취급
  * **출력:** `print()` 함수를 사용한다. f-string(f"...")을 사용하면 변수와 문자열을 편리하게 조합 가능

<!-- end list -->

```python
# 입력
name = input("이름을 입력하세요: ")

# 출력
print(name)
print(f"안녕하세요, {name}님!")
```

-----

## 3. 길이 확인

`len()` 내장 함수를 사용하여 문자열의 (문자 개수)를 확인한다.

```python
s = "Hello"
print(len(s)) # 5
```

-----

## 4. 문자 접근 (인덱스)

대괄호(`[]`)와 인덱스 번호를 사용하여 특정 위치의 문자에 접근한다. 인덱스는 **0부터 시작**한다. 음수 인덱스는 뒤에서부터 접근한다.

```python
s = "Hello"
print(s[0])   # 'H' (첫 번째 문자)
print(s[1])   # 'e' (두 번째 문자)
print(s[-1])  # 'o' (마지막 문자)
print(s[-2])  # 'l' (뒤에서 두 번째 문자)
```

**주의:** 문자열은 \*\*불변(immutable)\*\*하므로 `s[0] = 'J'`와 같이 인덱스를 통해 문자를 수정할 수는 없다.

-----

## 5. 부분 문자열 (substr)

**슬라이싱(slicing)** 구문 `[start:end:step]`을 사용한다. `end` 인덱스는 포함되지 않는다.

```python
s = "Hello, World!"
print(s[0:5])   # "Hello" (0부터 4까지)
print(s[:5])    # "Hello" (처음부터 4까지)
print(s[7:])    # "World!" (7부터 끝까지)
print(s[::2])   # "Hlo ol!" (처음부터 끝까지 2칸씩)
print(s[::-1])  # "!dlroW ,olleH" (문자열 뒤집기)
```

-----

## 6. 문자열 비교

비교 연산자(`==`, `!=`, `<`, `>`, `<=`, `>=`)를 사용한다. 비교는 유니코드(사전순)를 기준으로 한다.

```python
print("abc" == "abc") # True
print("abc" != "def") # True
print("abc" < "abd")  # True (c가 d보다 앞에 오므로)
print("A" < "a")      # True (대문자가 소문자보다 앞에 옴)
```

-----

## 7. 문자열 결합 및 추가

  * **결합:** `+` 연산자를 사용하여 두 문자열을 합친다.
  * **반복:** `*` 연산자를 사용하여 문자열을 반복한다.

<!-- end list -->

```python
s1 = "Hello"
s2 = " World"
s3 = s1 + s2
print(s3) # "Hello World"

s4 = "Hi" * 3
print(s4) # "HiHiHi"
```

-----

## 8. 삽입 (insert)

문자열은 불변이므로 직접 삽입은 불가능한다. 슬라이싱과 `+` 연산을 조합하여 새 문자열을 만듭니다.

```python
s = "Hllo"
index = 1
s_new = s[:index] + "e" + s[index:]
print(s_new) # "Hello"
```

-----

## 9. 삭제 (erase)

삽입과 마찬가지로 슬라이싱을 이용해 삭제할 부분을 제외하고 새 문자열

```python
s = "HeXllo"
index = 2 # 'X'의 위치
s_new = s[:index] + s[index+1:]
print(s_new) # "Hello"
```

-----

## 10. 교체 (replace)

`.replace(old, new)` 메소드를 사용하여 특정 부분 문자열을 다른 문자열로 교체한 **새 문자열을 반환**

```python
s = "Hello, world! world!"
s_new = s.replace("world", "Python")
print(s_new) # "Hello, Python! Python!"

# 세 번째 인자로 횟수를 지정할 수 있음
s_new_once = s.replace("world", "Python", 1)
print(s_new_once) # "Hello, Python! world!"
```

-----

## 11. 찾기 (find, rfind)

  * `.find(substring)`: 왼쪽에서부터 `substring`을 찾아 **첫 번째 인덱스**를 반환한다. 없으면 **-1**을 반환
  * `.rfind(substring)`: 오른쪽에서부터 `substring`을 찾아 **첫 번째 인덱스**를 반환한다. 없으면 **-1**을 반환

<!-- end list -->

```python
s = "hello, world! hello!"
print(s.find("hello"))  # 0
print(s.rfind("hello")) # 15
print(s.find("python")) # -1
```

**참고:** `.index()`와 `.rindex()`도 있지만, 찾는 문자열이 없으면 -1 대신 `ValueError`를 발생

-----

## 12. 특정 문자 찾기

`.find()`를 그대로 사용하거나, `in` 연산자를 사용하여 포함 여부(True/False)만 확인할 수 있다.

```python
s = "hello"
print(s.find('e')) # 1
print('e' in s)    # True
print('z' in s)    # False
```

-----

## 13. 구분자 기준 분리

`.split(delimiter)` 메소드를 사용하여 특정 구분자를 기준으로 문자열을 나눠 \*\*리스트(list)\*\*로 반환

```python
s = "apple,banana,orange"
fruits = s.split(',')
print(fruits) # ['apple', 'banana', 'orange']

s_space = "Hello World Python"
words = s_space.split() # 구분자를 생략하면 공백(스페이스, 탭, 엔터) 기준
print(words) # ['Hello', 'World', 'Python']
```

**반대:** `.join(list)`을 사용하면 리스트를 하나의 문자열로 합칠 수 있다.
`"-".join(fruits)`는 `"apple-banana-orange"`를 반환한다.

-----

## 14. 대소문자 변환

  * `.upper()`: 모두 대문자로
  * `.lower()`: 모두 소문자로
  * `.capitalize()`: 첫 글자만 대문자로
  * `.title()`: 각 단어의 첫 글자만 대문자로

<!-- end list -->

```python
s = "hello, world!"
print(s.upper())      # "HELLO, WORLD!"
print(s.lower())      # "hello, world!"
print(s.capitalize()) # "Hello, world!"
print(s.title())      # "Hello, World!"
```

-----

## 15. 문자열 뒤집기

슬라이싱의 `step`을 `-1`로 지정하는 것이 가장 간편한다.

```python
s = "hello"
s_reversed = s[::-1]
print(s_reversed) # "olleh"
```

-----

## 16. 공백 제거

  * `.strip()`: 양쪽 끝의 공백(및 지정 문자) 제거
  * `.lstrip()`: 왼쪽 끝의 공백(및 지정 문자) 제거
  * `.rstrip()`: 오른쪽 끝의 공백(및 지정 문자) 제거

<!-- end list -->

```python
s = "   Hello, World!   "
print(s.strip())  # "Hello, World!"
print(s.lstrip()) # "Hello, World!   "
print(s.rstrip()) # "   Hello, World!"

s_dots = "...hello..."
print(s_dots.strip('.')) # "hello"
```

-----

## 17. 문자열 비교 (대소문자 무시)

비교 전에 `.lower()` 또는 `.casefold()`를 사용하여 두 문자열을 모두 소문자로 변환한 후 비교한다. (`.casefold()`가 더 많은 유니코드 문자를 처리하므로 권장)

```python
s1 = "Hello"
s2 = "hello"
print(s1 == s2) # False
print(s1.lower() == s2.lower()) # True
print(s1.casefold() == s2.casefold()) # True
```

-----

## 18. 문자열을 숫자로 변환

  * `int(string)`: 정수로 변환
  * `float(string)`: 실수로 변환

<!-- end list -->

```python
s_num = "123"
s_float = "3.14"

num = int(s_num)
f_num = float(s_float)

print(num + 1)     # 124
print(f_num + 1.0) # 4.14
```

**주의:** "abc"나 "1.23"(int의 경우)처럼 변환할 수 없는 형태면 `ValueError`가 발생

-----

## 19. 숫자를 문자열로 변환

  * `str(number)`: 숫자를 문자열로 변환
  * f-string: 문자열 포매팅을 이용

<!-- end list -->

```python
num = 123
f_num = 3.14

s1 = str(num)
s2 = str(f_num)
s3 = f"{num}"

print(s1 + " is a string") # "123 is a string"
print(s3) # "123"
```

-----

## 20. 반복자 기반 접근

문자열은 순회 가능한(iterable) 객체이므로 `for` 루프를 사용하여 각 문자에 순서대로 접근 가능

```python
s = "abc"
for char in s:
    print(char)
# 'a'
# 'b'
# 'c'
```

-----

## 21. 문자열 정렬

문자열 자체는 정렬할 수 없다. `sorted()` 함수를 사용하면 문자열을 문자 단위로 정렬한 **새 리스트**를 반환한다. 정렬된 *문자열*을 얻으려면 `"".join()`을 사용해야 한다.

```python
s = "bcade"

# 1. 정렬된 리스트 얻기
sorted_list = sorted(s)
print(sorted_list) # ['a', 'b', 'c', 'd', 'e']

# 2. 정렬된 문자열 얻기
sorted_string = "".join(sorted_list)
print(sorted_string) # "abcde"

# 3. 역순 정렬
reverse_sorted_string = "".join(sorted(s, reverse=True))
print(reverse_sorted_string) # "edcba"
```

# 요약

| 기능 | 주요 코드 / 문법 | 설명 및 예시 |
| :--- | :--- | :--- |
| **문자열 초기화** | `s = """Multi-line"""` | 작은따옴표(`'`), 큰따옴표(`"`), 삼중따옴표(`"""..."""`)로 생성 |
| **문자열 입출력** | `s = input()` <br> `print(s)`| `input()`으로 입력 (문자열로 받음), `print()`로 출력 |
| **길이** | `len(s)` | 문자 개수를 반환 (예: `len("Hi")` -\> 2) |
| **문자 접근** | `s[0]` <br> `s[-1]` | 0부터 시작하는 인덱스로 문자에 접근. 음수 인덱스는 뒤에서부터 접근 |
| **부분 문자열** | `s[start:end]` | 슬라이싱. `start`부터 `end-1`까지의 부분 문자열을 반환 |
| **비교** | `==`, `!=`, `<`, `>` | 사전순(유니코드)으로 두 문자열을 비교한다. |
| **결합 및 추가** | `s1 + s2` <br> `s * 3` | `+` 연산자로 두 문자열 결합 `*` 연산자로 문자열을 반복 |
| **삽입** | `s[:idx] + "char" + s[idx:]` | 문자열은 불변(immutable)하므로, 슬라이싱을 이용해 새 문자열을 생성|
| **삭제** | `s[:idx] + s[idx+1:]` | 삭제할 문자를 제외하고 슬라이싱을 이용해 새 문자열을 생성 |
| **교체** | `s.replace(old, new)` | 문자열 내의 `old`를 `new`로 교체한 **새 문자열**을 반환 |
| **찾기** | `s.find(sub)` <br> `s.rfind(sub)` | `sub` 문자열의 시작 인덱스를 반환. 없으면 **-1**을 반환. `rfind`는 오른쪽부터 |
| **특정 문자 찾기** | `char in s` <br> `s.find(char)` | `in` 연산자는 포함 여부(True/False)를 반환. `find`는 인덱스를 반환 |
| **구분자로 분리** | `s.split(delimiter)` | `delimiter` 기준으로 나누어 \*\*리스트(list)\*\*로 반환. (예: `"a,b".split(',')` -\> `['a', 'b']`) |
| **대소문자** | `.upper()` <br> `.lower()` <br> `.capitalize()` | 각각 '전부 대문자', '전부 소문자', '첫 글자만 대문자'로 변환|
| **뒤집기** | `s[::-1]` | 슬라이싱의 `step` 값을 `-1`로 |
| **공백 제거** | `.strip()` <br> `.lstrip()` <br> `.rstrip()` | 양쪽, 왼쪽, 오른쪽 의 공백(또는 지정 문자)을 제거 |
| **비교 (대소문자 무시)** | `s1.lower() == s2.lower()` | `.lower()` (또는 `.casefold()`)를 사용해 모두 소문자로 변경 후 비교 |
| **숫자로 변환** | `int(s)` <br> `float(s)` | 문자열을 정수또는 실수로 변환 |
| **숫자를 변환** | `str(num)` <br> `f"{num}"` | `str()` 함수 또는 f-string을 사용하여 숫자를 문자열로 변환 |
| **반복자 기반 접근** | `for char in s:` | `for` 루프를 사용하여 문자열의 각 문자를 순서대로 순회|
| **문자열 정렬** | `"".join(sorted(s))` | `sorted(s)`는 문자를 정렬한 **리스트**를 반환. `"".join()`으로 다시 문자열 |

