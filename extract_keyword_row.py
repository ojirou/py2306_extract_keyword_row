import subprocess
import pandas as pd
import numpy as np
import openpyxl
import os
import glob
import datetime
BaseFolder = input('複数のcsvファイルが入っているフォルダを入力　>> ')
if(BaseFolder[-1:]!="\\"):
    BaseFolder=BaseFolder + '\\'
flags=[]
for FileName in os.listdir(BaseFolder):
    if FileName.endswith(".csv"):
        flags.append(FileName)
print(flags)
for flag in flags:
    file=BaseFolder+flag
    print(file)
    df=pd.read_csv(file, encoding='shift-jis', engine='python', skiprows=[], header=0)
    df=df.fillna({'利用店名':'欠損値'})
    df.head()
    df1=df.query('利用店名.str.contains(r"でんき|ガス|水道")', engine='python')
    ExlFile='C:\\Users\\user\\Downloads\\抽出結果_'+flag+'.xlsx'
    df1.to_excel(ExlFile)
    subprocess.Popen(["start", "", ExlFile], shell=True)