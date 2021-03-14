from config import mongo
from bson.objectid import ObjectId

def validateUser(username):
    user = mongo.db.USERS.find_one({"username":username}, {'_id': False})
    if user:
        return user
    return None

def validatePermission(action, role):
    role = mongo.db.ROLES.find_one({"role":role})
    if role:
        for per in role['Permission']:
            obj = mongo.db.PERMISSIONS.find_one({"permission":per},{'_id':False})
            if obj:
                if action in obj['actions']:
                    return obj
            else:
                return None
    return None

