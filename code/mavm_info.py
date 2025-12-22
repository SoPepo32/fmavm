import os

class mavm_info:
    def __init__(self, file='video.mavm', type_of_information=None, json_style=False):
        file_f = open(file,'br')
        file_data = file_f.read().split(b'-++')
        file_f.close()

        file_dat_json = {}
        for file_dat in file_data[1:]:
            file_name, file_d = file_d.split('+--')
            file_dat_json[file_name] = file_d
        
        if not(json_style):
            file_dat_extra = ''

            file_dat = ''
            for file_name, file_dat in file_dat_json.items():
                file_name_b = file_name.decode('utf-8')
                if file_name_b == 'metadata.json':
                    file_dat += 'file name: <<metadata.json>> file type: <json>/metadata\n'
                elif '.json' in file_name_b:
                    file_dat += f'file name: <<{file_name_b}>> file type: <json>/menu\n'
                elif '.opus' in file_name_b:
                    file_dat += f'file name: <<{file_name_b}>> file type: <opus>/sound\n'
                elif '.png' in file_name_b:
                    file_dat += f'file name: <<{file_name_b}>> file type: <png>/image\n'
                else:
                    file_dat_extra += f'file name: <<{file_name_b}>> file type: <{os.path.splitext(file_name_b)[1]}>\n'
                
            if type_of_information == 'embedded':
                file_dat_complete = f'embedded content:\n{file_dat_extra}'
            elif type_of_information == 'main_content':
                file_dat_complete = f'main content:\n{file_dat}'
            else:
                file_dat_complete = f'main content:\n{file_dat}\n\nembedded content:\n{file_dat_extra}'
                
            print(file_dat_complete)
        else:
            file_dat_extra = {}

            file_dat = []
            for file_name, file_dat in file_dat_json.items():
                if file_name.decode('utf-8') == 'metadata.json':
                    file_dat.append({'file_name': {file_name.decode('utf-8')}, 'file_type': 'json/metadata'})
                elif '.json' in file_name.decode('utf-8'):
                    file_dat.append({'file_name': {file_name.decode('utf-8')}, 'file_type': 'json/menu'})
                elif '.opus' in file_name.decode('utf-8'):
                    file_dat.append({'file_name': {file_name.decode('utf-8')}, 'file_type': 'opus/sound'})
                elif '.png' in file_name.decode('utf-8'):
                    file_dat.append({'file_name': {file_name.decode('utf-8')}, 'file_type': 'png/image'})
                else:
                    file_dat_extra.append({'file_name': {file_name.decode('utf-8')}, 'file_type': {os.path.splitext(file_name.decode('utf-8'))[1]}})
                
            if type_of_information == 'embedded':
                file_dat_complete = {'embedded content':file_dat_extra}
            elif type_of_information == 'main_content':
                file_dat_complete = {'main content':file_dat}
            else:
                file_dat_complete = {'embedded content':file_dat_extra,'main content':file_dat}
                
            print(file_dat_complete)