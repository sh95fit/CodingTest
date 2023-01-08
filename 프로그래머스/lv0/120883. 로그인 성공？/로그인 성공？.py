def solution(id_pw, db):
    dic_db = {i[0]:i[1] for i in db}
    if id_pw[0] in dic_db :
        if dic_db[id_pw[0]] == id_pw[1] :
            return "login"
        else :
            return "wrong pw"
    else :
        return "fail"