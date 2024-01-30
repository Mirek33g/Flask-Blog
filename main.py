from flask import Flask, render_template, request
import requests
import smtplib


posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

# MY_EMAIL = "my_email@gmail.com"
# PASSWORD = "my_password"
#
# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
# connection.login(MY_EMAIL, PASSWORD)


app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        msg = request.form["message"]
        print(name, email, phone, msg)
        #connection.sendmail(from_addr=MY_EMAIL, to_addrs="my_email@gmail.com", msg=f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {msg}")
        return render_template("contact.html", message="Successfully sent your message.")
    else:
        return render_template("contact.html", message="Contact me")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
