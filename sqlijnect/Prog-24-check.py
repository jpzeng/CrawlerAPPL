import requests

def Url_Set():
    url_set = ["http://localhost:8080/pysqlinject/handlelogin.jsp"]
    url_set.append("http://localhost:8080/pysqlinject/securitylogin.jsp")
    return url_set

def Check(mode,url_set,header):
    res = []
    for link in url_set:
        for i in mode:
            ssion = requests.session()
            data = {"username":i[0], "password":i[1]} 
            r = ssion.post(link , headers = header, data = data)
            print(data)
            if "登陆成功" in r.text:
                print(link + ">>>" + "存在SQL漏洞！")
            elif "Exception" in r.text:
                print(r.text)
                print(link + ">>>" + "SQL语句语法错误！")
            else:
                print(link + ">>>" +"无问题.")
    return

def GetMode(file):
    res = []
    f = open(file)
    for i in f:
        i = i.strip('\n')
        i = i.split('>')
        res.append(i)
    return res
        
    
if __name__ == "__main__":
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
    mode = GetMode("1.txt")
    url_set = Url_Set()
    Check(mode,url_set,header)
