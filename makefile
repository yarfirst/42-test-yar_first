test:
	python _test42/manage.py test
	pep8 --repeat --ignore=E501 _test42/*.py
	
cleanup:
	-rm -rf build
	-rm -rf *~*
	-find . -name '*.pyc' -exec rm {} \;