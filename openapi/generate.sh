SERVER_TYPE=$1

echo ${PWD}

if [ -d ${PWD}/out/$SERVER_TYPE ]
then
    rm -r ${PWD}/out/$SERVER_TYPE
    echo "removed jihun"
fi

mkdir -p ${PWD}/out/$SERVER_TYPE
echo "create jihun"

docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli generate \
    -i /local/main.yaml \
    -g $SERVER_TYPE \
    -o /local/out/$SERVER_TYPE

