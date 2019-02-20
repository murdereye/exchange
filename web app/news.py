from flask import Flask, request, render_template
from exc import firstfun,fun,detail
app=Flask(__name__)


@app.route("/")
def prg():
	new=firstfun()
	for x in new:
		if "USD" in x:
			new.remove(x)
			new.insert(0,x)
	new2=firstfun()
	return render_template("new2.html",new=new,new_2=new2)


@app.route("/",methods=['POST'])
def success():
	if request.method=="POST":
		money=request.form["money"]
		from_=request.form["cevr"] #çevrilecek para
		to=request.form["neye"] #neye çevrilecek
		res=fun(money,from_,to)
		new=firstfun()
		new2=firstfun()
		new.remove(from_)
		new.insert(0,from_)
		new2.remove(to)
		new2.insert(0,to)
		lists=detail(money,from_,to)
		return render_template("new2.html",new=new,new_2=new2,res=res,lists=lists)

if __name__=='__main__':
    app.debug=True
    app.run()

