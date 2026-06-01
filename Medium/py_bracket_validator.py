def bracket_validator(s: str) -> bool:
    l =["(", ")", "[", "]", "{", "}"]

    for chari in s:
        if chari not in l:
            s = s.replace(chari,"")
        s = s.replace("()", "")
        s = s.replace("[]", "")
        s = s.replace("{}", "")
    return s == ""
    

print(bracket_validator("(234 ) qw23 4eqw fw ef[ef (){}[][]] ewf23 f{}e 42 2423"))