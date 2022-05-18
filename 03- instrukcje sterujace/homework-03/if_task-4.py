variable = "hakunamatata"

if len(variable) > 5 and variable.find("a") != -1:
    variable = variable.replace("a", "z")
    print(variable)