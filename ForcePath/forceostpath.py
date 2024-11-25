import winreg

# レジストリベースキー
key_base = r"HKEY_CURRENT_USER\Software\Microsoft\Office"

# 各バージョンのレジストリキー名
versions = ["14.0", "15.0", "16.0"]

# 設定するOSTファイルのパス
ost_path = r"C:\Your\OST\Path"

for version in versions:
    key_path = f"{key_base}\{version}\Outlook"

    try:
        # レジストリキーを開く
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_ALL_ACCESS) as key:
            # レジストリ値を設定
            winreg.SetValueEx(key, "ForceOSTPath", 0, winreg.REG_SZ, ost_path)
            print(f"Found Outlook version: {version}")
            break
    except FileNotFoundError:
        # キーが見つからない場合の処理
        pass