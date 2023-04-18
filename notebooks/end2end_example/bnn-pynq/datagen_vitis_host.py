from dataset_loading import cifar

trainx, trainy, testx, testy, valx, valy = cifar.load_cifar_data("./", download=True, one_hot=False)
print(testx.shape)
print(testy.shape)


print(testx[0])
print(testy[0])

bsize = 64

test_imgs = testx
test_labels = testy

total = test_imgs.shape[0] # 10000
n_batches = int(total / bsize)

test_imgs = test_imgs[0:bsize]
print(test_imgs.shape)
test_labels = test_labels[0:bsize]
print(test_labels.shape)

# test_labels = test_labels.reshape(n_batches, bsize)

filedata = ""
ibuf_normal = test_imgs.flatten()
for val in ibuf_normal:
    # print(val)
    hex_val = '0x{:0{}X}'.format(val, 2)
    filedata = filedata + hex_val + ",\n"
    assert len(hex_val) == 4

with open("test_data.txt", "w") as outfile:
    outfile.write(filedata)


filedata = ""
expected = test_labels
for label in expected:
    filedata = filedata + str(label) + ",\n"
# print(ibuf_normal.shape)
# print(ibuf_normal)
# print(exp)

with open("expected.txt", "w") as outfile:
    outfile.write(filedata)










# import random
# import os
# import time
# from datetime import datetime
# from packaging.version import parse

# import torch
# import torchvision
# import torch.optim as optim
# from torch import nn
# from torch.optim.lr_scheduler import MultiStepLR
# from torch.utils.data import DataLoader
# from torchvision import transforms
# from torchvision.datasets import MNIST, CIFAR10

# num_wowrkers = 4
# random_seed = 1
# batch_size = 100

# random.seed(random_seed)
# torch.manual_seed(random_seed)
# torch.cuda.manual_seed_all(random_seed)

# # Datasets
# transform_to_tensor = transforms.Compose([transforms.ToTensor()])

# train_transforms_list = [transforms.RandomCrop(32, padding=4),
#                              transforms.RandomHorizontalFlip(),
#                              transforms.ToTensor()]
# transform_train = transforms.Compose(train_transforms_list)
# builder = CIFAR10


# train_set = builder(root="./",
#                     train=True,
#                     download=True,
#                     transform=transform_train)
# test_set = builder(root="./",
#                    train=False,
#                    download=True,
#                    transform=transform_to_tensor)
# train_loader = DataLoader(train_set,
#                             batch_size=batch_size,
#                             shuffle=True,
#                             num_workers=num_wowrkers)
# test_loader = DataLoader(test_set,
#                             batch_size=batch_size,
#                             shuffle=False,
#                             num_workers=num_wowrkers)

# count = 0
# for i, data in enumerate(test_loader):
#     print("i = " + str(i))
#     (input_data, target) = data
#     print("input_data = " + str(input_data))
#     print("target = " + str(target))

#     count = count + 1
#     if count == 1:
#         break


# def make_unsw_nb15_test_batches(bsize, dataset_root):
#     unsw_nb15_data = np.load(dataset_root + "/unsw_nb15_binarized.npz")["test"][:82000]
#     test_imgs = unsw_nb15_data[:, :-1]
#     test_labels = unsw_nb15_data[:, -1]
#     n_batches = int(test_imgs.shape[0] / bsize)
#     test_imgs = test_imgs.reshape(n_batches, bsize, -1)
#     test_labels = test_labels.reshape(n_batches, bsize)
#     return (test_imgs, test_labels)

# dataset_root = "."
# bsize = 1000

# (test_imgs, test_labels) = make_unsw_nb15_test_batches(bsize, dataset_root)
# # print(test_labels)
# # print(test_labels.shape)
# # print(test_labels[0].shape)
# # print(test_labels[0][0])



# filedata = ""
# val = ""
# count = 0
# for i in range(1024):
#     if i < 1000:
#         val = str(test_labels[0][i]) + val
#     else:
#         val = "0" + val
#     # filedata = filedata + str(test_labels[0][i])
#     if count == 511:

#         print(val)
#         hex_val = '{:0{}X}'.format(int(val, 2), len(val) // 4)
#         print(hex_val)
#         # print(hex_val[120 : 128])
#         for j in range(15,-1,-1):
#             filedata = filedata + "0x" + hex_val[8*j : 8*j + 8] + ",\n"
#             # print(hex_val[127-16*j:127-16*j-15])
#         val = ""
#     count = count + 1


# print(val)
# hex_val = '{:0{}X}'.format(int(val, 2), len(val) // 4)
# print(hex_val)

# # print("0b" + val)
# # print(hex_val)
# # print(hex_val[0:2])
# # print(hex_val[2:0])
# for j in range(15,-1,-1):
#     # print("0x" + hex_val[8*j : 8*j + 7] + ",")
#     filedata = filedata + "0x" + hex_val[8*j : 8*j + 8] + ",\n"

# with open("expected.txt", "w") as outfile:
#     outfile.write(filedata)



# img = test_imgs[0][0]
# # print(img)

# filedata = ""
# for i in range(1000):
#     img = test_imgs[0][i]
#     # print(img)
#     val = ""
#     count = 0
#     for j in range(593):
#         val = str(img[j]) + val

#         if count == 511:
#             hex_val = '{:0{}X}'.format(int(val, 2), len(val) // 4)
#             print(hex_val)
#             for j in range(15,-1,-1):
#                 filedata = filedata + "0x" + hex_val[8*j : 8*j + 8] + ",\n"
#             # print(val)
#             # filedata = ",\\ \n" + hex_val + filedata
#             # print("filedata is: " + filedata)
#             val = ""
#         count = count + 1
#     for j in range(431):
#         val = "0" + val # pad 0s
#         count = count + 1

#     hex_val = '{:0{}X}'.format(int(val, 2), len(val) // 4)
#     print(hex_val)
#     for j in range(15,-1,-1):
#         filedata = filedata + "0x" + hex_val[8*j : 8*j + 8] + ",\n"

#     # filedata = ",\\ \n" + hex_val + filedata
#     # print("filedata is: " + filedata)
#     assert(count == 1024)
#     # if(i == 2):
#     #     break
# # print(filedata)
# with open("test_data.txt", "w") as outfile:
#     outfile.write(filedata)
