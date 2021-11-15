import os
import requests
#from moviepy.editor import *

def heBingTsVideo(download_path,hebing_path):
    print("开始合并ts片段")
    all_ts = os.listdir(download_path)
    with open(hebing_path, 'wb+') as f:
        for i in range(len(all_ts)):
            ts_video_path = os.path.join(download_path, all_ts[i])
            f.write(open(ts_video_path, 'rb').read())
            print("\r正在处理第{:4d}个片段".format(i),end='')
    print("合并完成！！")

'''
def merge_to_video(download_path,hebing_path):
    L = []
    print("开始合并ts片段")
    all_ts = os.listdir(download_path)
    
    for i in range(len(all_ts)):
        ts_video_path = os.path.join(download_path, all_ts[i])
        video = VideoFileClip(ts_video_path)
        L.append(video)
        print("\r正在处理第{:4d}个片段".format(i),end='')
    final_clip = concatenate_videoclips(L)
    final_clip.to_videofile(hebing_path, fps=24, remove_temp=False)

    print("合并完成！！")
'''

def download(url,download_path):
    print("开始下载ts片段")

    all_content = requests.get(url).text # 获取M3U8的文件内容
    file_line = all_content.split("\n") # 读取文件里的每一行
    # 通过判断文件头来确定是否是M3U8文件
    if file_line[0] != "#EXTM3U":
        raise BaseException(u"非M3U8的链接")
    else:
        unknow = True   # 用来判断是否找到了下载的地址
        idx=1
        for index, line in enumerate(file_line):
            if "EXTINF" in line:
                unknow = False
                    # 拼出ts片段的URL
                pd_url = url.rsplit("/", 1)[0] + "/" + file_line[index + 1]
                res = requests.get(pd_url)
                c_fule_name = str(file_line[index + 1])
                print("\r正在下载第{:4d}个片段,已读到{:4d}行，共{:5d}行".format(idx,index,len(file_line)),end='')
                #print(url.rsplit("/", 1)[0],pd_url,c_fule_name)
                idx+=1
                with open(download_path + "\\" + c_fule_name, 'ab') as f:
                    f.write(res.content)
                    f.flush()

        if unknow:
            raise BaseException("未找到对应的下载链接")
        else:
            print("下载完成")
 
if __name__ == '__main__':
    # 参数设置（网址，片段保存文件夹，完整视频文件夹，视频名）
    url=input("请输入网址：")
    download_path =  "piece"
    convert_path= "all"
    convert_name=input("请输入保存视频名（默认为mp4文件，不用添加后缀）：")

    convert_fullname=convert_name+".mp4"

    # 创建文件夹
    if not os.path.exists(download_path):
        os.makedirs(download_path+'/'+convert_name)
        print("创建{}文件夹为片段保存文件夹\n".format(os.getcwd()+"\\"+download_path))
    else:
        os.mkdir(download_path+'/'+convert_name)
        print("文件夹{}已存在\n".format(os.getcwd()+"\\"+download_path))

    if not os.path.exists(convert_path):
        os.mkdir(convert_path)
        print("创建{}文件夹为完整视频保存文件夹\n".format(os.getcwd()+"\\"+convert_path))
    else:
        print("文件夹{}已存在\n".format(os.getcwd()+"\\"+convert_path))

    #视频路径
    convert_path=convert_path+"\\"+convert_fullname
    #下载片段
    download(url,download_path+'/'+convert_name )
    #合并片段
    heBingTsVideo(download_path+'/'+convert_name,convert_path)
    #merge_to_video(download_path+'/'+convert_name,convert_path)

    print("片段保存在{}\n完整视频保存在{}".format(os.getcwd()+"\\"+download_path,os.getcwd()+"\\"+convert_path))
    



