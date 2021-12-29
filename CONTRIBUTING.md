## Setup

```sh
python3.6 -m virtualenv venv
source venv/bin/activate
pip install -e .[dev]
./unit_tests.sh
```

## Uploading

```sh
./upload_package.sh
```
