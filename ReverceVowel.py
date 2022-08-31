var_a="hellotyeog"
vowel_char=""
for i in var_a:
    if i in "aeiouAEIOU":
        vowel_char+=i
var_x=""
for j in var_a:
    if j in "aeiouAEIOU":
        var_x+=vowel_char[-1]
        vowel_char=vowel_char[:-1]
    else:
        var_x+=j
print(var_x)

















    



