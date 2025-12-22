import os

class create_mavm:
    def __init__(self, files="", file_out="video.mavm", r=None,verbose=False):
        self.file_out = file_out
        if r:
            files_names_txt = open(files, 'r')
            files_names     = files_names_txt.read().split('\n')
            files_names_txt.close()
            if verbose:
                print('file list information read')
            self.create_r(files=files_names,verbose=verbose) #aca se crea el archivo mavm en base a los otros archivos
        else:
            self.create_r(files=files)
    
    def create_r(self, files, verbose=False):
        files_d = []
        for file in files[0:]:
            try:
                file_f = open(file, 'rb')
                files_d.append([os.path.basename(file).encode("utf-8"),file_f.read()])
                file_f.close()
                if verbose:
                    print(f'file: "{os.path.basename(file)}" read')
            except Exception as e:
                print(e)
        
        file_bits_list = []
        for file_d in files_d:
            try:
                file_name, file_data = file_d
                file = b"".join([b"-++", file_name, b"+--", file_data])
                file_bits_list.append(file)
                if verbose:
                    print(f'file: "{file_name.decode("utf-8")}" packaged')
            except Exception as e:
                print(e)
        
        file_bits = b"".join(file_bits_list)
        file_out = open(self.file_out, 'bw')
        file_out.write(file_bits)
        if verbose:
            print('MaVM saved')
        file_out.close()