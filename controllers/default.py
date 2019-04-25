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


def store():
    submitted_surname = request.vars.surname
    submitted_othername = request.vars.othername
    submitted_dateofbirth = request.vars.dateofbirth
    submitted_gender = request.vars.gender
    submitted_department = request.vars.department 
    submitted_qualification = request.vars.qualification
    submitted_email = request.vars.email
    submitted_number =request.vars.number
    submitted_staffid = request.vars.staffid
    submitted_rank = request.vars.rank

    results = db.users.insert(
        db_surname =submitted_surname,
        db_othername =submitted_othername,
        db_dateofbirth =submitted_dateofbirth,
        db_gender =submitted_gender,
        db_department =submitted_department,
        db_qualification =submitted_qualification,
        db_email =submitted_email,
        db_number =submitted_number,
        db_staffid =submitted_staffid,
        db_rank =submitted_rank
    )

    if results:
        return "User Saved Successfully"
    else:
        return "An Error Occured"

def details():
   users = db().select(db.users.ALL)
   return dict(users=users)
   

def authenticate():
    submitted_email = request.vars.email
    submitted_password = request.vars.password

    if db(db.user.db_email==submitted_email
            and db.users.db_password==submitted_password).count()>0:
        return "User Logged in Successfully"
    else: 
        return "User Not found. Please Sign Up"