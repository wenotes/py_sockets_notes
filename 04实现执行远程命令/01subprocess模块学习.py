#coding:utf-8
"""

"""

import subprocess

while True:
	cmd = input('请输入命令>>>')
	cmd = cmd.strip()
	if not cmd:
		print('命令不能为空，',end='')
		continue
	if cmd=='exit':
		break
	# 执行命令，并返回命令结果
	sp_obj = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
	# shell，stdout
	# stdout=subprocess.PIPE 意思是把命令的执行结果放到管道里面。
	# stdin=subprocess.PIPE 意思是把命令放到管道里面。
	# stderr=subprocess.PIPE 意思是把命令的执行错误结果放到管道里面。
	
	res_out1 = sp_obj.stdout.read().decode('gbk')
	res_out2 = sp_obj.stdout.read().decode('gbk')
	print('第一次取出stdout管道内容 ==>\n',res_out1)
	print('第二次取出stdout管道内容 ==>',res_out2) #再次打印就没有命令执行结果了

	res_in = sp_obj.stdin #stdin 不能read，先不管这个
	print('取出stdin内容',res_in, res_in.readable())

	res_err = sp_obj.stderr.read().decode('gbk')
	print('取出stderr内容',res_err)
