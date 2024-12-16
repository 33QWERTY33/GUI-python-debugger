import collector as collector
import manage as manage
import sys

collector.setup(r"static\code_files")

status = collector.main(sys.argv[1], r"static\code_files") # this is src and destination paths

del sys.argv[1]
# removing the source path so manage.py can handle all sys.argv elements properly

sys.argv.append("runserver")
# this start script will also run the server
# that will be useful when creating a python entry point script during pa
if status != False:
    manage.main()