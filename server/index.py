from flask import Flask, request,  make_response
import json
import base64
import datetime

app = Flask(__name__)
@app.route('/passcheck', methods = ['GET'])
def index():
	def base64func(par):
	    b = par.encode("UTF-8")
	    d = base64.b64decode(b).decode("UTF-8")
	    return d
	boolean = ""
	login = request.args.get("login")
	password = request.args.get("password")
	with open("ftSDYWDA78FYWQESWD.txt", "r", encoding="utf-8") as f:
		jb = json.loads(f.read())
		f.close()
		try:
			a = jb[base64func(login)]
			if a["password"] == base64func(password):
				boolean = "True"
			else:
				boolean = "False"
		except:
			boolean = "False"
	res = make_response(boolean)
	res.headers['Content-Type'] = 'text/plain'
	res.headers['Access-Control-Allow-Origin'] = '*'
	res.headers['Access-Control-Allow-Credentials'] = 'true'
	return res
@app.route('/activeusers', methods = ['GET'])
def index1():
	a = {}
	with open("ftSDYWDA78FYWQESWD.txt", "r", encoding="utf-8") as f:
		jb = json.loads(f.read())
		for k, v in jb.items():
			a[k] = "active"
	res = make_response(json.dumps(a))
	res.headers['Content-Type'] = 'text/plain'
	res.headers['Access-Control-Allow-Origin'] = '*'
	res.headers['Access-Control-Allow-Credentials'] = 'true'
	return res
@app.route('/registration', methods = ['GET'])
def index2():
	def base64func(par):
	    b = par.encode("UTF-8")
	    d = base64.b64decode(b).decode("UTF-8")
	    return d
	boolean = ""
	login = request.args.get("login")
	password = request.args.get("password")
	password1 = request.args.get("passwordre")
	if password != password1:
		boolean = "False"
	else:
		with open("ftSDYWDA78FYWQESWD.txt", "r", encoding="utf-8") as f:
			jb = json.loads(f.read())
			for k, v in jb.items():
				if k == base64func(login):
					boolean = "False"
					break
				else:
					boolean = "True"
			l = {}
			l["password"] = base64func(password)
			l["host"] = "none"
			jb[base64func(login)] = l
			f.close()
		with open("ftSDYWDA78FYWQESWD.txt", "w+", encoding="utf-8") as f:
			f.seek(0)
			f.close()
		with open("ftSDYWDA78FYWQESWD.txt", "w", encoding="utf-8") as f:
			f.write(json.dumps(jb))
			f.close()
	res = make_response(boolean)
	res.headers['Content-Type'] = 'text/plain'
	res.headers['Access-Control-Allow-Origin'] = '*'
	res.headers['Access-Control-Allow-Credentials'] = 'true'
	return res
@app.route('/checkchat', methods = ['GET'])
def index3():
	def base64func(par):
	    b = par.encode("UTF-8")
	    d = base64.b64decode(b).decode("UTF-8")
	    return d
	boolean = ""
	login = request.args.get("login")
	password = request.args.get("password")
	chatname = request.args.get("chatname")
	with open("ftSDYWDA78FYWQESWD.txt", "r", encoding="utf-8") as f:
		jb = json.loads(f.read())
		try:
			d = jb[base64func(login)]["password"]
			if d == base64func(password):
				o = open("hguidhguidhugihsduighdsuhg.txt", "r", encoding="utf-8")
				jb1 = json.loads(o.read())
				o.close()
				jb2 = {}
				jb2[chatname] = jb1[chatname]
				boolean = json.dumps(jb2)
				del jb2[chatname]
			else:
				boolean = "False"
		except:
			boolean = "False"
		f.close()
	res = make_response(boolean)
	res.headers['Content-Type'] = 'text/plain'
	res.headers['Access-Control-Allow-Origin'] = '*'
	res.headers['Access-Control-Allow-Credentials'] = 'true'
	return res
@app.route('/chatplus', methods = ['GET'])
def index4():
	def base64func(par):
	    b = par.encode("UTF-8")
	    d = base64.b64decode(b).decode("UTF-8")
	    return d
	def base64func2(par):
		b = s.encode("UTF-8")
		e = base64.b64encode(b)
		s1 = e.decode("UTF-8")
		return s1
	boolean = ""
	login = request.args.get("login")
	password = request.args.get("password")
	chatname = request.args.get("chatname")
	message = request.args.get("message")
	with open("ftSDYWDA78FYWQESWD.txt", "r", encoding="utf-8") as f:
		jb = json.loads(f.read())
		try:
			d = jb[base64func(login)]["password"]
			print(d)
			if d == base64func(password):
				o = open("hguidhguidhugihsduighdsuhg.txt", "r", encoding="utf-8")
				jb1 = json.loads(o.read())
				o.close()
				now = datetime.datetime.now()
				resi = str(now)+" "+base64func(login)
				jb1[chatname][resi] = message
				o = open("hguidhguidhugihsduighdsuhg.txt", "w+", encoding="utf-8")
				o.seek(0)
				o.close()
				o = open("hguidhguidhugihsduighdsuhg.txt", "w", encoding="utf-8")
				o.write(json.dumps(jb1))
				o.close()
				boolean = "True"
			else:
				boolean = "False"
		except:
			boolean = "False"
		f.close()
	res = make_response(boolean)
	res.headers['Content-Type'] = 'text/plain'
	res.headers['Access-Control-Allow-Origin'] = '*'
	res.headers['Access-Control-Allow-Credentials'] = 'true'
	return res
@app.route('/checkchattwo', methods = ['GET'])
def index5():
	def base64func(par):
	    b = par.encode("UTF-8")
	    d = base64.b64decode(b).decode("UTF-8")
	    return d
	boolean = ""
	login = request.args.get("login")
	password = request.args.get("password")
	chatname = request.args.get("chatname")
	with open("ftSDYWDA78FYWQESWD.txt", "r", encoding="utf-8") as f:
		jb = json.loads(f.read())
		try:
		    print(jb)
		    d = jb[base64func(login)]["password"]
		    print(d)
		    if d == base64func(password):
		    	print("ok")
		    	o = open("hguidhguidhugihsduighdsuhg.txt", "r", encoding="utf-8")
		    	jb1 = json.loads(o.read())
		    	o.close()
		    	jb2 = {}
		    	jb2[chatname] = jb1[chatname]
		    	k1 = len(jb2[chatname])
		    	for k in jb2[chatname]:
		    		k1 -= 1
		    		if k1 == 0:
		    			boolean = str(k)+"<br>"+str(base64func(jb2[chatname][k]))
		    	#del jb2[chatname]
		    else:
		    	boolean = "False"
		except:
			boolean = "False"
		f.close()
	print(boolean)
	res = make_response(boolean)
	res.headers['Content-Type'] = 'text/plain'
	res.headers['Access-Control-Allow-Origin'] = '*'
	res.headers['Access-Control-Allow-Credentials'] = 'true'
	return res
if __name__ == "__main__":
    app.run()