# -*- coding:utf8 -*-
import os
import Image,ImageFilter

#LOMO
colormatrix_lomo = [1.7,  0.1, 0.1, 0, -73.1,0,  1.7, 0.1, 0, -73.1,0,  0.1, 1.6, 0, -73.1,0,  0, 0, 1.0, 0 ]
#黑白
colormatrix_heibai = [0.8,  1.6, 0.2, 0, -163.9,0.8,  1.6, 0.2, 0, -163.9,0.8,  1.6, 0.2, 0, -163.9,0,  0, 0, 1.0, 0 ]
#复古
colormatrix_huajiu = [0.2,0.5, 0.1, 0, 40.8,0.2, 0.5, 0.1, 0, 40.8, 0.2,0.5, 0.1, 0, 40.8, 0, 0, 0, 1, 0 ]
#哥特
colormatrix_gete = [1.9,-0.3, -0.2, 0,-87.0,-0.2, 1.7, -0.1, 0, -87.0, -0.1,-0.6, 2.0, 0, -87.0, 0, 0, 0, 1.0, 0]
#锐化
colormatrix_ruise = [4.8,-1.0, -0.1, 0,-388.4,-0.5,4.4, -0.1, 0,-388.4, -0.5,-1.0, 5.2, 0,-388.4,0, 0, 0, 1.0, 0]
#淡雅
colormatrix_danya = [0.6,0.3, 0.1, 0,73.3,0.2,0.7, 0.1, 0,73.3, 0.2,0.3, 0.4, 0,73.3,0, 0, 0, 1.0, 0 ]
#酒红
colormatrix_jiuhong = [1.2,0.0, 0.0, 0.0,0.0,0.0,0.9, 0.0, 0.0,0.0, 0.0,0.0, 0.8, 0.0,0.0,0, 0, 0, 1.0, 0]
#清宁
colormatrix_qingning = [0.9, 0, 0, 0, 0, 0, 1.1,0, 0, 0, 0, 0, 0.9, 0, 0, 0, 0, 0, 1.0, 0]
#浪漫
colormatrix_langman = [0.9, 0, 0, 0, 63.0, 0, 0.9,0, 0, 63.0, 0, 0, 0.9, 0, 63.0, 0, 0, 0, 1.0, 0 ]
#光晕
colormatrix_guangyun = [0.9, 0, 0,  0, 64.9,0, 0.9,0,  0, 64.9,0, 0, 0.9,  0, 64.9,0, 0, 0, 1.0, 0]
#蓝调
colormatrix_landiao = [2.1, -1.4, 0.6, 0.0, -31.0, -0.3, 2.0, -0.3, 0.0, -31.0,-1.1, -0.2, 2.6, 0.0, -31.0, 0.0, 0.0, 0.0, 1.0, 0.0]
#梦幻
colormatrix_menghuan = [0.8, 0.3, 0.1, 0.0, 46.5, 0.1, 0.9, 0.0, 0.0, 46.5, 0.1, 0.3, 0.7, 0.0, 46.5, 0.0, 0.0, 0.0, 1.0, 0.0]
#夜色
colormatrix_yese = [1.0, 0.0, 0.0, 0.0, -66.6,0.0, 1.1, 0.0, 0.0, -66.6, 0.0, 0.0, 1.0, 0.0, -66.6, 0.0, 0.0, 0.0, 1.0, 0.0]

def filterImage(imgpath,savepath,effect):
    img=Image.open(imgpath)
    w,h=img.size
    x,y=1,1
    newimg=Image.new("RGBA", img.size, 0xffffff)
    while x<w-1:
        while y<h-1:
            point=(x,y)
            r,g,b=0,0,0
            col,row=-1,-1
            while col<2:
                while row<2:
                    tr,tg,tb=img.getpixel((x + row,y + col))
                    alpha = 1
                    r,g,b,alpha = changeRGBA(tr,tg,tb,1,effect)
                    r = int(r)
                    g = int(g)
                    b = int(b)
                    row=row+1
                row=-1
                col=col+1                       
            newimg.putpixel((x,y),(r,g,b))
            y+=1
        y = 1
        x+=1
    newimg.save(savepath)
     


def changeRGBA(red,green,blue,alpha,f):
    redV = red
    greenV = green
    blueV = blue
    alphaV = alpha
    
    red = f[0] * redV + f[1] * greenV + f[2] * blueV + f[3] * alphaV + f[4]
    green = f[0+5] * redV + f[1+5] * greenV + f[2+5] * blueV + f[3+5] * alphaV + f[4+5]
    blue = f[0+5*2] * redV + f[1+5*2] * greenV + f[2+5*2] * blueV + f[3+5*2] * alphaV + f[4+5*2]
    alpha = f[0+5*3] * redV + f[1+5*3] * greenV + f[2+5*3] * blueV + f[3+5*3] * alphaV + f[4+5*3]
    
    if (red > 255):
        red = 255
    if(red < 0):
        red = 0;
    if (green > 255):
        green = 255
    if (green < 0):
        green = 0
    if (blue > 255):
        blue = 255
    if (blue < 0):
        blue = 0
    if (alpha > 255):
        alpha = 255
    if (alpha < 0):
        alpha = 0
    return red,green,blue,alpha


if __name__ == "__main__":
    filterImage("example.jpg","new_lomo.jpg",colormatrix_lomo)
    filterImage("example.jpg","new_heibai.jpg",colormatrix_heibai)
    filterImage("example.jpg","new_huajiu.jpg",colormatrix_huajiu)
    filterImage("example.jpg","new_gete.jpg",colormatrix_gete)
    filterImage("example.jpg","new_ruise.jpg",colormatrix_ruise)
    filterImage("example.jpg","new_danya.jpg",colormatrix_danya)
    filterImage("example.jpg","new_jiuhong.jpg",colormatrix_jiuhong)
    filterImage("example.jpg","new_qingning.jpg",colormatrix_qingning)
    filterImage("example.jpg","new_guangyun.jpg",colormatrix_guangyun)
    filterImage("example.jpg","new_landiao.jpg",colormatrix_landiao)
    filterImage("example.jpg","new_menghuan.jpg",colormatrix_menghuan)
    print 'Enjoy.'
