import os
import sys

def MatBuild(Folder):

    Meshes = []
    Base = {}
    Emission = {}
    Metal = {}
    Normal = {}
    Reflectance = {}
    Rough = {}
    SSS = {}
    Transmission = {}

    # parse files in folder passed to script -
    # sort through specific mesh names and assign paths to appropriate channel dicts

    try:
        os.path.exists(Folder)
    except:
        print ('Path: %s does not exist. Exiting program' % Folder)
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
                    if 'Ref' in parts[1]: Reflectance.update({parts[0]: file})
                    if 'Rou' in parts[1]: Rough.update({parts[0]: file})
                    if 'SSS' in parts[1]: SSS.update({parts[0]: file})
                    if 'Tra' in parts[1]: Transmission.update({parts[0]: file})

    # Create sub folder for material files

    Matpath = os.path.join(Folder, 'Materials')

    try:
        os.mkdir(Matpath)
    except:
        print ('%s already exists' % Matpath)

    # write files into subfolder
    i = 0
    for mesh in Meshes:

        Matname = mesh + '.mat'
        f = open(os.path.join(Matpath, Matname), 'w+')

        if mesh in Base: Basepath = os.path.join(Folder, Base[mesh])
        else: Basepath = ''
        if mesh in Emission: Emissionpath = os.path.join(Folder, Emission[mesh])
        else: Emissionpath = ''
        if mesh in Metal: Metalpath = os.path.join(Folder, Metal[mesh])
        else: Metalpath = ''
        if mesh in Normal: Normalpath = os.path.join(Folder, Normal[mesh])
        else: Normalpath = ''
        if mesh in Reflectance: Reflectancepath = os.path.join(Folder, Reflectance[mesh])
        else: Reflectancepath = ''
        if mesh in Rough: Roughpath = os.path.join(Folder, Rough[mesh])
        else: Roughpath = ''
        if mesh in SSS: SSSpath = os.path.join(Folder, SSS[mesh])
        else: SSSpath = ''
        if mesh in Transmission: Transmissionpath = os.path.join(Folder, Transmission[mesh])
        else: Transmissionpath = ''

        f.write('{\n')
        f.write('    "name": "%s", \n' % mesh)
        f.write('\n')
        f.write('    "model": "MetallicRoughness", \n')
        f.write('\n')
        f.write('    "baseColor": [ 1.0, 1.0, 1.0 ], \n')
        f.write('    "baseColorTexture": "%s", \n' % Basepath.replace('\\','/',))
        f.write('    "useBaseColorTextureAlpha": false, \n')
        f.write('    "metallic": 1.0, \n')
        f.write('    "metallicTexture": "%s", \n' % Metalpath.replace('\\','/',))
        f.write('    "reflectance": 0.5, \n')
        f.write('    "reflectanceTexture": "%s", \n' % Reflectancepath.replace('\\','/',))
        f.write('    "roughness": 1.0, \n')
        f.write('    "roughnessTexture": "%s", \n' % Roughpath.replace('\\','/',))
        f.write('\n')
        f.write('    "transmissionWeight": 0.0, \n')
        f.write('    "transmissionTexture": "%s", \n' % Transmissionpath.replace('\\','/',))
        f.write('    "transmissionColor": [ 1.0, 1.0, 1.0 ], \n')
        f.write('    "ior": 1.5, \n')
        f.write('\n')
        f.write('    "emissiveStrength": 0.0, \n')
        f.write('    "emissiveColor": [ 1.0, 1.0, 1.0 ], \n')
        f.write('    "emissiveTexture": "%s", \n' % Emissionpath.replace('\\','/',))
        f.write('\n')
        f.write('    "sssWeight": 0.0, \n')
        f.write('    "sssWeightTexture": "%s", \n' % SSSpath.replace('\\','/',))
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

    print('processed %s files in materials directory /n' % i)
    return()

if __name__ == "__main__":
    MatBuild(sys.argv[1])
