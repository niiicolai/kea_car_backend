# create a variable for the source set to the app directory as default
export SOURCE=${1:-app}

# check if a parameter was passed
if [ $# -eq 0 ]; then
  echo "No parameter was passed, using the default source directory $SOURCE"
fi

# otherwise, use the parameter as the source directory
if [ $# -eq 1 ]; then
  SOURCE=$1
fi

# check if the source directory exists
if [ ! -d $SOURCE ]; then
  echo "The source directory $SOURCE does not exist"
  exit 1
fi

coverage run --source=$SOURCE -m pytest
coverage report -m
coverage html
