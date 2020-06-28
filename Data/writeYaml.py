import yaml

data = { "Search_Data":{
    "search_test_002":{"expect": {'value':"你好"},'value':"你好"},
    "search_test_001":{"expect": [1,2,3,4],'value':1234}
}
}

# 在data目录下新建abc.yml文件，并写入data字典数据
# 打开文件 指定 encoding="utf8"
with open("./abd.yml",'a',encoding="utf8") as f:    # f 待写入文件对象
    # 写入yaml数据
    yaml.safe_dump(data,f,encoding="utf8",allow_unicode=True)