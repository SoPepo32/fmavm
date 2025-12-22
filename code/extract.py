import os

class extract:
    def __init__(self, file, files, output_folder='', verbose=False):
        file_f = open(file,'br')
        file_data = file_f.read().split(b'-++')
        if verbose:
            print('MaVM file read')
        file_f.close()

        file_dat_json = {}
        for file_dat in file_data[1:]:
            file_name, file_d = file_d.split(b'+--')
            file_dat_json[file_name.decode('utf-8')] = file_d
            if verbose:
                file_name_b = file_name.decode('utf-8')
                print(f'Information extracted from the object: "{file_name_b}"')
        
        files_list = json.loads(files)
        for file_extract in files_list:
            file_fo = open(os.path.join(output_folder,file_extract),'bw')
            file_fo.write(file_dat_json[file_extract])
            file_fo.close()
            if verbose:
                print(f'Object: "{file_extract}" extracted')