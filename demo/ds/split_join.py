st = "java,python,c#,javascript,sql"
langs = st.split(",")

for idx, lang in enumerate(langs):
    langs[idx] = lang.capitalize()

new_st = ";".join(langs)
print(new_st)