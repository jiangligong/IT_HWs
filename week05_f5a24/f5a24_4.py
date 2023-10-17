print("f5a24黎家暉")

import my_unit_change as muc

def choose() :
    print("""
選擇單位轉換的編號
1.暫停程序
2.吋->呎
3.公斤->公噸
4.米每秒->公里每小時
""")
    choose = int(input("請輸入編號："))
    if choose == 1 :
        pass
    elif choose == 2 :
        feet_to_inch()
    elif choose == 3 :
        kg_to_tonne()
    elif choose == 4 :
        mpers_to_kmperh()

def feet_to_inch() :
    feet = float(input("？吋->呎："))
    print(f"{feet}吋相當於{muc.feet_to_inch(feet)}呎\n")
    choose()

def kg_to_tonne() :
    kg = float(input("？公斤->公噸："))
    print(f"{kg}公斤相當於{muc.kg_to_tonne(kg)}公噸")
    choose()

def mpers_to_kmperh() :
    mpers = float(input("？米每秒->公里每小時："))
    print(f"{mpers}米每秒相當於{muc.mpers_to_kmperh(mpers)}公里每小時")
    choose()

choose()