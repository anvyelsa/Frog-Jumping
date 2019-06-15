# Frog-Jumping
A frog is currently at the point **0** on a coordinate axis **Ox**. It jumps by the following algorithm: the first jump is **a** units to the right, the second jump is **b** units to the left, the third jump is **a** units to the right, the fourth jump is **b** units to the left, and so on.

**Formally:**
- if the frog has jumped an even number of times (before the current jump), it jumps from its current position **x** to position **x+a;**
- otherwise it jumps from its current position **x** to position **x−b**.
Your task is to calculate the position of the frog after **k** jumps.

But... One more thing. You are watching **t** different frogs so you have to answer **t** independent queries.

## Input
The first line of the input contains one integer **t (1≤t≤1000)** — the number of queries.

Each of the next **t** lines contain queries (one query per line).

The query is described as three space-separated integers **a,b,k (1≤a,b,k≤10^9)** — the lengths of two types of jumps and the number of jumps, respectively.

## Output
Print **t** integers. The **i**-th integer should be the answer for the **i**-th query.

## example
- input
```python
6
5 2 3
100 1 4
1 10 5
1000000000 1 6
1 1 1000000000
1 1 999999999
```
- output
```python
8
198
-17
2999999997
0
1

```
### python3
```python
t=int(input())
for i in range(t):
    a,b,k=map(int,input().split())   
    if k%2==0:
        a=a*(k//2)
        b=b*(k//2)    
        print(a-b)
    elif k%2!=0:
        a=a*(k//2+1)
        b=b*(k//2)
        print(a-b)
```
    
