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

HOW TO RUN:
	SETUP:
		1. Run main.py
		2. Go to http://127.0.0.1:5000/ in any browser
			-- This will automatically create a database to begin testing
			-- The FIRST account created will be designated as the admin of the database, and will act differently from other accounts
			-- If you wish to 'reset' the demo at any time, simply delete the instance database and re-run main.py to set everything back to its default states.