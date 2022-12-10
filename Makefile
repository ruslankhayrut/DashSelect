build:
	dash-generate-components ./src/lib/components dash_select -p package-info.json
	npm run build:backends
	npm run build:js

run:
	python usage.py