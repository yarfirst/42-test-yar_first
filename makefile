test: cleanup
	python manage.py test main
	
cleanup:
	-rm -rf build
	-rm -rf *~*
	-find . -name '*.pyc' -exec rm {} \;
	
syncdb:
	python manage.py syncdb --noinput

migrate:
	python manage.py migrate

run:
	python manage.py runserver 0.0.0.0:8000
	
shell:
	python manage.py shell