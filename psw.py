def psw_list(psw_file):
    
    psw_resource = open(psw_file, 'r')
    psw_file = psw_resource.readlines()
    psw_resource.close()

    psw_list = []

    for psw in psw_file:
        psw_list.append(psw.replace('\n', ''))

    return psw_list