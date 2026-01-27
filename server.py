from flask import Flask, jsonify, request

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


# Path Parameters
#Is  a dynamic part of URL used to identity a specific item or resource with an API

#GET http://127.0.0.1:5000/greet/name
@app.route("/greet/<string:name>", methods=["GET"])
def greet(name):
  print(f"this is the name {name}")
  return jsonify({"message": f"Hello {name}"}), 200 # OK 


products =[
  {"_id": 1, 
  "title": "Nintendo Switch",
  "price":499.99,
  "cataegory":"electronics",
  "image":"https://picsum.photos/seed/1/300/300"
  },
   {"_id": 2, 
  "title": "Smart refrigerator",
  "price":999.99,
  "cataegory":"kitchen",
  "image":"https://picsum.photos/seed/2/300/300"
  },
 {"_id": 3, 
  "title": "Bluetooth Speaker",
  "price":89.99,
  "cataegory":"electronics",
  "image":"https://picsum.photos/seed/3/300/300"
  }

]
#GET http://127.0.0.1:5000/products
@app.route("/products" , methods=["GET"])
def product_list():
    return jsonify({
      "success": True,
      "message": "Products retrieved successfullly",
      "products": products
    }) , 200 #Ok

#GET http://127.0.0.1:5000/products/_id
@app.route("/product/<int:_id>", methods=["GET"])
def get_product_id(_id):
    for product in products:
        if product ["_id"]== _id:
           return jsonify({
            "success": True,
            "message": "Product retrieved successfully",
            "data": product
           }), 200 #OK
    return jsonify({
      "success": False,
      "message":"Product not found"
    }), 404 

#POST http://127.0.0.1:5000/api/products
@app.route("/api/products", methods=["POST"])
def create_product():
    new_product = request.get_json()
    print(new_product)
    products.append(new_product)
    return jsonify({
      "success": True,
      "message": "Product successfully created",
      "data": new_product
    }),201 #created 



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


#------Copouns----------
#------Aissignment 3---------

coupons_list=[
    {"_id": 1, "code": "WELCOME10", "discount": 10},
    {"_id": 2, "code": "SPOOKY25", "discount": 25},
    {"_id": 3, "code": "VIP50", "discount": 50}
]


# POST
@app.route("/api/coupons", methods=["POST"])
def create_coupon():
    new_coupon = request.get_json()
    print(new_coupon)
    coupons_list.append(new_coupon)
    return jsonify({
      "success": True,
      "message": "Coupon successfully added!",
       "data":new_coupon
    }),201



#GET
@app.route("/api/coupons/<int:_id>", methods=["GET"])
def coupon_id(_id):
    for coupon in coupons_list:
      if coupon ["_id"]== _id:
         return jsonify({
          "success": True,
          "message": "Successfully!",
          "data": coupon
         }),200
    return jsonify({
      "success": False,
      "message":"Coupon not found"
    }), 404 




if __name__ == "__main__":
  app.run(debug=True)
# When this file is run directly: __name__== "__main__"
# When this file is imported as a module: _name_== "server.py"
    