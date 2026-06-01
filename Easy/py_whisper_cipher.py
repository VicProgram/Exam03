def whisper_cipher(text: str, shift: int) -> str:
        
    res = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                start = ord('a')
            else:
                start = ord('A')
            newch = chr((ord(char) - start + shift) % 26 + start)
            res += newch
        else:
            res += char

    return res


print(whisper_cipher("xyzabc123", 1))