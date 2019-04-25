from gluon.contrib.appconfig import AppConfig
configuration = AppConfig(reload=True)

db = DAL("sqlite://storage.sqlite")
db.define_table("users",
            Field('db_name'),
            Field('db_email'),
            Field('db_password'),
            Field('db_surname'),
            Field('db_othername'),
            Field('db_dateofbirth').
            Field('db_gender'),
            Field('db_department'),
            Field('db_qualification'),
            Field('db_rank')
            )