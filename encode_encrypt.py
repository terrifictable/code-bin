import codecs


amt = 2 # how often it will get encoded
code = """import os; print(f'Hello from: {os.getenv("COMPUTERNAME")}')""" # What you want to encode in here


# Encode Function
def enc(code):
    return codecs.encode(bytes(code, 'utf-8'), 'base64').decode('utf-8').replace("\n", "") # The encoding it self


if amt > 13: # after 13x encoding the base64 code will be too long to be displayed (at least in visual studio code) so it just returns to 13 if the amt is bigger. Just comment it out if you dont like it
    amt = 13

for i in range(amt): # *loop*
    encoded_code = enc(code) # encode the code from above
    code = f"""import codecs; exec(codecs.decode(b"{encoded_code}", 'base64').decode('utf-8'))""" # append decoding (and executing) to it so it can be encoded even more. Just remove the "exec()" if you dont want the code to be executed
    print("\rEncoded Layer: " + str(i+1), end="\r") # prints how often the above code has been encoded
print(code) # return the code you will be able to execute

# OUTPUT:
# import codecs; exec(codecs.decode(b"aW1wb3J0IGNvZGVjczsgZXhlYyhjb2RlY3MuZGVjb2RlKGIiYVcxd2IzSjBJRzl6T3lCd2NtbHVkQ2htSjBobGJHeHZJR1p5YjIwNklIdHZjeTVuWlhSbGJuWW9Ja05QVFZCVlZFVlNUa0ZOUlNJcGZTY3AiLCAnYmFzZTY0JykuZGVjb2RlKCd1dGYtOCcpKQ==", 'base64').decode('utf-8'))

# OUTPUT from executing above code (i just removed my PC name):
# Hello from: DESKTOP-*******
