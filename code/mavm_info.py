import json
import os

class mavm_info:
    def __init__(self, file='video.mavm', type_of_information=None, json_style=False):
        file_f = open(file,'br')
        file_data = file_f.read().split(b'-++')
        file_f.close()

        file_dat_json = {}
        for file_dat in file_data[1:]:
            file_name, file_d = file_dat.split(b'+--')
            file_dat_json[file_name] = file_d
        
        if not(json_style):
            files_dat_extra = ''
            files_dat = ''
            mavm_v = ''
            for file_name, file_dat in file_dat_json.items():
                file_name_b = file_name.decode('utf-8')
                if 'metadata.json' == file_name_b:
                    file_dat_list = json.loads(file_dat.decode('utf-8'))
                    mavm_v = file_dat_list["mavm_version"]
                    files_dat += 'file name: <<metadata.json>> file type: <json>/metadata\n'
                elif '.json' in file_name_b:
                    files_dat += f'file name: <<{file_name_b}>> file type: <json>/menu\n'
                elif '.opus' in file_name_b:
                    files_dat += f'file name: <<{file_name_b}>> file type: <opus>/sound\n'
                elif '.png' in file_name_b:
                    files_dat += f'file name: <<{file_name_b}>> file type: <png>/image\n'
                elif '.mkv' in file_name_b:
                    files_dat += f'file name: <<{file_name_b}>> file type: <mkv>/video\n'
                else:
                    files_dat_extra += f'file name: <<{file_name_b}>> file type: <{os.path.splitext(file_name_b)[1]}>\n'
            
            file_dat_complete = f'MaVM version: {mavm_v}\n'
            if type_of_information == 'embedded':
                file_dat_complete += f'embedded content:\n{files_dat_extra}'
            elif type_of_information == 'main_content':
                file_dat_complete += f'main content:\n{files_dat}'
            else:
                file_dat_complete += f'main content:\n{files_dat}\n\nembedded content:\n{files_dat_extra}'
                
            print(file_dat_complete)
        else:
            files_dat_extra = []
            files_dat = []
            mavm_v = ''
            for file_name, file_dat in file_dat_json.items():
                file_name_b = file_name.decode('utf-8')
                if 'metadata.json' == file_name_b:
                    file_dat_list = json.loads(file_dat.decode('utf-8'))
                    mavm_v = file_dat_list["mavm_version"]
                    files_dat.append({'file_name': file_name_b, 'file_type': 'json/metadata'})
                elif '.json' in file_name_b:
                    files_dat.append({'file_name': file_name_b, 'file_type': 'json/menu'})
                elif '.opus' in file_name_b:
                    files_dat.append({'file_name': file_name_b, 'file_type': 'opus/sound'})
                elif '.png' in file_name_b:
                    files_dat.append({'file_name': file_name_b, 'file_type': 'png/image'})
                elif '.mkv' in file_name_b:
                    files_dat.append({'file_name': file_name_b, 'file_type': 'mkv/video'})
                else:
                    files_dat_extra.append({'file_name': file_name_b, 'file_type': os.path.splitext(file_name_b)[1]})
                
            if type_of_information == 'embedded':
                file_dat_complete = {'MaVM version':mavm_v,'embedded content':files_dat_extra}
            elif type_of_information == 'main_content':
                file_dat_complete = {'MaVM version':mavm_v,'main content':files_dat}
            else:
                file_dat_complete = {'MaVM version':mavm_v,'embedded content':files_dat_extra,'main content':files_dat}
                
            print(file_dat_complete)