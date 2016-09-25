import flask
import os
import time
import functions


app=flask.Flask(__name__)

@app.route('/favicon.ico')
def favicon():
	return flask.send_file(os.path.join(app.root_path, 'static','favicon.ico'))

@app.route("/")
def index():
	return flask.render_template("index.html")

@app.route("/browse/")
def root():
	BASE_PATH=""
	folders,files=functions.ReadPath("")
	#route=["/"]
	print(files)
	return flask.render_template("root.html",**locals())

@app.route("/browse/<path:path>")
def browse(path):
	BASE_PATH=path

	# 404
	if functions.ReadPath(path)==None:
		functions.log("Error; 404; IP=%s" % flask.request.remote_addr)
		Error404=True
		ClientIP=flask.request.remote_addr
		return flask.render_template("browse.html",**locals())
	
	elif functions.IsFile(path):
		return flask.send_file(functions.RepoPath(path))
		
	else:
		folders,files=functions.ReadPath(path)

	route=path.split("/")

	return flask.render_template("browse.html",**locals())


if __name__=="__main__":

	# Check if ThrowBox is installed.
	if not functions.Installed():
		print("It seems like the throwbox isn't")
		print("installed correctly.")
		choice=input("Do you want to install now? (Y/N):")

		if choice.lower()=="y":
			functions.Install()
			print("Installed.")
		else:
			print("OK, exiting.")
			exit()

	# Run The Debugging Server.
	app.run(host="0.0.0.0", port=8080)
