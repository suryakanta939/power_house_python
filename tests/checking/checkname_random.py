import names

fn=names.get_first_name(gender="male")
print("first name is "+fn)
ln=names.get_last_name()
print(f"last name is {ln} ")
fnl=names.get_first_name(gender="female")
print(fnl)
fullnamemale=names.get_full_name(gender="male")
print(fullnamemale)
fullnamefemale=names.get_full_name(gender="feamale")
print(fullnamefemale)
