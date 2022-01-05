import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

products_db = myclient["products"]
order_management_db = myclient["order_management"]


def get_product(code):
    products_coll = products_db["products"]

    product = products_coll.find_one({"code":code},{"_id":0})

    return product

def get_products():
    product_list = []

    products_coll = products_db["products"]

    for p in products_coll.find({},{"_id":0}):
        product_list.append(p)

    return product_list


def get_branch(code):
    products_coll = products_db["branches"]

    branch = products_coll.find_one({"code":code})

    return branch

def get_branches():
    branch_list = []

    products_coll = products_db["branches"]

    for p in products_coll.find({}):
        branch_list.append(p)

    return branch_list

def get_user(username):
    customers_coll = order_management_db['customers']
    user=customers_coll.find_one({"username":username})
    return user

def create_order(order):
    orders_coll = order_management_db['orders']
    orders_coll.insert(order)

def get_orders(code):
    orders_coll = order_management_db['orders']

    past_order = orders_coll.find_one({"code":code},{"_id":0})

    return past_order

def get_orders():
    order_list = []

    orders_coll = order_management_db["orders"]

    for p in orders_coll.find({},{"_id":0}):
        order_list.append(p)

    return order_list

def change_password():
    if password1 == password2:
        db.customers.updateOne({"username":user}, {"$set":{"password":password1}})
    else:
        return "Error: The passwords do not match"
    
