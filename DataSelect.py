available_ingredients = { # Nguyen lieu co san trong tu lanh
    "ca chua" : 100,
    "thit heo" : 150,
    "bun" : 200,
    "suon bo" : 100,
    "ot" : 40,
    "xa lach" : 50,
    "bap bo" : 100
}
alergic_food = [ # Danh sach nguyen lieu nguoi dung bi di ung
    "thit than heo",
    "suon bo"
]
alergic_food = set(alergic_food) # Dung set de truy van trong O(1)
prices = { # Gia tien nguyen lieu tren thi truong (kg)
    "ca chua" : 40000, # 40000/kg
    "thit heo" : 150000,
    "bun" : 15000,
    "suon bo" : 100000,
    "ot" : 50000,
    "xa lach" : 50000,
    "bap bo" : 220000,
    "hanh" : 30000,
    "rau" : 50000,
    "nam bo" : 170000,
    "hanh la" : 20000,
    "gung" : 50000,
    "sa" : 30000,
    "thit than heo" : 130000,
    "hanh tim" : 30000,
    "toi" : 60000
}
# Cac thong tin ve nguyen lieu
need_ingredients1 = { # Mon 1 : Com tam
    "name of dish": "Com tam",
    "ingredients": {
        "suon bo": 400,
        "hanh": 15,
        "rau": 50
    }
}
need_ingredients2 = { # Mon 2 : Bun bo Hue
    "name of dish": "Bun bo Hue",
    "ingredients": {
        "bun": 300,
        "bap bo": 500,
        "nam bo": 500,
        "ot": 20,
        "hanh la": 20,
        "gung" : 50,
        "sa" : 100
    }
}
need_ingredients3 = { # Mon 3 : Bun thit nuong
    "name of dish": "Bun thit nuong",
    "ingredients": {
        "thit than heo": 500,
        "bun": 300,
        "xa lach": 100,
        "hanh tim": 50,
        "toi" : 20,
        "ot" : 20,
        "sa": 50
    }
}
dishes = [ # Danh sach cac mon an
    need_ingredients1,
    need_ingredients2,
    need_ingredients3
]
# prices_for_user = [0] * 3 # Gia tien ban dau cua moi mon an
list_price_and_dish = []
max_price_allowed = 500000 # Gia tien toi da cua nguoi dung cho bua an
for i in range(0, 3):
    price_of_current_dish = 0
    not_alergic = True
    for key, value in dishes[i]["ingredients"].items():
        if key in alergic_food: # Kiem tra xem nguoi dung co di ung voi nguyen lieu nay khong
            not_alergic = False
        if key in available_ingredients.keys(): # Neu co san trong tu lanh thi tru di tien cua nhung nguyen lieu nay
            price_of_current_dish += prices[key] * (max(0, value - available_ingredients[key]) / 1000)
        else: # Neu khong co san thi mua het
            price_of_current_dish += prices[key] * (value / 1000)
    if not_alergic and price_of_current_dish <= max_price_allowed:  # Neu khong di ung thi them vao danh sach
        list_price_and_dish.append((price_of_current_dish, dishes[i]["name of dish"]))
# Sort lai mon an theo gia giam dan
list_price_and_dish.sort(key = lambda x: x[0])
list_price_and_dish.reverse()
if len(list_price_and_dish) == 0: # Khong co mon an nao phu hop
    print("There aren't any dish suitable for your choice of price now :(")
else:   # In ra danh sach mon an va gia tien
    for price, name in list_price_and_dish:
        at_least_one_ok = True
        print(f"{name}: {price} VND")