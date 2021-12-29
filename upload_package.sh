#!/bin/bash
set -e

main() {
  activate_virtualenv
  run_tests
  build_distributions
  upload_distributions
}

activate_virtualenv() {
  if [ -d venv ]; then
    rm -r ./venv
  fi
  python3.8 -m virtualenv venv
  source venv/bin/activate
  install_dependencies
}

install_dependencies() {
  pip install -e .[dev]
  pip check
}

run_tests() {
  bash unit_tests.sh
}

build_distributions() {
  mkdir -p dist
  rm dist/*
  python setup.py sdist bdist_wheel
}

upload_distributions() {
  twine upload dist/* --skip-existing
}

main
