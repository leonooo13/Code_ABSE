## 可搜索加密计算流程
1. 本地明文使用AES加密，和hash值上传到云端组成字典
2. 本地搜索值hash后进行与云端的hash值进行比较，如果相等将字典中的加密进行进行解密输出
3. 不相等，不匹配