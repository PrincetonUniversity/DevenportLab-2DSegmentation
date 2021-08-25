from model import *
from data import *
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("--train", help="training dir")
parser.add_argument("--test", help="test dir")
parser.add_argument("--test_out", help="test output dir")
parser.add_argument("--res", help="resolution")
parser.add_argument("--name", help="model name")
parser.add_argument("--epoch", help="epoch count")
parser.add_argument("--steps", help="step count")
args = parser.parse_args()

res=int(args.res)
train_dir=args.train
test_dir=args.test 
model_ver=args.name
epoch_ctr=int(args.epoch)
step_ctr=int(args.steps)
testOpDir=args.test_out
# TRAIN
data_gen_args = dict(rotation_range=0.2,
                    width_shift_range=0.05,
                    height_shift_range=0.05,
                    shear_range=0.05,
                    zoom_range=0.05,
                    horizontal_flip=True,
                    fill_mode='nearest')
myGene = trainGenerator(16,train_dir,'image','label',data_gen_args,save_to_dir = None,target_size = (res,res))
model = unet(input_size = (res,res,1))
model_checkpoint = ModelCheckpoint(model_ver+'.hdf5', monitor='loss',verbose=1, save_best_only=True)
model.fit_generator(myGene,steps_per_epoch=step_ctr,epochs=epoch_ctr,callbacks=[model_checkpoint])

#TEST
filePathList=[]
for file in os.listdir(test_dir):
    filePath = os.path.join(test_dir, file)
    if re.match(r".*.png$", file) or re.match(r".*.tif$", file):
        filePathList.append(filePath)
testCtr=len(filePathList)
print("Number of tests:"+str(testCtr))
os.makedirs(testOpDir, 0o777, True)
testGene = testGeneratorDir(filePathList,target_size = (res,res))
model = unet(input_size = (res,res,1))
model.load_weights(model_ver+'.hdf5')
results = model.predict_generator(testGene,testCtr,verbose=1)
saveResult(testOpDir,results)