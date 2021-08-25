from model import *
from data import *
import skimage.io as io
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("--test_dir_file", help="test filename or directory")
parser.add_argument("--model_dir", help="model directory")
parser.add_argument("--res", help="resolution")
parser.add_argument("--name", help="model name")
parser.add_argument("--force_rerun", help="force re-run of the model")
parser.add_argument("--thresh_window", help="window size for local thresholding.")
args = parser.parse_args()

res = int(args.res)
test_dir_file = args.test_dir_file.strip()
model_ver = args.name
model_dir = args.model_dir
thresh_window = int(args.thresh_window)
force_rerun = int(args.force_rerun)
#TEST

if os.path.isfile(test_dir_file):
    test_dir = os.path.dirname(test_dir_file)
    test_basename = os.path.basename(test_dir_file)
    test_basename = os.path.splitext(test_basename)[0]
    testOpDir = os.path.join(test_dir,test_basename)
    os.makedirs(testOpDir, 0o777, True)
    img = io.imread(test_dir_file, as_gray=True)
    h, w = img.shape
    if force_rerun == 0 and os.path.exists(os.path.join(testOpDir, "%s_predict.png" % test_basename)):
        img_inv = io.imread(os.path.join(testOpDir, "%s_predict.png" % test_basename))
        postProcessFile(testOpDir, img_inv, test_basename, thresh_window)
    else:
        testGene = testGeneratorFile(test_dir_file,target_size = (res,res))
        model = unet(input_size = (res,res,1))
        model_path = os.path.join(model_dir,model_ver+".hdf5")
        model.load_weights(model_path)
        results = model.predict(testGene,verbose=1)
        saveResultFile(testOpDir,results,test_basename,thresh_window,(h, w))
elif os.path.isdir(test_dir_file):
    filePathList=[]
    inputResList=[]
    for file in os.listdir(test_dir_file):
        filePath = os.path.join(test_dir_file, file)
        if re.match(r".*.png$", file) or re.match(r".*.tif$", file):
            filePathList.append(filePath)
            img = io.imread(filePath, as_gray=True)
            h, w = img.shape
            inputResList.append((h,w))

    testGene = testGeneratorDir(filePathList, target_size=(res, res))
    model = unet(input_size=(res, res, 1))
    model_path = os.path.join(model_dir, model_ver + ".hdf5")
    model.load_weights(model_path)
    results = model.predict_generator(testGene, len(filePathList), verbose=1)
    saveResultDir(filePathList, results, thresh_window, inputResList)






