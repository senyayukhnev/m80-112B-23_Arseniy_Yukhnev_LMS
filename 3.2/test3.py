n = int(input())
st = set()
for _ in range(n):
    s = str(input()).split()
    for j in s:
        st.add(j)
for i in st:
    print(i)
