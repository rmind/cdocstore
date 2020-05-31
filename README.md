# CDocStore

## Usage

To build and run the service:
```shell
docker-compose up
open http://127.0.0.1:8000/
```
Note: production-like service runs on port `8080` (use `8000` for development).

## Development

For iterative development:
```shell
docker-compose run --service-ports dev bash -i
./run.sh  # stop and re-run when you change the code
pipenv run tests  # to run the unit tests
```
