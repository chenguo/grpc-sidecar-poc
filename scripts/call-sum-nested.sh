#! /bin/bash

X=${1:-10}
Y=${2:-20}

curl "localhost:9125/sum-nested?x=$X&y=$Y"
