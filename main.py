import pandas
import subprocess
from tkinter import filedialog
import os

def exit_execution():
    exit()
    subprocess.call("cmd.exe /C exit", shell=True)

def transform_to(end_type:str, obj, filename: str):
    match end_type:
        case ".csv":
            pandas.DataFrame.to_csv(self=obj,path_or_buf=(filename+end_type))
        case ".xml":
            pandas.DataFrame.to_xml(self=obj,path_or_buffer=(filename+end_type))
        case ".json":
            pandas.DataFrame.to_json(self=obj,path_or_buf=(filename+end_type))
        case ".html":
            pandas.DataFrame.to_html(self=obj,buf=(filename+end_type))
        case ".orc":
            pandas.DataFrame.to_orc(self=obj,path=(filename+end_type))
        case ".xlsx":
            pandas.DataFrame.to_excel(self=obj, excel_writer=(filename+end_type))
        case ".feather":
            pandas.DataFrame.to_feather(self=obj,path=(filename+end_type))
        case ".paraquet":
            pandas.DataFrame.to_parquet(self=obj,path=(filename+end_type))
        case ".dta":
            pandas.DataFrame.to_stata(self=obj,path=(filename+end_type))
        case ".pkl":
            pandas.DataFrame.to_pickle(self=obj,path=(filename+end_type))
    print("File cloned into the new format, check before using. Do you wish tho convert another file (s/n):")
    redo = str(input()).capitalize()
    if redo == "S":
        print()
        main()
    else:
        exit_execution()

def sift(source_type: str, obj, filename: str):
    types = [".csv",".xml",".json",".html",".orc",".xlsx",".feather",".paraquet",".dta",".pkl"]
    types.remove(source_type)
    print("Adaptable to", end="")
    for t in types:
        print(f' "{t}",',end="")
    print(":")
    while True:
        end_type = str(input())
        if types.__contains__(end_type):
            break
        else:
            print("That is not one of the allowed types, try again:")
    transform_to(end_type, obj, filename)
        

def clasify(rute: str):
    filename, type = os.path.splitext(rute)
    obj = None
    parsed_rute=os.path.join(r'\\sprx', rute)
    match(type):
        case ".csv":
            obj = pandas.read_csv(parsed_rute)
        case ".xml":
            obj = pandas.read_xml(parsed_rute)
        case ".json":
            obj = pandas.read_json(parsed_rute)
        case ".html":
            obj = pandas.read_html(parsed_rute)
        case ".orc":
            obj = pandas.read_orc(parsed_rute)
        case ".xlsx":
            obj = pandas.read_excel(parsed_rute)
        case ".feather":
            obj = pandas.read_feather(parsed_rute)
        case ".paraquet":
            obj = pandas.read_parquet(parsed_rute)
        case ".dta":
            obj = pandas.read_stata(parsed_rute)
        case ".pkl":
            obj = pandas.read_pickle(parsed_rute)
        case _:
            print("This file's type isn't supported by this tool, please try again:")
            identify_file()
    sift(type, obj, filename)

def identify_file():
    ruta = None
    ruta = filedialog.askopenfilename()
    if(not ruta):
        exit_execution()
    else:
        clasify(ruta)

def main():
    print("Select the file to transform: ")
    identify_file()

if __name__=="__main__":
    main()







