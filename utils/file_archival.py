# Move processed files to archive with timestamp

import shutil
import time

timestamp = int(time.time())
archive_path = f"/archive/archive_{timestamp}/"

shutil.move("/input/", archive_path)
