from dataset_loading import cifar

trainx, trainy, testx, testy, valx, valy = cifar.load_cifar_data("./", download=True, one_hot=False)
print(testx.shape)
print(testy.shape)


# print(testx[0])
# print(testy[0])

bsize = 640

test_imgs = testx
test_labels = testy

# total = test_imgs.shape[0] # 10000
# n_batches = int(total / bsize)

# test_imgs = test_imgs[0:bsize]
# print(test_imgs.shape)

# test_labels = test_labels.reshape(n_batches, bsize)


# Use 9600 out of 10000 for testing
for i in range(9600//bsize):
    print(i)
    for j in range(bsize//32): # write 32 images at the time
        filedata = ""
        test_imgs = testx[bsize*i + 32*j : bsize*i + 32*(j+1)]
        # print(test_imgs.shape)

        ibuf_normal = test_imgs.flatten()
        for val in ibuf_normal:
            # print(val)
            hex_val = '0x{:0{}X}'.format(val, 2)
            filedata = filedata + hex_val + ",\n"
            # assert len(hex_val) == 4
        if i == 0 and j == 0:
            with open("test_data.dat", "w") as outfile:
                outfile.write(filedata)
        else:
            with open("test_data.dat", "a") as outfile:
                outfile.write(filedata)



test_labels = test_labels[0:9600]
print(test_labels.shape)

filedata = ""
expected = test_labels
for label in expected:
    filedata = filedata + str(label) + ",\n"

with open("expected.dat", "w") as outfile:
    outfile.write(filedata)