# PocketStudio

A simple tool to build Pocket Studio material files from a folder of textures

.mat files for each materail will be added to a siubfolder called 'materials'

a mat file will be built for each unique prefix found within the collective texture filenames

appropriate image types are limited png, jpg and tga (it will ignore any other filetypes found)

to function correctly, texture filenames should be formatted as: 'materialname_mapname.ext'

the material will be named as per 'materialname'

texture inputs for the material will be matched using 'mapname' as follows:

'Alb' -> Base colour (RGB)
'Emm' -> Emmission Colour (RGB)
'Met' -> Metaliic (Value)
'Nor' -> Normal (RGB encoded normals)
'Ref' -> Reflectance (Value)
'Rou' -> Roughness (Value)
'SSS' -> SSSweight (Value)
'Tra' -> Transmission (RGB)

matname can be longer and still match correctly as long as they include the denoted strings - eg:

'Mymesh_Albedo.png' 

will correctly match to the base colour map slot on a mamterial called 'Mymesh.mat'

to use from within a python script:

import build
build.MatBuild("SomeValidTexturepath")

or call the script from the commandline:

python build.py "SomeValidTexturepath"
