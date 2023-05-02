The bulk of the code for this version of the product was written in Viscual Studio Code, but any editor should work fine.
Python 3.11.3 (64-bit) was used, use older versions at your own risk

A working internet connection is required to make this demo work correctly. Without it, the Bootstrap-derived parts may not work.

	Dependencies:
		Python
		Flask
		Flask-Login
		Flask-SQLAlchemy

	Other Software used, but not required:
		Prettier for VS Code (for HTML formatting)
		autopep8 for VS Code (for Python formatting)

How to run:
	1. Run main.py. This will automatically create a database that the program will pull from, as well as launch a local server to run the html on.
	2. Go to http://127.0.0.1:5000/ and interact with the demo.

Do note, the first account created will be the Admin account for the demo. Later accounts will be normal users.

Demo Video Link: https://iu.mediaspace.kaltura.com/media/t/1_g84e6o8y

MAJOR CHANGES:
	User Authentication, complete with actual hashed passwords!
	Front and back ends that actually communicate with each other!
	The interface doesn't completely awful (thanks Bootstrap)!
	Users can actually do stuff with the program!