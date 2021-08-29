while True:
    try:
        from requests import post,get
    except:
        import os
        os.system("pip install requests")
    else:
        break

def upload(name,paste,password=None):
    if not password:
        password = ""
    data = {"title":name,"text":paste,"password":password}
    try:
        a = post("https://ghostbin.com/paste/new",data=data)
    except:
        return "Could not make request!"
    else:
        return a.url

def raw(url):
    try:
        a = get(url)
    except:
        return "Could not make request!"
    else:
        paste = a.text.split('<textarea class="form-control" id="paste" name="paste" disabled>')[1].split('</textarea>')[0]
        return paste




if __name__ == "__main__":
    print("""You cannot use this file by just opening it!
Include these in your main.py file to use:

ghostbin.upload(name,paste,password) 
--name = The name of the paste you are uploading
--paste = The paste contents
--password (optional) = If you want to make the paste private, include a password

ghostbin.raw(url,name)
--url = The url of the paste you are trying to download""")