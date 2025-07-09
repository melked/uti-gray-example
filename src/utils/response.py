
from sdks.novavision.src.helper.package import PackageHelper
from components.Rotation.src.models.PackageModel import PackageModel, PackageConfigs, ConfigExecutor, GrayOutputs, GrayResponse, GrayExecutor, OutputImage


def build_response(context):
    outputImage = OutputImage(value=context.image)
    Outputs = GrayOutputs(outputImage=outputImage)
    grayResponse = GrayResponse(outputs=Outputs)
    grayExecutor = GrayExecutor(value=grayResponse)
    executor = ConfigExecutor(value=grayExecutor)
    packageConfigs = PackageConfigs(executor=executor)
    package = PackageHelper(packageModel=PackageModel, packageConfigs=packageConfigs)
    packageModel = package.build_model(context)
    return packageModel