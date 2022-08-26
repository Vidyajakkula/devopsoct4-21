# api to update server requests

from sre_constants import SUCCESS
from ssl import Purpose
from urllib import response
from flask import Flask, request, jsonify
from connect2db import *
import requests
from datetime import date
import time

date_today = date.today()
# print(time.asctime( time.localtime(time.time()) ))


app = Flask(__name__)


@app.route('/update_server', methods=['PUT'])
def update_server():
    conn = connectDB()
    if request.method == 'PUT':
        _json = request.json
        ID = _json["ID"]
        Creator = _json["Creator"]
        Start_Date = _json["Start_Date"]
        End_Date = _json["End_Date"]
        Manufacturer = _json["Manufacturer"]
        Number_Of_Servers = _json["Number_Of_Servers"]
        Cpu_model = _json["Cpu_model"]
        CPU_Sockets = _json["CPU_Sockets"]
        DIMM_Size = _json["DIMM_Size"]
        DIMM_Quantity = _json["DIMM_Quantity"]
        OS_Vendor = _json["OS_Vendor"]
        OS_Controller = _json["OS_Controller"]
        OS_Capacity = _json["OS_Capacity"]
        Disk_Vendor = _json["Disk_Vendor"]
        Disk_Controller = _json["Disk_Controller"]
        Disk_Capacity = _json["Disk_Capacity"]
        Network_Type = _json["Network_Type"]
        Network_speed = _json["Network_speed"]
        Network_ports = _json["Network_ports"]
        Special_Switching_Needs = _json["Special_Switching_Needs"]
        Infraadmin_Comments = _json["Infraadmin_Comments"]
        User_Comments = _json["User_Comments"]

        cursor = conn.cursor()

        data = (ID, Creator, Start_Date, End_Date, Manufacturer, Number_Of_Servers, Cpu_model, CPU_Sockets, DIMM_Size,
                DIMM_Quantity, OS_Vendor,
                OS_Controller, OS_Capacity, Disk_Vendor, Disk_Controller, Disk_Capacity, Network_Type, Network_speed,
                Network_ports, Special_Switching_Needs, Infraadmin_Comments, User_Comments)
        cursor.execute("SELECT *"
                       " FROM server_request  WHERE ID=%s", (ID,))
        print(data)

        cursor.execute(
            "UPDATE  server_request SET Creator= %s, Start_Date= (%s), End_Date= (%s), Manufacturer= %s, Number_Of_Servers = %s , Cpu_model = %s, CPU_Sockets = %s, DIMM_Size = %s, DIMM_Quantity = %s, OS_Vendor = %s, OS_Controller = %s, OS_Capacity = %s , Disk_Vendor = %s, Disk_Controller = %s, Disk_Capacity = %s, Network_Type = %s, Network_speed = %s, Network_ports = %s, Special_Switching_Needs = %s, Infraadmin_Comments = %s, User_Comments = %s  WHERE ID =%s",
            (Creator, Start_Date, End_Date, Manufacturer, Number_Of_Servers, Cpu_model, CPU_Sockets, DIMM_Size,
             DIMM_Quantity, OS_Vendor,
             OS_Controller, OS_Capacity, Disk_Vendor, Disk_Controller, Disk_Capacity, Network_Type, Network_speed,
             Network_ports, Special_Switching_Needs, Infraadmin_Comments, User_Comments, ID))

        conn.commit()
        cursor.execute('select * from server_request where ID = %s', ID)
        data = cursor.fetchall()
        resp = jsonify({'message': 'Server Request updated successfully !!', 'status': '200 OK'})
        print(resp)
        resp.status_code = 200
        v = resp.status_code
        print(v)
        assert v == 200, "code does'not match"
        return resp


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)