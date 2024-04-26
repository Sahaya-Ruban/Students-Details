from flask import Flask, session, render_template, request, redirect, url_for,flash

app=Flask(__name__)

user_name="Ruban"
password="ruban@123"
app.secret_key="Ruban@123"

Student_list = [{"Name":"Deva","Age":21 ,"Roll_NO": 101, "Marks":[90,75,80,98,75]},
                {"Name":"Eswar","Age":24 ,"Roll_NO": 102, "Marks":[90,75,80,98,65]},
                {"Name":"Siva","Age":23 ,"Roll_NO": 103, "Marks":[90,75,80,78,99]},
                {"Name":"Ruban","Age":24 ,"Roll_NO": 104, "Marks":[94,75,80,88,35]},
                {"Name":"Kiruba","Age":22 ,"Roll_NO": 105, "Marks":[70,85,80,98,35]},          
                {"Name":"Halith","Age":25 ,"Roll_NO": 106, "Marks":[90,75,85,98,35]},
                {"Name":"Thenmozhi","Age":23 ,"Roll_NO": 107, "Marks":[80,98,35,90,75]}
                ]

def isloggedin():
    return user_name in session

@app.route("/",methods=["GET","POST"])

def login():
    if request.method == "POST":
        Name=request.form.get("name")
        Password=request.form.get("Password")
        
        if user_name == Name and password == Password:
            session["user_name"] = Name
            return redirect(url_for("home"))
        else:
            return "Invalid"
    return render_template("user.html")

@app.route("/logout")

def logout():
    session.pop("user_name",None)
    return redirect(url_for("login"))

@app.route("/home")
def home():
    return render_template("index.html",data=Student_list)

@app.route("/add",methods=["GET","POST"])
def student():
    if request.method=="POST":
        Name=request.form.get("Name")
        Age=request.form.get("Age")
        RollNo=request.form.get("Roll_NO")
        Tamil=request.form.get("Tamil")
        English=request.form.get("English")
        Maths=request.form.get("Maths")
        Science=request.form.get("Science")
        Social=request.form.get("Social")
        Mark_list=[Tamil,English,Maths,Science,Social]
        Student_dict={}
        Student_dict.update({"Name":Name})
        Student_dict.update({"Age":Age})
        Student_dict.update({"Roll_NO":RollNo})
        Student_dict.update({"Marks":Mark_list})
        
        Student_list.append(Student_dict)
        flash("User added","Success")
        return redirect(url_for("home"))
       
    return render_template("add.html",data=Student_list)

@app.route("/edit/<string:name>",methods=["GET","POST"])
def edit(name):
    if request.method=="POST":
        Name=request.form.get("Name")
        Age=request.form.get("Age")
        RollNo=request.form.get("Roll_NO")
        Tamil=request.form.get("Tamil")
        English=request.form.get("English")
        Maths=request.form.get("Maths")
        Science=request.form.get("Science")
        Social=request.form.get("Social")
        Mark_list1=[Tamil,English,Maths,Science,Social]
        edit_dict=Student_list[int(name)-1]
        edit_dict["Name"]=Name
        edit_dict["Age"]=Age
        edit_dict["Roll_NO"]=RollNo
        edit_dict["Marks"]=Mark_list1
        return redirect(url_for("home"))
    flash("Student Edited","Success")
    edit_list=Student_list[int(name)-1]
    return render_template("edit.html",form_edit=edit_list)

@app.route("/delete/<string:name>",methods=["GET","POST"])
def delete_method(name):
    Student_list.pop(int(name)-1)
    return redirect(url_for("home"))
if __name__=="__main__":
    app.run(debug=True)