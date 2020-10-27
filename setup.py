from cx_Freeze import setup, Executable
import json
import os

with open("setup.json", 'r', encoding='utf8') as f:
    obj = json.load(f)

setup(name=obj['name'],
      version=obj['version'],
      description=obj['description'],
      options={
          'build_exe':{
              'include_files': ['ki01-src', 'ko02-src', 'ko03-src', 'ko05-src', 'ko11-src', 'ko12-src']
              },
          'bdist_msi':{
              'upgrade_code': '{09682a48-7cc7-46bd-b646-0dd76cab0543}'
              }
          },
      executables=[Executable("program.py", icon='logo1.ico', targetName=obj['name'],
                              shortcutName=obj['name'], copyright=obj['copyright'], trademarks=obj['developer'],
                              shortcutDir="DesktopFolder")])
