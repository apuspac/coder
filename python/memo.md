## 入力処理
### 1つ
```python
# ex.N

# str
a = input()

# int
a = int(input)
```

### 空白区切り
```python
# ex.Hello Python

list_a = input.split()
# もしくは
a, b = input.split()

#int
list_a = list(map(int, input().split()))
# もしくは
a,b = map(int, input().split())
```

### 連続数値を行ごと列ごとに取得
ここらへんは臨機応変にsplit()とmapとintさえ使えれば、入力に関してはなんとかなる
```python
3
1 2
3 4
5 6

# 行ごと
n = int(input())
list_a = []
for i in range(n):
    list_a.append(list(map(int, input().split())))


# 列ごと
n = int(input())
list_a = []
list_b = []

for i in range(n):
    a,b = map(int, input().split())
    list_a.append(a)
    list_b.append(b)
```

## 出力処理
だいたい改行と空白区切りで出力。
```python
ans_list = [a, b, c]

print(*ans)
# もしくは
print(" ".join(map(str, ans)))
# joinは特定の文字列で引数のiterable(forで回せるlistのようなもの)を結合したものを返す


```



一般に、 P を並び替えて Q と等しくできるかどうかという問題を解く最も簡単な方法は、 P と Q を双方ソートしてその結果が同じになるかを調べる ( 同じになれば可能、そうでなければ不可能 ) というものです。