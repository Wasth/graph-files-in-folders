import os
import re
import pandas

abs_path = 'C:\\path\\to\\root'
dir_pattern = r'^folder_[0-9]{1,}$'

raw_data = {
    'tz_name': [],
    'files_amount': []
}

for root, dirs, files in os.walk(abs_path):
    basename = os.path.basename(root)
    if re.match(dir_pattern, basename):
        raw_data['tz_name'].append(basename)
        raw_data['files_amount'].append(len(files))

df = pandas.DataFrame(raw_data)

df.to_csv('data.csv')
