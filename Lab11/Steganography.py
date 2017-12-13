import numpy as np
import scipy
import imageio
import zlib
import base64
import json as js
import copy

class Payload:

    def __init__(self, rawData=None, compressionLevel=-1, json=None):
        if rawData is not None:
            if not (isinstance(rawData, np.ndarray)):
                raise TypeError("rawData should be a numpy array of type uint8")
            if compressionLevel > 9 or compressionLevel < -1:
                raise ValueError("compressionlevel must be between -1 and 9")
            self.rawData = rawData
            norm_data = self.norm_foo(rawData)
            fin_string = self.compress_foo(norm_data, compressionLevel)

            self.json = self.gen_json(fin_string, compressionLevel, rawData)

        elif json is not None:
            try:
                json_object = js.loads(json)
            except:
                raise TypeError("json should be a json string")

            type1 = json_object["type"]
            if type1 == "text":
                compress1 = json_object["isCompressed"]
                content1 = json_object["content"]
                content1 = bytes(content1, "utf-8")
                content1 = base64.b64decode(content1)
                new_content = content1
                if compress1:
                    new_content = zlib.decompress(content1)
                d1_arr = np.frombuffer(new_content,dtype=np.uint8)
                self.rawData = d1_arr


            elif type1 == "gray":
                size1 = json_object["size"]
                row , col = size1.split(",")
                row = row.strip()
                col = col.strip()
                row = int(row)
                col =int(col)
                compress1 = json_object["isCompressed"]
                content1 = json_object["content"]
                content1 = bytes(content1, "utf-8")
                content1 = base64.b64decode(content1)
                new_content = content1
                if compress1:
                    new_content = zlib.decompress(content1)
                d1_arr = np.frombuffer(new_content,dtype=np.uint8)
                arr_2d = d1_arr.reshape((row,col))
                self.rawData = arr_2d

            elif type1 == "color":
                size1 = json_object["size"]
                row , col = size1.split(",")
                row = row.strip()
                col = col.strip()
                row = int(row)
                col =int(col)
                compress1 = json_object["isCompressed"]
                content1 = json_object["content"]
                content1 = bytes(content1, "utf-8")
                content1 = base64.b64decode(content1)
                new_content = content1
                if compress1:
                    new_content = zlib.decompress(content1)
                d1_arr = np.frombuffer(new_content,dtype=np.uint8)
                arr_3d = d1_arr.reshape((row,col,3))
                self.rawData = arr_3d

        else:
            raise ValueError("rawData and json are both None!!")


    def norm_foo(self, rawData):
        if rawData.ndim == 1:
            return rawData
        elif rawData.ndim == 2:
            return rawData.flatten()
        elif rawData.ndim == 3:
            row, col, wid = rawData.shape
            red = rawData[:, :, 0].flatten()
            green = rawData[:, :, 1].flatten()
            blue = rawData[:, :, 2].flatten()
            inter = np.ravel(np.column_stack((red,green,blue)))
            return inter


    def compress_foo(self,data, compresslvl):
        res = data
        if compresslvl != -1:
            res = zlib.compress(data,compresslvl)


        fin = base64.b64encode(res)
        fin_string = fin.decode("utf-8")
        pass

        return fin_string


    def gen_json(self,fin_string, compressionLevel, rawData):

        if compressionLevel != -1:
            compress = "true"
        else:
            compress= "false"

        if rawData.ndim == 1:
            type1 = "text"
            size1 = "null"
            return '{{"type":"{}","size":{},"isCompressed":{},"content":"{}"}}'.format(type1,size1,compress,fin_string)
        elif rawData.ndim == 2:
            type1 = "gray"
            row,col = rawData.shape
            size1 = "{},{}".format(row,col)
        elif rawData.ndim == 3:
            type1 = "color"
            row,col,trash = rawData.shape
            size1 = "{},{}".format(row,col)

        return '{{"type":"{}","size":"{}","isCompressed":{},"content":"{}"}}'.format(type1,size1,compress,fin_string)



