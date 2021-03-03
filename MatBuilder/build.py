import os
import sys
import time

def main(Folder):

    Meshes = []
    Base = {}
    Emission = {}
    Metal = {}
    Rough = {}
    Normal = {}

    # parse files in folder passed to script -
    # sort through specific mesh names and assign paths to appropriate channel dicts

    try:
        os.path.exists(Folder)
    except:
        print ('Path: %s does not exist. Exiting program' % Folder)
        time.sleep(2)
        exit()


    filelist = os.listdir(Folder)
    # print ('processing %s files in directory: %s /n' % (len(filelist), Folder))

    extensions = ('png','jpg','tga')
    for file in filelist:
        ext = file.split('.')
        if len(ext) > 1:
            if ext[1] in extensions:
                parts = ext[0].split('_')
                if parts[0] not in Meshes: Meshes.append(parts[0]) 
                if len(parts) > 1:
                    if 'Alb' in parts[1]: Base.update({parts[0]: file}) 
                    if 'Emi' in parts[1]: Emission.update({parts[0]: file}) 
                    if 'Met' in parts[1]: Metal.update({parts[0]: file})  
                    if 'Nor' in parts[1]: Normal.update({parts[0]: file}) 
                    if 'Rou' in parts[1]: Rough.update({parts[0]: file}) 
 
    # Create sub folder for material files

    Matpath = os.path.join(Folder, 'Materials')

    try:  
        os.mkdir(Matpath)  
    except OSError as error:  
        print(error)

    # write files into subfolder
    i = 1
    for mesh in Meshes:

        Matname = mesh + '.mat'
        f = open(os.path.join(Matpath, Matname), 'w+')

        if mesh in Base: Basepath = os.path.join(Folder, Base[mesh])
        else: Basepath = '' 
        if mesh in Emission: Emissionpath = os.path.join(Folder, Emission[mesh])
        else: Emissionpath = ''
        if mesh in Metal: Metalpath = os.path.join(Folder, Metal[mesh])
        else: Metalpath = ''
        if mesh in Rough: Roughpath = os.path.join(Folder, Rough[mesh])
        else: Roughpath = ''
        if mesh in Normal: Normalpath = os.path.join(Folder, Normal[mesh])
        else: Normalpath = ''

        f.write('{\n')
        f.write('    "name": "%s", \n' % mesh)
        f.write('\n')
        f.write('    "model": "MetallicRoughness", \n')
        f.write('\n')
        f.write('    "baseColor": [ 1.0, 1.0, 1.0 ], \n')
        f.write('    "baseColorTexture": "%s", \n' % Basepath.replace('\\','/',))
        f.write('    "useBaseColorTextureAlpha": true, \n')
        f.write('    "metallic": 1.0, \n')
        f.write('    "metallicTexture": "%s", \n' % Metalpath.replace('\\','/',))
        f.write('    "reflectance": 0.5, \n')
        f.write('    "reflectanceTexture": "", \n')
        f.write('    "roughness": 1.0, \n')
        f.write('    "roughnessTexture": "%s", \n' % Roughpath.replace('\\','/',))
        f.write('\n')
        f.write('    "transmissionWeight": 0.0, \n')
        f.write('    "transmissionTexture": "", \n')	
        f.write('    "transmissionColor": [ 1.0, 1.0, 1.0 ], \n')
        f.write('    "ior": 1.5, \n')
        f.write('\n')
        f.write('    "emissiveStrength": 0.0, \n')
        f.write('    "emissiveColor": [ 1.0, 1.0, 1.0 ], \n')
        f.write('    "emissiveTexture": "%s", \n' % Emissionpath.replace('\\','/',))
        f.write('\n')
        f.write('    "sssWeight": 0.0, \n')
        f.write('    "sssWeightTexture": "", \n')
        f.write('    "sssRadiusScale": 0.1, \n')	
        f.write('    "sssRadiusColor": [ 1.0, 1.0, 1.0 ], \n')
        f.write('\n')
        f.write('    "normalFactor": 1.0, \n')
        f.write('    "normalTexture": "%s" \n' % Normalpath.replace('\\','/',))
        f.write('}\n')
        f.write('\n')
        f.close()

        print ('processed material file for %s /n' % Matname)
        i = i + 1

    print('processed %s files in materials directory /n' %i)
    time.sleep(2)
    exit()



