import urllib3

http = urllib3.PoolManager()
r = http.request('GET', 'https://raw.githubusercontent.com/j-delaney/easy-application/master/README.md')
s = r.data.decode("utf-8").split("\n")
for i in s:
    if i.find("NY") >= 0:
        q = i.split("(")
        w = q[1].split(")")
        e = q[0] + "	" + w[0] + "	" + w[1]
        print(e)