class Carrier:

    def __init__(self, img):
        if not (isinstance(img, np.ndarray)):
                raise TypeError("img should be a numpy array of type uint8")

        if img.ndim < 3 :
                raise ValueError("img array must have 3 or more dimensions")
        row,col,dim = img.shape
        if dim < 4:
                raise ValueError("img array must have 4 or more channels")
        self.img = img

    def payloadExists(self):
        row,col,dim = self.img.shape
        msgcnt = 0
        final_str = ""
        for x in range(row):
            if(msgcnt == 4):
                break
            for y in range(col):
                if(msgcnt == 4):
                    break
                r = format(self.img[x][y][0], '08b')
                g = format(self.img[x][y][1], '08b')
                b = format(self.img[x][y][2], '08b')
                a = format(self.img[x][y][3], '08b')
                new_char = chr(int(a[6:8] + b[6:8] + g[6:8] + r[6:8],2))
                final_str += new_char
                msgcnt += 1
        if(final_str == '{"ty'):
            return True
        else:
            return False

    def clean(self):

        new_img = copy.deepcopy(self.img)
        row,col,dim = self.img.shape
        rand_arr = np.random.randint(4, size=(row, col,4))
        new_img_1 = np.bitwise_and(new_img, 252)
        new_img_2 = np.bitwise_or(new_img_1,rand_arr)

        return new_img_2

    def embedPayload(self, payload, override=False):
         if not isinstance(payload,Payload):
             raise TypeError("payload must be of type Payload")
         row,col,dim = self.img.shape
         if len(payload.json) > int((row*col)):
             raise ValueError("payload too large for carrier!")
         if override is False and self.payloadExists():
             raise Exception("carrier has payload already!")

         new_img = copy.deepcopy(self.img)

         msg_arr = np.fromstring(payload.json,dtype=np.uint8)

         msg_red = np.bitwise_and(msg_arr, 3)
         msg_green = np.right_shift(np.bitwise_and(msg_arr, 12), 2)
         msg_blue = np.right_shift(np.bitwise_and(msg_arr, 48), 4)
         msg_alpha = np.right_shift(msg_arr, 6)

         red = new_img[:, :, 0].flatten()
         green = new_img[:, :, 1].flatten()
         blue = new_img[:, :, 2].flatten()
         alpha = new_img[:, :, 3].flatten()


         new_red_1 = np.bitwise_and(red, 252)

         red[:msg_red.size] = np.bitwise_or(new_red_1[:msg_red.size],msg_red)

         new_green_1 = np.bitwise_and(green, 252)
         green[:msg_green.size] = np.bitwise_or(new_green_1[:msg_green.size],msg_green)

         new_blue_1 = np.bitwise_and(blue, 252)
         blue[:msg_blue.size] = np.bitwise_or(new_blue_1[:msg_blue.size],msg_blue)

         new_alpha_1 = np.bitwise_and(alpha, 252)
         alpha[:msg_alpha.size] = np.bitwise_or(new_alpha_1[:msg_alpha.size],msg_alpha)

         new_img[:, :, 0] =red.reshape(row,col)
         new_img[:, :, 1] =green.reshape(row,col)
         new_img[:, :, 2] =blue.reshape(row,col)
         new_img[:, :, 3] =alpha.reshape(row,col)

         return new_img


    def extractPayload(self):
        new_img = copy.deepcopy(self.img)


        red = new_img[:, :, 0].flatten()  #not sure why flatten
        green = new_img[:, :, 1].flatten()
        blue = new_img[:, :, 2].flatten()
        alpha = new_img[:, :, 3].flatten()


        new_green = np.left_shift(green, 2)
        new_blue = np.left_shift(blue, 4)
        new_alpha = np.left_shift(alpha, 6)


        new_new_red = np.bitwise_and(red,3)
        new_new_green = np.bitwise_and(new_green,12)
        new_new_blue = np.bitwise_and(new_blue,48)
        new_new_alpha = np.bitwise_and(new_alpha,192)

        fin1 = np.bitwise_or(new_new_red, new_new_green)
        fin2 = np.bitwise_or(fin1, new_new_blue)
        fin3 = np.bitwise_or(fin2, new_new_alpha)

        super_threshold_indices = fin3 > 126
        fin3[super_threshold_indices] = 0

        test = fin3.tostring()

        test2 = str(test, encoding='UTF-8')

        im, rest = test2.split("}",1)    #changed !!!!!!!!!!!!!!!!!!!!

        im = im + "}"



        return Payload(json=im)

if __name__== "__main__":
    pass
    #rawData = imageio.imread("projectfiles/data/payload1.png")
    #Payload(rawData, -1)

    #with open("projectfiles/data/payload1.json", "r") as xFile:
        #content = xFile.read()
        #payload = Payload(json=content)
    #print(scipy.__version__)
    #print(imageio.__version__)
    #test = imageio.imread("projectfiles/data/carrier.png")
    #payload = Carrier(test)
    #p = Payload(imageio.imread("projectfiles/data/payload1.png"), -1)
    #c = Carrier(imageio.imread("projectfiles/data/carrier.png"))
    #actualValue = c.embedPayload(p)
    #expectedValue = imageio.imread('projectfiles/data/embedded1_-1.png')
    #assertArrayEqual(expectedValue, actualValue)

    #clean1 = c.clean()

