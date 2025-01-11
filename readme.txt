In a terminal window
====================

cd Projects/py1/winter

source .venv/bin/activate

python manage.py runserver


Also need an Email for testing (unless already put up to Gmail)
---------------------------------------------------------------
In a new Terminal Window

	cd Projects/py1/winter

	source .venv/bin/activate

	python -m smtpd -n -c DebuggingServer localhost:1025


In settings.py, make sure the EMAIL_PORT = 1025

To turn off the virtual environment
===================================

deactivate

