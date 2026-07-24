
st = "programming is fun"

unique_chars = []
for c in st:
    if c not in unique_chars:
        print(c, st.count(c))
        unique_chars.append(c)



