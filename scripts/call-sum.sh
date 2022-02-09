#! /bin/bash

X=${1:-10}
Y=${2:-20}

curl "localhost:9125/sum?x=$X&y=$Y"
