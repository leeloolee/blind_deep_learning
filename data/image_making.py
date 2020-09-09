import pandas as pd
import argparse
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib


parser = argparse.ArgumentParser(description = "this code makes csv file to image")

parser.add_argument("--train-data", default = "./train.csv", type = str, help = "arrnrn")
parser.add_argument("--test-data", default = "./test.csv", type = str, help = "arrnrn")

args = parser.parse_args()

def main(args):
    if not os.path.isdir("./images"):
        os.mkdir("./images")
        os.mkdir("./images/train")
        os.mkdir("./images/test")

    train_data_csv = pd.read_csv(args.train_data)
    test_data_csv = pd.read_csv(args.test_data)

    ## train row to image
    for i, data in enumerate(train_data_csv):
        image = np.array(train_data_csv.iloc[i, 3:]).reshape(28,28).astype(float)
        matplotlib.image.imsave('images/train/train_image_'+str(i)+'.png', image)

    for i, data in enumerate(test_data_csv):
        image = np.array(test_data_csv.iloc[i, 2:]).reshape(28,28).astype(float)
        matplotlib.image.imsave('images/test/test_image_'+str(i)+'.png', image)


if __name__ == "__main__":
    main(args)
