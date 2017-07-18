import click
import os
import sys
import subprocess
import termicoder.utils.display as display
import termicoder.utils.parse as parse
import json

lang_map={
".py":"python",
".c":"c",
".cpp":"cpp",
".cc":"cpp",
".c++":"cpp",
".java":"java"
}

def edit_templates():
    click.confirm("This will open the templates folder in file manager\n"+
    "Where you can edit templates for various languages\n"
    "Do you want to conitnue?",default=True,abort=True)
    templates_folder=os.path.join(os.path.dirname(__file__),"templates")
    click.launch(templates_folder)
    sys.exit()

def edit_defaults():
    click.confirm("This will open the json code default file\n"+
    "where you can edit default editors for various languages\n"
    "Do you want to conitnue?",default=True,abort=True)
    code_defaults_file=os.path.join(os.path.dirname(__file__),"code_defaults.json")
    click.launch(code_defaults_file)
    sys.exit()

# TODO: a default name for code file
def code(code_file):
    code_defaults_file=os.path.join(os.path.dirname(__file__),"code_defaults.json")
    f=open(code_defaults_file,"r")
    defaults=json.load(f)
    ext=os.path.splitext(code_file)[1]
    app=None

    if(ext in lang_map):
        if(os.path.exists(code_file)==False):
            templates_folder=os.path.join(os.path.dirname(__file__),"templates")
            lang_folder=lang_map[ext]
            lang_folder=os.path.join(templates_folder,lang_folder)
            try:
                template_file=os.path.join(lang_folder,"template"+ext)
                template=open(template_file,"r").readlines()
                f=open(code_file,"w")
                f.write(''.join(template))
                f.close()
            except:
                pass
        app=defaults[lang_map[ext]]

        if(app is None):
            click.launch(code_file)
        else:
            subprocess.call([app,code_file])

    else:
        display.error("termicoder doesn't support extension: "+ext)
