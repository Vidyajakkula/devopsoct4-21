from flask_cors import CORS,cross_origin
import psycopg2
# from addserverFORM import app
from flask import Flask, request, jsonify, make_response
import requests                                   #importing the packages/modules
import psycopg2
# import INSERT                                    #inserting the database file
# import threading
# from connect2DB import *

app = Flask(__name__)
CORS(app)

@app.route('/add_server', methods=['POST'])
def add_asset():
    # conn = connectDB()              #called the connectDB file to connect with the database
    # connecting with the database
    dbase = psycopg2.connect(         #the database is assigned by dbase
        host='localhost',
        dbname='sample',
        user='postgres',
        password='Vidya_98',
        port=5432)
    # conn.autocommit = True         #if you commit a database, it saves all the changes till that particular point

    #    _json = request.json  # converting to json


    cursor = dbase.cursor()
    conn=cursor.connection



    if request.method == 'POST':  # using POST method to request the data
        _json = request.json
        print("sonali")
        print("_json")
        Asset_ID = _json["Asset_ID"]     #list of column data from server_table
        # id = _json["id"]
        Manufacturer = _json["Manufacturer"]
        BMC_ip = _json["BMC_ip"]
        BMC_User= _json["BMC_User"]
        BMC_password = _json["BMC_password"]
        Asset_location = _json["Asset_location"]
        Reserved = _json["Reserved"]
        #assigned_on = _json["assigned_on"]
        Assigned_to = _json["Assigned_to"]
        Assigned_from=_json["Assigned_from"]
        Assigned_by = _json["Assigned_by"]
        Created_on=_json["Created_on"]
        Created_by = _json["Created_by"]
        OS_IP=_json["OS_IP"]
        OS_User=_json["OS_User"]
        OS_Password=_json["OS_Password"]
        Updated_on=_json["Updated_on"]
        Updated_by= _json["Updated_by"]
        Purpose = _json["Purpose"]
        Cluster_Id = _json["Cluster_Id"]
        # team_id = _json["team_id"]
        Delete = "0"
        Status = _json["Status"]
        print("server_id")
        # cursor = conn.cursor()  # created a cursor
        print("zdfrhv")
        query1 ="SELECT Asset_ID FROM Asset"
        print(query1,"q1111")
        cursor.execute(query1)
        fetch = cursor.fetchall()
        print(fetch,"fe1111")
        lst = []
        for i in fetch:
            for j in i:
                lst.append(j)
            print(lst,"lsttt")
        if Asset_ID in lst:
            return "already exist"
            print("already exist")

        else:

                # values to assign in the columns
            VALUES = (Asset_ID,Manufacturer,BMC_ip,BMC_User,BMC_password,
                      Asset_location,Reserved,Assigned_to,Assigned_from,Assigned_by,
                      Created_on,Created_by,OS_IP,OS_User,OS_Password,Updated_on,Updated_by,
                      Purpose,Cluster_Id,Delete,Status)
            print("iohvd")
            cursor.execute(
                'INSERT INTO Asset(Asset_ID,Manufacturer,BMC_ip,BMC_User,'
                'BMC_password,Asset_location,Reserved,Assigned_to,Assigned_from,'
                'Assigned_by,Created_on,Created_by,OS_IP,OS_User,OS_Password,Updated_on,'
                'Updated_by,Purpose,Cluster_Id,Delete,Status)'
                'values (%s, %s ,%s ,%s ,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',VALUES )
                # execute the values using cursor in the server_table to store all the new data
            print("awxfyn")


    #CREATE TABLE Asset(Asset_ID  SERIAL NOT NULL PRIMARY KEY,Manufacturer varchar NOT NULL, BMC_ip varchar NOT NULL, BMC_User varchar NOT NULL,
            # BMC_password varchar NOT NULL, Asset_location varchar NOT NULL,Reserved BOOL, Assigned_to int null ,Assigned_from DATE  null,Assigned_by varchar(50)  null,
            # Created_on DATE  NULL,Created_by VARCHAR(50)  NULL,Updated_on DATE  NULL,Updated_by varchar(80)  NULL,Purpose varchar(300) NOT NULL,Cluster_Id  Varchar Not NULL, Delete BIT NOT NULL,Status BOOL NOT NULL );


                # cursor.commit()
            conn.commit()
            print("_id")
            # conn.commit()  # commit
            print("oook")
            cursor.execute('select * from asset') # to show the data in the asset_table
            print("fjrdgchk")
            data = cursor.fetchall()              #it will fetch all the data with variable data

            print("_id")

            # serverList = []          #using the for loop to execute all data oneby one and then stored in the serverlist
            # for serverData in data:
            #     data = {"Asset_ID": serverData[0], "Manufacturer": serverData[1],"BMC_ip": serverData[2], "BMC_User": serverData[3],
            #             "BMC_password": serverData[4], "Asset_location": serverData[5],
            #             "Reserved": serverData[6],"Assigned_to":serverData[9],"Assigned_from":serverData[8],"Assigned_by":serverData[7],
            #             "Created_on":serverData[10],"Created_by":serverData[11],"Updated_on":serverData[12],"Updated_by":serverData[13],"Purpose":serverData[14],"Cluster_Id":serverData[15] ,
            #             "Delete":serverData[16],"Status":serverData[17]}


                # serverList.append(data)
            # return jsonify(serverList)            #it will show list of server with this newly added
            resp = jsonify('server added successfully!')  # created a response and jsonifed it
            resp.status_code = 200  # given a status code 200(truse) to the above response
            return resp  # returning the response if the above condition works



if __name__== '__main__':
    # app.app_context()
    app.run(debug=True)