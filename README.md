#非常简单基础的人脸核定练习作业demo

1.运行环境 Anaconda3

2.B度下载人物头像,如
```
python captureFace.py -n 郑爽

python captureFace.py -n 凯特·布兰切特

python captureFace.py -n 王心凌
```
3.运行训练
```
python train.py
```

4.复制待验证图片到 predict 目录（没有新建）

5.执行人脸核定
```
python predict.py
```

```
Using TensorFlow backend.
2017-11-06 13:44:09.229277: W c:\tf_jenkins\home\workspace\release-win\m\windows\py\35\tensorflow\core\platform\cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use SSE instructions,
 but these are available on your machine and could speed up CPU computations.
2017-11-06 13:44:09.229277: W c:\tf_jenkins\home\workspace\release-win\m\windows\py\35\tensorflow\core\platform\cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use SSE2 instructions
, but these are available on your machine and could speed up CPU computations.
2017-11-06 13:44:09.229277: W c:\tf_jenkins\home\workspace\release-win\m\windows\py\35\tensorflow\core\platform\cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use SSE3 instructions
, but these are available on your machine and could speed up CPU computations.
2017-11-06 13:44:09.230277: W c:\tf_jenkins\home\workspace\release-win\m\windows\py\35\tensorflow\core\platform\cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use SSE4.1 instructio
ns, but these are available on your machine and could speed up CPU computations.
2017-11-06 13:44:09.230277: W c:\tf_jenkins\home\workspace\release-win\m\windows\py\35\tensorflow\core\platform\cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use SSE4.2 instructio
ns, but these are available on your machine and could speed up CPU computations.
2017-11-06 13:44:09.231277: W c:\tf_jenkins\home\workspace\release-win\m\windows\py\35\tensorflow\core\platform\cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use AVX instructions,
 but these are available on your machine and could speed up CPU computations.
2017-11-06 13:44:09.231277: W c:\tf_jenkins\home\workspace\release-win\m\windows\py\35\tensorflow\core\platform\cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use AVX2 instructions
, but these are available on your machine and could speed up CPU computations.
2017-11-06 13:44:09.232277: W c:\tf_jenkins\home\workspace\release-win\m\windows\py\35\tensorflow\core\platform\cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use FMA instructions,
 but these are available on your machine and could speed up CPU computations.
Model is now loaded in the disk
1ed1b21c8701a18bd88a07ec9e2f07082838fe31.jpg-----------------
[[ 0.05205698  0.55930746  0.38863558]]
0.559307
王心凌
-----------------
下载.jpg-----------------
[[ 0.00136033  0.3319867   0.66665298]]
0.666653
郑爽
-----------------
微信图片_20171104163020.jpg-----------------
[[ 0.07029545  0.3921687   0.53753585]]
0.537536
郑爽
-----------------
微信图片_20171106130458.jpg-----------------
[[ 0.98938352  0.00379768  0.00681882]]
0.989384
凯特·布兰切特
-----------------
```