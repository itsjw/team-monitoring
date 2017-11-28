#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset


celery -A employee_one.taskapp worker -l INFO
