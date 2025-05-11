from PackageCredentials import PackageCredentials

def checkVersion(nodePackageProps: dict, strNodeModules: dict, dependencyPropsDic: dict, key: str):
    nodeVersion = nodePackageProps.get(strNodeModules+key)
    nodeVersionValue = nodeVersion['version']

    packageJsonValue = dependencyPropsDic[key]

    clearedJsonValue = packageJsonValue.replace("^", "")
    if nodeVersionValue != clearedJsonValue:
        if clearedJsonValue.isnumeric() == False:

            credential= PackageCredentials( key, nodeVersionValue, packageJsonValue)
        
    
        
            return credential

    else :
        return     
