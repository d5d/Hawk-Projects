# coding=utf-8
#下面的代码是接口函数，无关
def get(ar,index):
	l=len(ar);
	if index<0:
		return ar[l+index];
	else:
		return ar[index];
		
def execute(ar,filter,func):
	for r in ar:
		if filter(r):
			func(r);
unabled=[户型图存储方案,户型图存储,安居客户型列表,安居客评价,安居客楼盘详情,相册存储方案,安居客相册];
for e in unabled:
	e.etls[0].Enabled=False

execute(详细参数.etls,lambda x:x.TypeName=='WriteFileTextTF',lambda x:x.Enabled==False);

#下面是可能需要修改的配置:
###################################################

#是否要保存相册？不论是否保存，都会将相册的路径存入数据库中
get(安居客相册.etls,-1).Enabled=True

#是否要保存户型图？不论是否保存，都会将户型图的路径存入数据库中
get(户型图存储.etls,-1).Enabled=True	
	
#要采集的城市，使用正则表达式，如果包含全部城市，则写为''
get(安居客城市.etls,-1).Script='上海'
#户型图的存储路径
get(户型图存储方案.etls,-2).Format='E:\安居客图片\{0}\户型图\{1}_{2}_{3}.jpg'
#相册的存储路径
get(相册存储方案.etls,-2).Format='E:\安居客图片\{0}\相册\{1}_{2}_{3}.jpg'