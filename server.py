from flask import Flask  

app = Flask(__name__) #instance of Flask

# http://127.0.0.1:5000/
@app.route("/",methods=["GET"])
def index():
  return "welcome to Framework"

# http://127.0.0.1:5000/hello
@app.route("/hello", methods=['GET'])
def hello():
  return "Hello World from flask"


# http://127.0.0.1:5000/cohort-63  
@app.route("/cohort-63", methods=["GET"])
def cohort63():
     student_list = ["robert", "luis", "barney", "lemuel", "john", "reece", "angel"]
     return student_list


# http://127.0.0.1:5000/cohort-99  
@app.route("/cohort-99", methods=["GET"])
def cohort99():
     student_list = ["pam", "michael", "angela", "dwight"]
     return student_list


@app.route("/contact", methods=["GET"])
def contact():
  info = {
    "email": "bigdog@gmail.com",
    "phone": "561-682-5690"
  }
  return info


@app.route("/course-info", methods=["GET"])
def course_info():
  course_data = {
    "Title": " Python with Flask",
    "Duration": "4 Sessions",
    "Level": "Beginner"
  }
  return course_data



#------Copouns----------
#------Aissignment 1---------
coupons_list= [
    {"_id": 1, "code": "WELCOME10", "discount": 10},
    {"_id": 2, "code": "SPOOKY25", "discount": 25},
    {"_id": 3, "code": "VIP50", "discount": 50}
  ]

@app.route("/coupons", methods=["GET"])
def coupons():
     return coupons_list

@app.route("/coupons/count", methods=["GET"]) 
def coupons_count():
    count = len(coupons_list) 
    return {"count":count}   



  





if __name__ == "__main__":
  app.run(debug=True)
# When this file is run directly: __name__== "__main__"
# When this file is imported as a module: _name_== "server.py"
    