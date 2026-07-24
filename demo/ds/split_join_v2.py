st = "java,python,c#,javascript,sql"
langs = st.split(",")

new_st = ""
for lang in langs:
    new_st = new_st + lang.capitalize() + ";"

print(new_st[:-1])  # Remove last char
print(new_st.strip(";"))  # Remove last char