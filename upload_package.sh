#!/bin/bash
set -euo pipefail

main() {
  build_distributions
  upload_distributions
}

build_distributions() {
  mkdir -p dist
  rm -f dist/*
  python setup.py sdist bdist_wheel
}

upload_distributions() {
  if [ -z ${CI+x} ]; then
    twine upload --skip-existing --verbose dist/*
  else
    twine upload --skip-existing --non-interactive --username "$PYPI_USERNAME" --password "$PYPI_PASSWORD" dist/*
  fi
}

main
