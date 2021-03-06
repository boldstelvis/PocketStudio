# PocketStudio

A simple tool to build Pocket Studio material files from a folder of textures

.mat files will be added to a subfolder called 'materials' for each unique prefix found within the collective texture filenames. 
Note the the script assumes a metallicRoughness material type

Appropriate image types are limited to png, jpg and tga (it will ignore any other filetypes found).
To function correctly, texture filenames should be formatted as: 

    'materialname_mapname.ext' 
    
(note the underscore used as delimiter)

The material will be named as per 'materialname'. Texture inputs for the material will be matched using 'mapname' as follows:

* 'Alb' -> Base colour (RGB)
* 'Emm' -> Emmission Colour (RGB)
* 'Met' -> Metaliic (Value)
* 'Nor' -> Normal (RGB encoded normals)
* 'Ref' -> Reflectance (Value)
* 'Rou' -> Roughness (Value)
* 'SSS' -> SSSweight (Value)
* 'Tra' -> Transmission (RGB)

mapname can be longer and still match correctly as long as it includes the denoted string - eg:

    'Mymesh_Albedo.png' 

will correctly match to the base colour map slot on a material called 'Mymesh.mat'


To use from within a python script:

    import build
    build.MatBuild("SomeValidFolderPath")

or call the script from the commandline:

    python build.py "SomeValidFolderPath"
