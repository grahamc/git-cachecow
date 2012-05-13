#!/bin/bash

REPO=$1
TO=$2
CID=$3

WAS=`pwd`
CACHE=`echo $REPO | md5`
CDIR="$( cd -P "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
CREPO=$CDIR/cache/$CACHE.git

if [ -d "$CREPO" ]; then
    cd "$CREPO"
    git fetch
    cd $WAS
else
    git clone --mirror "$1" $CREPO
fi

git clone $REPO --reference $CREPO $TO

if [ -n "$CID" ]; then
    cd $TO
    git checkout $CID
    cd $WAS
fi
