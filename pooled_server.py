import sys
import os
from cross_origin  # The typical way to import flask-cors
import requests  # importing the packages/modules
from flask_cors import CORS, cross_origin
import psycopg2
from connect2db import connectD
app = Flask(_name_)
def convert_json(l_o_t, key):
    b = []
    # iterating  the list of tuples to get individual tuples.
    for item in l_o_t:
        a = {}
        # taking range from 0 to number of items in tuples - 1
        for i in range(len(item)):
            a[key[i]] = item[
                i]  # appending value to dictionary by mapping key from array to value in tuples using indexing.
        b.append(a)  # appending all dictionaries to a list.
    return b


# base.autocommit= True
@app.route('/list_asset/Pooled', methods=['GET'])
def list_all_pool():
    conn = connectDB()  # called the connectDB file to connect with the database
    # connecting with the database
    base = psycopg2.connect(  # the database is assigned by dbase
        host='localhost',
        dbname='sample',
        user='postgres',
        password='Vidya_98',
        port=5432)

    try:
        cursor = base.cursor()
        # To show reserved servers,fetch all the data base from the asset table where reserved=true.
        cursor.execute(
            "select asset_id,manufacturer,bmc_ip,bmc_user,asset_location,reserved,assigned_to,assigned_from,assigned_by,created_on,created_by,updated_on,updated_by,os_ip,os_user,purpose,cluster_id,delete,status from asset where reserved=false or reserved=null")
        res = cursor.fetchall()
        print(res)
        # arr = [desc[0].capitalize() for desc in cursor.description]  # getting column name from database
        arr = ["Asset_ID", "Manufacturer", "BMC_IP", "BMC_USER", "Asset_location", "Reserved", "Assigned_to",
               "Assigned_from", "Assigned_by", "Created_on", "Created_by", "Updated_on", "Updated_by", "OS_IP",
               "OS_User", "Purpose", "Cluster_Id", "Delete", "Status"]
        json_data = convert_json(res, arr)
        data = []
        for i in json_data:

            cursor.execute("select email_id from users where user_id=%s", [i['Assigned_to']])
            res = cursor.fetchall()
            print(res)
            for j in res:
                i.update({"Assigned_to": j[0].split("@")[0]})
            data.append(i)
        print(data)
        # if json.args()
        return jsonify({"ListAsset": data, "message": "listing all assets!", "status code": "200 ok"})
    except Exception as e:
        print(e)
        return jsonify({"message": "exception occurred!", "status code": "400 bad request"})


if __name__ == '__main__':
    app.run(debug=True, port=4000)
