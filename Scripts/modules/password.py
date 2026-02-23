from zxcvbn import zxcvbn
import bcrypt
from getpass import getpass

def check_stength(password):
    results = zxcvbn(password)
    score = results["score"]
    if score == 3:
        reponse = "strong enough password scor of 3 "
    
    elif score == 4:
        reponse = "strong password of score 4"
    else:
        feedback = results.get("feedback")
        Warning = feedback.get("warning")
        suggestions = feedback.get("suggestions")
        reponse = "week password of : score of " + str(score)
        reponse += "\n warning " + Warning
        reponse += "\n Suggestions"
        for suggestion in suggestions:
            reponse += " "+ suggestion
    return reponse

def hash_pw(password):
    salt = bcrypt.gensalt()
    hashes = bcrypt.hashpw(password.encode(), salt)
    return hashes

def verify_password (pw_attemp , hashed):
    if bcrypt.checkpw(pw_attemp.encode(), hashed):
        return "password is correct "
    else : 
        return "incorrect password"
    



if __name__ =="__main__":
    while True :
        password1 = getpass("enter a password ")
        print (check_stength(password1))
        if check_stength(password1).startswith("week"):
            print("pleas chose a strong password. ")
        else :
            break

    hashed_password = hash_pw(password1)
    print("hashed password ", hashed_password)
    attempt = getpass("re enter the password to verify ")
    print (verify_password(attempt,hashed_password))

    