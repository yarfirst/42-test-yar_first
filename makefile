test: cleanup
	python manage.py test
	
cleanup:
	-rm -rf build
	-rm -rf *~*
	-find . -name '*.pyc' -exec rm {} \;