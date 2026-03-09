import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/fatima/MR_Lab_Fatima/install/my_first_pkg'
