from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class ShortForm(Model):
    id = Column(Integer, primary_key=True)
    price = Column(Integer(80), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    last_4_of_ssn = Column(Integer(80), unique=True, nullable=False)
    birthday = Column(db.Date)
    zip = Column(Integer(10), unique=True, nullable=False)

    def __repr__(self):
        return self . username


class LongFormStep1(db.Model):
    id = db.Column(Integer, primary_key=True)
    first_name = Column(String(120), unique=True, nullable=False)
    last_name = Column(String(120), unique=True, nullable=False)
    street_adress = Column(String(120), unique=True, nullable=False)
    code_city = Column(String(2), unique=True, nullable=False)
    city = Column(String(40), unique=True, nullable=False)
    zip = Column(Integer(10), unique=True, nullable=False)
    phone = Column(Integer(20), unique=True, nullable=False)
    mobil_phone = Column(Integer(20), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    birthday = Column(Date)
    social_security = Column(Integer(80), unique=True, nullable=False)
    driver_license = Column(Integer(80), unique=True, nullable=False)
    issuing_state = Column(String(80), unique=True, nullable=False)
    home_ownership = Column(String(80), unique=True, nullable=False)
    time_at_residence = Column(String(40), unique=True, nullable=False)

    def __repr__(self):
        return self . username


class LongFormStep2(Model):
    id = Column(Integer, primary_key=True)
    military = Column(String(10), unique=True, nullable=False)
    income = Column(String(10), unique=True, nullable=False)
    company_name = Column(String(80), unique=True, nullable=False)
    position = Column(String(80), unique=True, nullable=False)
    work_phone = Column(Integer(20), unique=True, nullable=False)
    time_of_job = Column(String(10), unique=True, nullable=False)
    total_monthly_income = Column(String(80), unique=True, nullable=False)
    payment_frequency = Column(String(20), unique=True, nullable=False)
    first_payment = Column(Date)
    second_payment = Column(Date)
    deposit = Column(String(10), unique=True, nullable=False)

    def __repr__(self):
        return self . username

class LongFormStep3(Model):
    id = Column(Integer, primary_key=True)
    aba = Column(Integer(10), unique=True, nullable=False)
    bank_name = Column(String(10), unique=True, nullable=False)
    time_at_bank = Column(String(10), unique=True, nullable=False)
    checking = Column(String(10), unique=True, nullable=False)
    checking_account = Column(Integer(80), unique=True, nullable=False)

    def __repr__(self):
        return self . username
