import random
import os
import time
import json

def show_logo():
    print("""разработчики:
██╗░░██╗███████╗████████╗░░░░░░░░░██╗░░██╗░█████╗░████████╗
██║░██╔╝██╔════╝╚══██╔══╝░░░░░░░░░██║░██╔╝██╔══██╗╚══██╔══╝
█████╔╝░█████╗░░░░░██║░░░░░░░░░░░░█████╔╝░███████║░░░██║░░░
██╔═██╗░██╔══╝░░░░░██║░░░░░░░░░░░░██╔═██╗░██╔══██║░░░██║░░░
██║░░██╗███████╗░░░██║░░░███████╗░██║░░██╗██║░░██║░░░██║░░░
╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚══════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░
""")

def clear_screen_with_logo():
    os.system("cls" if os.name == "nt" else "clear")  
    show_logo()

show_logo() 
while True:
    print("\rЗапуск программы...", end="")
    time.sleep(0.3)
    print("\rЗапуск программы.. ", end="") 
    time.sleep(1)
    print("\rЗапуск программы.  ", end="")
    time.sleep(1)
    print("\rКонец запуска программы")
    time.sleep(1)
    clear_screen_with_logo() 
    break


if os.path.exists("save.json"):
    with open("save.json", "r", encoding="utf-8") as file:
        save_data = json.load(file)
        monuy = save_data["money"]
        reputation = save_data["reputation"]
        exchanges = save_data["exchanges"]
    print("🚀 Прогресс успешно загружен из save.json!")
else:
    monuy = 10000
    reputation = 0
    day = 0
    exchanges = {
        "нефть": {"price": 161, "player_number_of_exchanges": 0},
        "биткоин": {"price": 349098, "player_number_of_exchanges": 0},
        "золото": {"price": 3213, "player_number_of_exchanges": 0},
        "платина": {"price": 14913, "player_number_of_exchanges": 0},
        "алмаз": {"price": 1000000, "player_number_of_exchanges": 0}
    }

    charity = ["дом пристарелых","деский дом","детский садик","городу","офис KET_KAT"]
    print("Приветствую тебя в симуляторе биржи! УДАЧИ, твой начальный баланс 10 000$")

while True:
    print(f"""
день: {day}
деньги {monuy}$
репутация {reputation}
1. Купить
2. продать
3. лечь спать
4. пожертвовать
5. недвижимость
0. Выйти и сохранить прогресс
""")
    
    try:
        player_input_lobby = int(input("///  "))
    except ValueError:
        print("Пожалуйста, вводи цифры от 0 до 5")
        continue
    
    if player_input_lobby == 1:
        clear_screen_with_logo()
        print("\nСегодня у нас по курсу:")
        count = 1
        for exchanges_, info in exchanges.items():
            print(f"{count}. Актив: {exchanges_} | Куплено: {info['player_number_of_exchanges']} шт. | Цена: {info['price']}$")
            count += 1
        
        player_buy = input("\nЧто сегодня хотите купить: ").lower().strip()

        if player_buy in exchanges:
            try:
                buy_nember = int(input("Сколько штук? "))
                if buy_nember <= 0:
                    print("Количество должно быть больше нуля!")
                    continue
            except ValueError:
                print("Вводите количество числами")
                continue
                
            total_price = exchanges[player_buy]["price"] * buy_nember
            
            if monuy >= total_price:
                monuy -= total_price
                exchanges[player_buy]["player_number_of_exchanges"] += buy_nember
                print(f"Успешно! Куплено {buy_nember} шт. {player_buy} за {total_price}$")
            else:
                print(f"У вас недостаточно денег! Нужно {total_price}$, а у вас {monuy}$")
        else:
            print("Такого актива нет, присмотритесь к списку")
            
    elif player_input_lobby == 2:
        clear_screen_with_logo()
        print("\nмои активы")
        count = 1
        for exchanges_, info in exchanges.items():
            print(f"{count}. Актив: {exchanges_} | Куплено: {info['player_number_of_exchanges']} шт. | Цена: {info['price']}$")
            count += 1
        count = 0
        
        player_sell = input("\nЧто сегодня хотите продать: ").lower().strip()

        if player_sell in exchanges:
            try:
                sell_nember = int(input("Сколько штук? "))
                if sell_nember <= 0:
                    print("Количество должно быть больше нуля!")
                    continue
                if sell_nember > exchanges[player_sell]["player_number_of_exchanges"]:
                    print("у вас столько  нет")
                    continue
            except ValueError:
                print("Вводите количество числами")
                continue
            total_price = sell_nember * exchanges[player_sell]["price"]
            exchanges[player_sell]["player_number_of_exchanges"] -= sell_nember
            monuy += total_price
            print(f"Вы успешно продали {sell_nember} | по {player_sell}.шт | за {total_price}$!")

    elif player_input_lobby == 3:
        clear_screen_with_logo()
        exchanges["нефть"]["price"] = random.randint(100, 1000)
        exchanges["биткоин"]["price"] = random.randint(20000, 100000)
        exchanges["золото"]["price"] = random.randint(1000, 7000)
        exchanges["платина"]["price"] = random.randint(10000, 32000)
        day += 1
        print("вы проснулись!/n")
    elif player_input_lobby == 4:
        clear_screen_with_logo()
        for charity_ in charity.items():
            print(f"{count}. благотворительность: {charity_}")
            count += 1
        count = 0
        charity_buy = input("куда пожертвуем: ").lower().strip()
        if charity_buy in charity:
            try:
                charity_number = int(input("сколько: "))
                if monuy > charity_number:
                    print("у вас недостаточно денег")
                    continue
            except ValueError:
                print("вводите числами")
            monuy -= charity_number
            
            if charity_number <= 100:
                reputation += 1
            elif charity_number <= 1000:
                reputation += random.randint(1,3)
            elif charity_number <= 10000:
                reputation += random.randint(2,5)
            elif charity_number <= 100000:
                reputation += random.randint(4,10)
            elif charity_number <= 1000000:
                reputation += random.randint(8,20)
            else:
                reputation += random.randint(16,100)
            
    elif player_input_lobby == 5:
        clear_screen_with_logo()
        for exchanges_, info in exchanges.items():
            print(f"{count}. Актив: {exchanges_} | Куплено: {info['player_number_of_exchanges']} шт. | Цена: {info['price']}$")
            count += 1
        count = 0

    elif player_input_lobby == 0:
        clear_screen_with_logo()
        save_data = {
            "money": monuy,
            "reputation": reputation,
            "exchanges": exchanges
        }
        with open("save.json", "w", encoding="utf-8") as file:
            json.dump(save_data, file, indent=4, ensure_ascii=False)
            
        print("Прогресс успешно сохранен! До встречи!")
        break
    else:
        print("число вне диапозона. Введите число от 1, 5")
        
print("\nСпасибо, что попробовали продукт от KET_KAT")