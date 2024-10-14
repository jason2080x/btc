import bitcoin
# pyinstaller --onefile --windowed btc.py
i = input("请输入密码: ")
private_key = bitcoin.hashlib.sha256(i.encode('utf-8')).hexdigest()
wif_private_key = bitcoin.encode_privkey(private_key, 'wif')
public_key = bitcoin.privtopub(private_key)
address = bitcoin.pubtoaddr(public_key)
print(wif_private_key)
print(address)
