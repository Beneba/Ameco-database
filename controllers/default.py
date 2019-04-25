def signup():
    return dict()

def store():
    submitted_name = request.vars.name
    submitted_email = request.vars.email
    submitted_password =request.vars.password

    results = db.users.insert(
        db_name =submitted_name,
        db_email =submitted_email,
        db_password = submitted_password
    )

    if results:
        return "User Saved Successfully"
    else:
        return "An Error Occured"


def lecturers():
    return dict()

def tutors():
    return dict()
# def store():
#     submitted_name = request.vars.name
#     submitted_email = request.vars.email
#     submitted_password =request.vars.password

#     results = db.users.insert(
#         db_name =submitted_name,
#         db_email =submitted_email,
#         db_password = submitted_password
#     )

#     if results:
#         return "User Saved Successfully"
#     else:
#         return "An Error Occured"

def authenticate():
    submitted_email = request.vars.email
    submitted_password = request.vars.password

    if db(db.user.db_email==submitted_email
            and db.users.db_password==submitted_password).count()>0:
        return "User Logged in Successfully"
    else: 
        return "User Not found. Please Sign Up"