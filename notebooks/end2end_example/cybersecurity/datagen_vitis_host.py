import numpy as np


def make_unsw_nb15_test_batches(bsize, dataset_root):
    unsw_nb15_data = np.load(dataset_root + "/unsw_nb15_binarized.npz")["test"][:82000]
    test_imgs = unsw_nb15_data[:, :-1]
    test_labels = unsw_nb15_data[:, -1]
    n_batches = int(test_imgs.shape[0] / bsize)
    test_imgs = test_imgs.reshape(n_batches, bsize, -1)
    test_labels = test_labels.reshape(n_batches, bsize)
    return (test_imgs, test_labels)

dataset_root = "."
bsize = 1000

(test_imgs, test_labels) = make_unsw_nb15_test_batches(bsize, dataset_root)
# print(test_labels)
# print(test_labels.shape)
# print(test_labels[0].shape)
# print(test_labels[0][0])



filedata = ""
val = ""
count = 0
for i in range(1024):
    if i < 1000:
        val = str(test_labels[0][i]) + val
    else:
        val = "0" + val
    # filedata = filedata + str(test_labels[0][i])
    if count == 511:

        print(val)
        hex_val = '{:0{}X}'.format(int(val, 2), len(val) // 4)
        print(hex_val)
        # print(hex_val[120 : 128])
        for j in range(15,-1,-1):
            filedata = filedata + "0x" + hex_val[8*j : 8*j + 8] + ",\n"
            # print(hex_val[127-16*j:127-16*j-15])
        val = ""
    count = count + 1


print(val)
hex_val = '{:0{}X}'.format(int(val, 2), len(val) // 4)
print(hex_val)

# print("0b" + val)
# print(hex_val)
# print(hex_val[0:2])
# print(hex_val[2:0])
for j in range(15,-1,-1):
    # print("0x" + hex_val[8*j : 8*j + 7] + ",")
    filedata = filedata + "0x" + hex_val[8*j : 8*j + 8] + ",\n"

with open("expected.txt", "w") as outfile:
    outfile.write(filedata)



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
