import functions

# Check if ThrowBox is installed.
if not functions.Installed():
	print("It seems like the throwbox isn't")
	print("installed (correctly).")
	choice=input("Do you want to install now? (Y/N):")

	if choice.lower()=="y":
		functions.Install()
		print("Installed.")
	else:
		print("OK, exiting.")
		exit()

else:
	print("Throwbox installed.")