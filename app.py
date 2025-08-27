from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId
from flask import jsonify
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"

# ===== MongoDB Connection =====
app.config["MONGO_URI"] = "mongodb+srv://aditijagdale:AditiJagdale12@cluster1.4lmvqqz.mongodb.net/campus2career?retryWrites=true&w=majority"
mongo = PyMongo(app)

# --- Make `user` available in ALL templates (so navbar always works) ---
@app.context_processor
def inject_user():
    return {"user": session.get("user")}

# ===== Home Page =====
@app.route("/", methods=["GET"])
def home():
    query = request.args.get("q", "")
    if query:
        results = mongo.db.internships.find({
            "$or": [
                {"title": {"$regex": query, "$options": "i"}},
                {"company": {"$regex": query, "$options": "i"}}
            ]
        })
        internships = list(results)
    else:
        internships = all_internships  # Show all internships if no query

    return render_template("home.html", internships=internships, query=query)



# ===== Register =====
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = generate_password_hash(request.form["password"])

        # Check if user exists
        if mongo.db.users.find_one({"email": email}):
            flash("User already exists!", "danger")
            return redirect(url_for("register"))

        mongo.db.users.insert_one({"name": name, "email": email, "password": password})
        flash("Registration successful! Please login.", "success")
        return redirect(url_for("login"))

    return render_template("register.html")

# ===== Login =====
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = mongo.db.users.find_one({"email": email})

        if user and check_password_hash(user["password"], password):
            # Store user session
            session["user"] = {
                "_id": str(user["_id"]),
                "name": user.get("name"),
                "email": user.get("email"),
                "college": user.get("college", ""),
                "graduation_year": user.get("graduation_year", ""),
                "links": user.get("links", ""),
                "domains": user.get("domains", ""),
                "internship_type": user.get("internship_type", ""),
                "skills": user.get("skills", ""),
                "proficiency": user.get("proficiency", ""),
                "projects": user.get("projects", ""),
                "personal_statement": user.get("personal_statement", ""),
                "resume": user.get("resume", "")
            }
            flash("Login successful!", "success")
            return redirect(url_for("home"))

        flash("Invalid email or password!", "danger")

    return render_template("login.html")

# ===== Logout =====
@app.route("/logout")
def logout():
    session.pop("user", None)
    flash("Logged out successfully!", "info")
    return redirect(url_for("home"))

# ===== Profile Page =====
@app.route("/profile")
def profile():
    if not session.get("user"):
        return redirect(url_for("login"))
    return render_template("profile.html")

# ===== Update Profile =====
@app.route("/update_profile", methods=["POST"])
def update_profile():
    if not session.get("user"):
        return redirect(url_for("login"))

    user_id = session["user"]["_id"]

    # Collect form data
    update_data = {
        "name": request.form.get("full_name"),
        "college": request.form.get("college"),
        "graduation_year": request.form.get("graduation_year"),
        "links": request.form.get("links"),
        "domains": request.form.get("domains"),
        "internship_type": request.form.get("internship_type"),
        "skills": request.form.get("skills"),
        "proficiency": request.form.get("proficiency"),
        "projects": request.form.get("projects"),
        "personal_statement": request.form.get("personal_statement")
    }

    # Handle resume upload
    if "resume" in request.files and request.files["resume"].filename != "":
        file = request.files["resume"]
        resume_filename = file.filename
        os.makedirs("static/resumes", exist_ok=True)
        file_path = os.path.join("static/resumes", resume_filename)
        file.save(file_path)
        update_data["resume"] = resume_filename

    # Update MongoDB
    mongo.db.users.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": update_data}
    )

    # Refresh session with updated user
    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    user["_id"] = str(user["_id"])
    session["user"] = user

    flash("Profile updated successfully!", "success")
    return redirect(url_for("profile"))

# ===== About Us =====
@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")

# ===== Resources =====
@app.route("/resources")
def resources():
    return render_template("resources.html")

from insert import internships as all_internships


@app.route('/internships')
def internships():
    domain = request.args.get('domain')
    company = request.args.get('company')
    type_ = request.args.get('type')

    filtered = all_internships
    if domain:
        filtered = [i for i in filtered if i['domain'] == domain]
    if company:
        filtered = [i for i in filtered if i['company'] == company]
    if type_:
        filtered = [i for i in filtered if i['type'] == type_]

    return render_template("internships.html", internships=filtered)




# ===== Run App =====
if __name__ == "__main__":
    app.run(debug=True)
