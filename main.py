from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5
import smtplib


SKILLS = {
    "SKILL 1": 100,
    "SKILL 2": 70,
    "SKILL 3": 80,
    "SKILL 4": 75,
    "SKILL 5": 85,
}
EXPERIENCE = {
    "2018 - Present": ["JOB 1", "COMPANY NAME 1", "CITY, COUNTRY 1", "WHAT YOU DO 1"],
    "2016 - 2018": ["JOB 0", "COMPANY NAME 0", "CITY, COUNTRY 0", "WHAT YOU DO 0"],
}
EDUCATION = {
    "2018 - 2020": ["WHAT DID YOU LEARN 1", "WHERE 1", "CITY, COUNTRY 1", "WHAT YOU LEARNED 1"],
    "2016 - 2018": ["WHAT DID YOU LEARN 0", "WHERE 0", "CITY, COUNTRY 0", "WHAT YOU LEARNED 0"],
}
MAIL_ADDRESS = os.environ.get("EMAIL_KEY")
MAIL_APP_PW = os.environ.get("PASSWORD_KEY")

app = Flask(__name__)
Bootstrap5(app)

@app.route('/')
def home():
    return render_template("index.html",
                           SKILLS=SKILLS,
                           EXPERIENCE=EXPERIENCE,
                           EDUCATION=EDUCATION)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    my_email = "your email"
    password = "password"
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('comment')

        # Sending email
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="to address",
                msg=f"Subject: Contact from User\n\n"
                    f"Name: {name}\n"
                    f"Email: {email}\n"
                    f"Subject: {subject}\n"
                    f"Message: {message}"
            )
        return render_template("index.html",
                               SKILLS=SKILLS,
                               EXPERIENCE=EXPERIENCE,
                               EDUCATION=EDUCATION)

    return render_template("index.html",
                           SKILLS=SKILLS,
                           EXPERIENCE=EXPERIENCE,
                           EDUCATION=EDUCATION)


if __name__ == "__main__":
    app.run(debug=True, port=5007)