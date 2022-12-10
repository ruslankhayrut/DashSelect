build:
	dash-generate-components ./src/lib/components dash_select -p package-info.json
	npm run build

run:
	python usage.py

publish:
	python setup.py sdist bdist_wheel
	twine upload dist/*