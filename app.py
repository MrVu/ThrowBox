import flask
import os
import time
import configparser
import functions

app=flask.Flask(__name__)


# Load the config file
# Currently supported options:
#	pagetitle
#	username
#	paragraph

cp=configparser.ConfigParser()
cp.read("throwbox.conf")
for section in cp:
	section_obj=cp[section]
	app.config[section]=section_obj



@app.route('/favicon.ico')
def favicon():
	return flask.send_file(os.path.join(app.root_path, 'static','favicon.ico'))

@app.route("/robots.txt")
def robots():
	print(app.config["MAIN"]["allowrobots"])
	if app.config["MAIN"]["allowrobots"].lower()=="false":
		return "User-agent: *\nDisallow: /"
	else:
		flask.abort(404)

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

		# Remove the hidden files and folders (hidden=beggining with ".")
		folders=functions.RemoveHiddenObjects(folders)
		files=functions.RemoveHiddenObjects(files)

		# Sort the folders and files list.
		folders.sort()
		files.sort()

	route=path.split("/")

	return flask.render_template("browse.html",**locals())


if __name__=="__main__":

	# Run The Debugging Server.
	app.run(host="0.0.0.0", port=8080)
