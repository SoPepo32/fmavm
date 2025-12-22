#librerias
import argparse
import os

#otros scripts
from mavm_packer import create_mavm
from mavm_info import mavm_info
from extract import extract

class formato(argparse.HelpFormatter):
    def _split_lines(self, text, width):
        return text.splitlines()

def main():
    parser = argparse.ArgumentParser(description="mavm packager",formatter_class=formato)
    parser.add_argument("--verbose", action="store_true", help="detailed mode\n\n\n")


    parser.add_argument("--package", action="store_true", help="Option to package multiple files into a single MaVM file (version in the range of v.3.x.x)\n")

    parser.add_argument("--files_r", help="txt document with the files to import\n")
    parser.add_argument("--file", help="file to import (JSON/MKV/OPUS)\n")
    parser.add_argument("--file_out", help="output file in .mavm format\n\n\n", default="video.mavm")


    parser.add_argument("--information", action="store_true", help="Option to extract information (version in the range of v.3.x.x)\n")

    parser.add_argument("--file_i", help="MaVM file to extract the information\n")
    parser.add_argument("--type_of_information", help="type of information to extract (embedded/main_content)\n")
    parser.add_argument("--json_style", action="store_true", help="Option to select JSON style output\n\n\n")


    parser.add_argument("--extract", action="store_true", help="Option to extract information (version in the range of v.3.x.x)\n")

    parser.add_argument("--file_e", help="MaVM file to extract the content\n")
    parser.add_argument("--files_e", help='files to extract (format ["file1.json","file1.mkv","file.opus"])\n')
    parser.add_argument("--output_folder", help='output folder for the content to be extracted\n')

    args = parser.parse_args()
    
    if args.package:
        if not('.mavm' in args.file_out.lower()):
            print("The output file must be in .mavm format")
            exit()
        elif args.files_r == None and args.file == None:
            print("You need to set the input file(s).")
            exit()
        elif args.files_r != None and args.file != None:
            print("It is either a file or a list of files, not both.")
            exit()
        if args.files_r == None:
            create_mavm(files=args.file,file_out=args.file_out,verbose=args.verbose)
        elif args.file == None:
            create_mavm(files=args.files_r,file_out=args.file_out,r=True,verbose=args.verbose)
    elif args.information:
        if not('.mavm' in args.file_i.lower()):
            print("The file must be in MaVM format")
            exit()
        elif args.files_i == None:
            print("You need to set the input file.")
            exit()
        if args.type_of_information != None:
            mavm_info(file=args.file_i, type_of_information=args.type_of_information, json_style=args.json_style)
        else:
            mavm_info(file=args.file_i, json_style=args.json_style)
    elif args.extract:
        if not('.mavm' in args.file_e.lower()):
            print("The file must be in MaVM format")
            exit()
        elif args.file_e == None:
            print("You need to set the input file.")
            exit()
        if args.files_e == None:
            print("You need to specify the files to extract.")
            exit()
        else:
            extract(file=args.file_e, files=args.files_e,output_folder=args.output_folder,verbose=args.verbose)

main()
