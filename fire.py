from flask import Flask, request, send_file
import subprocess
import os
import argparse
import zipfile
from chatdev.chat_chain import ChatChain
from chatdev.utils import log_and_print_online, now


def getPath(name, start_time):
        filepath = os.path.dirname(__file__)
        root = os.path.dirname(filepath)
        directory = os.path.join(root, "WareHouse")
        
        software_path = os.path.join(directory, "_".join([name, "DefaultOrganization", start_time]))
        return software_path

def createZip(name, software_path):
     zip = ''+name +'.zip'
     with zipfile.ZipFile(zip,'w',zipfile.ZIP_DEFLATED) as z:
          z.write(software_path, os.path.basename(software_path))

     return send_file(zipfile, as_attachment=True)




app = Flask(__name__)

names = ''
desc_ = ''
time = ''

def setName(name):
    global names 
    names = name
    return names

def getName():
     return names

def setTime(start_time):
     global time
     time = start_time
     return time

def getTime():
     return time


@app.route('/start', methods = ['POST'])

def appRun():
    print("Server HIT!")
    desc = request.form.get("desc")
    name = request.form.get("name")
    setName(name)
    
    API_KEY = "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"
    # Scripts  --------------->
    process = f"python run.py --task \"{desc}\" --name \"{name}\"" #Script of actual chatdev
    online = f"python3 online_log/app.py"                          #Script of the online logger
   
    
    print(name,"  ",desc)
    
    os.environ["OPENAI_API_KEY"] = API_KEY
    try:
        # Use subprocess to run the command
        start = now()
        setTime(start)
        print("THE PATH IS")
        print(getPath(name, start))
        subprocess.run(process, shell=True, check=True)
        olog = subprocess.run(online, shell=True, check=True)
        
        
       

       
    except subprocess.CalledProcessError as e:
        a = print(f"Error running script: {e}")
        return a, 500
    except Exception as e:
        a = print(f"An error occurred: {e}")
        return a, 500

   
   
    return olog, 200

@app.route('/download_zip', methods=['GET'])
def zipDownload():
    
    name = getName()
    time = getTime()

    software_path = getPath(name, time)
    zip = createZip(name, software_path)
    return zip, 200
















      
   
        
      
   






if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)

