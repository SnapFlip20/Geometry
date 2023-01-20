# Geometry
## Point
* 새로운 point 객체 선언
```python
a = point(1)
b = point(1, 2)
c = point(1, 2, 3)
print(a, b, c)

# >>> point(1, 0, 0) point(1, 2, 0) point(1, 2, 3)
```
```python
a = point((1))
b = point([1, 2])
c = point(point(1, 2, 3))
print(a, b, c)

# >>> point(1, 0, 0) point(1, 2, 0) point(1, 2, 3)
```
* 수치 연산
    * 두 점 사이의 거리
    ```python
    point.dist(a, b) # 두 점 사이의 유클리드 거리
    point.dist2(a, b) # 두 점 사이의 유클리드 거리 제곱
    point.dist_taxi(a, b) # 두 점 사이의 택시 거리
    ```
    * 대칭 이동
    ```python
    point.flipx(a) # x축에 대하여 대칭 이동
    point.flipy(a) # y축에 대하여 대칭 이동
    point.flipz(a) # z축에 대하여 대칭 이동
    point.flipxy(a) # xy평면에 대하여 대칭 이동
    point.flipxz(a) # xz평면에 대하여 대칭 이동
    point.flipyz(a) # yz평면에 대하여 대칭 이동
    point.flipxyz(a) # point(0, 0, 0)에 대하여 대칭 이동(= -point(a))
    ```
    * 평행 이동
    ```python
    a.move(1) # x축으로 1만큼 평행 이동 
    a.move(1, 1) # x, y축으로 1만큼 평행 이동 
    a.move(1, 1, 1) # x, y, z축으로 1만큼 평행 이동 
    ```
    * 두 점 사이의 기울기
    ```python
    point.slope(a, b) # y축에 평행한 경우 inf 반환
    ```
    * 특정 좌표 기준 거리가 가까운 순으로 정렬
    ```python
    point.sort_closest(point_lst, main_point)
    ```
    * 특정 좌표 기준 반시계방향으로 정렬
    ```python
    point.sort_acw(point_lst, main_point)
    ```
  
## Vector
* 새로운 vector 객체 선언
```python
a = vector(1)
b = vector(1, 2)
c = vector(1, 2, 3)
print(a, b, c)

# >>> vector(1, 0, 0) vector(1, 2, 0) vector(1, 2, 3)
```
```python
a = vector((1))
b = vector([1, 2])
c = vector(vector(1, 2, 3))
print(a, b, c)

# >>> vector(1, 0, 0) vector(1, 2, 0) vector(1, 2, 3)
```
* 두 point 객체를 잇는 벡터 생성
```python
a = point(1, 2, 3)
b = point(2, -3, 1)
ab = vector.to_vector(a, b)
print(ab)

# >>> vector(1, -5, 2)
```

* 수치 연산
    * 벡터합
    ```python
    a = vector(1, 2, 3)
    b = vector(2, -3, 1)
    print(a+b, a-b)

    # >>> vector(3, -1, 4) vector(-1, 5, 2)
    ```
    * 스칼라곱
    ```python
    a = vector(1, 2, 3)
    print(a*3, 2*a)
    print(a/3)

    # >>> vector(3, 6, 9) vector(2, 4, 6)
    # >>> vector(0.3333333333333333, 0.6666666666666666, 1.0)
    ```
    * 절댓값(벡터의 크기)
    ```python
    a = vector(1, 2, 3)
    print(abs(a), a.size())

    # >>> 3.7416573867739413 3.7416573867739413
    ```
    * 두 벡터가 이루는 각(단위: degree)
    ```python
    a = vector(1, 2, 3)
    b = vector(-1, -3, 2)
    print(vector.angle(a, b))

    # >>> 94.09604375815233
    ```
    * 두 벡터가 이루는 삼각형의 넓이
    ```python
    a = vector(1, 2, 3)
    b = vector(-1, -3, 2)
    print(vector.area3(a, b))

    # >>> 1.0580798500470525
    ```
    * 두 벡터가 이루는 평행사변형의 넓이
    ```python
    a = vector(1, 2, 3)
    b = vector(-1, -3, 2)
    print(vector.area4(a, b))

    # >>> 2.116159700094105
    ```
    * 두 벡터의 외적
    ```python
    a = vector(1, 2, 3)
    b = vector(-1, -3, 2)
    print(vector.cross(a, b))

    # >>> vector(13, 0, -1)
    ```
    * 두 벡터의 내적
    ```python
    a = vector(1, 2, 3)
    b = vector(-1, -3, 2)
    print(vector.dot(a, b))

    # >>> -1
    ```
    * 역벡터
    ```python
    a = vector(-2, 1, 3)
    print(a.reverse())

    # >>> vector(2, -1, -3)
    ```
    * 영벡터
    ```python
    print(vector.zero())

    # >>> vector(0, 0, 0)
    ```
