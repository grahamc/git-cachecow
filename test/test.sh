#!/bin/bash

E=0

./describe.sh; E=$(($E+$?))
./describe-empty.sh; E=$(($E+$?))

exit $((0 + $E))
