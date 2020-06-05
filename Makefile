.PHONY: test dist
build: setup.py
	rm -rf dist
	python3 setup.py bdist_wheel
test: build
	twine upload -u thinkdatasci --repository-url https://test.pypi.org/legacy/ dist/*
dist: build
	twine upload -u thinkdatasci dist/*
