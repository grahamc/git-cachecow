#!/bin/bash

_DIR="$( cd -P "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $_DIR

E=0

./describe.sh; E=$(($E+$?))
./describe-empty.sh; E=$(($E+$?))

exit $((0 + $E))
