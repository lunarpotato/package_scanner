class PackageCredentials:
    def __init__(self, nodePackageName:str, nodePackageVersion:str, jsonPackageVersion:str):
        self.nodePackageName = nodePackageName
        self.nodePackageVersion = nodePackageVersion
        self.jsonPackageVersion = jsonPackageVersion