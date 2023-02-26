# 对称可搜索加密
# symmetric Searchable Encryption

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import hashlib

# 假设明文数据为 "hello world"
plaintext = "helloworldmakeas"
plaintext1 = plaintext.encode()
print(len(plaintext1))
# plaintext=pad(plaintext,16)
# print(len(plaintext))
# 生成AES密钥和IV向量
key = hashlib.sha256(b"mysecretkey").digest()
iv = hashlib.sha256(b"mysecret iv").digest()[:16]
# 使用AES-CBC模式加密明文数据
# iv=pad(iv,16)
print(iv)
print(len(key))
cipher = AES.new(key, AES.MODE_CBC, iv)
print(plaintext)
ciphertext = cipher.encrypt(plaintext.encode())
print(ciphertext)
# 计算明文数据的SHA-256哈希值
hash_value = hashlib.sha256(plaintext.encode()).hexdigest()
# 存储加密后的密文数据和哈希值
encrypted_data = {
    "ciphertext": ciphertext,
    "hash_value": hash_value
}
# print(encrypted_data)
# 假设搜索关键词为 "world"

search_word = "helloworldmakeas"

# 计算搜索关键词的SHA-256哈希值
search_hash = hashlib.sha256(search_word.encode()).hexdigest()
print("search_hash",search_hash)
print('hashvalue',encrypted_data["hash_value"])
# 解密并匹配哈希值
if search_hash == encrypted_data["hash_value"]:
    # 使用AES-CBC模式解密密文数据
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(encrypted_data["ciphertext"]).decode()
    print(plaintext)
    print("Matched! The plaintext is:", plaintext)
else:
    print("Not matched!")