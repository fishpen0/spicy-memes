#!/usr/bin/env bash
source ./.env

if [ command -v emojipacks ]; then
    for f in "packs"/*.yaml
    do
      echo ${f}
      emojipacks -s ${SUBDOMAIN} -e ${EMAIL} -p ${PASSWORD} -y ${f};
    done
else
    echo "Install emojipacks! https://github.com/lambtron/emojipacks"
fi
