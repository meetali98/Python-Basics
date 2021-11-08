#lex_auth_01269363490743091290

def display(num):
    message=""
    if(num%3==0 and num%5==0):
        message = "Zoom"
    elif(num%3==0):
        message = "Zip"
    elif(num%5==0):
        message = "Zap"
    else:
        message = "Invalid"
    return message
message=display(9)
print(message)