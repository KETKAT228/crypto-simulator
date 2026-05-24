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
    time.sleep(0.5)
    print("\rЗапуск программы.  ", end="")
    time.sleep(0.5)
    print("\rКонец запуска программы")
    time.sleep(0.5)
    clear_screen_with_logo() 
    break

charity = ["дом пристарелых", "детский дом", "детский садик", "городу", "офис KET_KAT"]

if os.path.exists("save.json"):
    with open("save.json", "r", encoding="utf-8") as file:
        save_data = json.load(file)
        monuy = save_data["money"]
        reputation = save_data["reputation"]
        day = save_data.get("day", 1)
        exchanges = save_data["exchanges"]
        real_estate = save_data.get("real_estate", {
            "трейлер": {"price": 5000, "req_rep": 0, "owned": 0, "income": 50},
            "квартира": {"price": 45000, "req_rep": 5, "owned": 0, "income": 300},
            "вилла": {"price": 250000, "req_rep": 25, "owned": 0, "income": 2000}
        })
    print("🚀 Прогресс успешно загружен из save.json!")
else:
    monuy = 10000
    reputation = 0
    day = 1
    exchanges = {
        "нефть": {"price": 161, "player_number_of_exchanges": 0},
        "биткоин": {"price": 349098, "player_number_of_exchanges": 0},
        "золото": {"price": 3213, "player_number_of_exchanges": 0},
        "платина": {"price": 14913, "player_number_of_exchanges": 0},
        "алмаз": {"price": 1000000, "player_number_of_exchanges": 0}
    }
    real_estate = {
        "трейлер": {"price": 5000, "req_rep": 0, "owned": 0, "income": 50},
        "квартира": {"price": 45000, "req_rep": 5, "owned": 0, "income": 300},
        "вилла": {"price": 250000, "req_rep": 25, "owned": 0, "income": 2000}
    }
    print("Приветствую тебя в симуляторе биржи! УДАЧИ, твой начальный баланс 10 000$")

while True:
    print(f"""
======================================
день: {day} | деньги: {monuy}$ | репутация: {reputation}
======================================
1. Купить актив
2. Продать актив
3. Лечь спать
4. Пожертвовать
5. Недвижимость
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
                print(f"Успешно куплено {buy_nember} шт. {player_buy} за {total_price}$!")
            else:
                print(f"Недостаточно денег! Нужно {total_price}$, у вас {monuy}$")
        else:
            print("Такого актива нет.")

    elif player_input_lobby == 2:
        clear_screen_with_logo()
        print("\n=== МОИ АКТИВЫ ===")
        count = 1
        for exchanges_, info in exchanges.items():
            print(f"{count}. Актив: {exchanges_} | Куплено: {info['player_number_of_exchanges']} шт. | Цена: {info['price']}$")
            count += 1
        
        player_sell = input("\nЧто сегодня хотите продать: ").lower().strip()

        if player_sell in exchanges:
            if exchanges[player_sell]["player_number_of_exchanges"] == 0:
                print(f"У вас нет активов '{player_sell}' для продажи.")
                continue
            try:
                sell_nember = int(input("Сколько штук? "))
                if sell_nember <= 0:
                    print("Количество должно быть больше нуля!")
                    continue
                if sell_nember > exchanges[player_sell]["player_number_of_exchanges"]:
                    print("У вас нет столько активов на балансе!")
                    continue
            except ValueError:
                print("Вводите количество числами")
                continue
            
            total_price = sell_nember * exchanges[player_sell]["price"]
            exchanges[player_sell]["player_number_of_exchanges"] -= sell_nember
            monuy += total_price
            print(f"Вы успешно продали {sell_nember} шт. {player_sell} за {total_price}$!")
        else:
            print("Такого актива нет в списке.")

    elif player_input_lobby == 3:
        clear_screen_with_logo()
        exchanges["нефть"]["price"] = random.randint(100, 1000)
        exchanges["биткоин"]["price"] = random.randint(20000, 100000)
        exchanges["золото"]["price"] = random.randint(1000, 7000)
        exchanges["платина"]["price"] = random.randint(10000, 32000)
        day += 1
        
        total_income = 0
        for home_name, home_info in real_estate.items():
            total_income += home_info["owned"] * home_info["income"]
        
        monuy += total_income
        print("Вы проснулись! Наступил новый торговый день.")
        if total_income > 0:
            print(f"Недвижимость принесла вам пассивный доход: +{total_income}$")

    elif player_input_lobby == 4:
        clear_screen_with_logo()
        print("\n=== БЛАГОТВОРИТЕЛЬНОСТЬ ===")
        count = 1
        for charity_ in charity:
            print(f"{count}. {charity_}")
            count += 1
        
        charity_buy = input("\nКуда пожертвуем (введи название): ").lower().strip()
        
        if charity_buy in charity:
            try:
                charity_number = int(input("Сколько долларов пожертвуем? "))
                if charity_number <= 0:
                    print("Сумма должна быть больше нуля!")
                    continue
            except ValueError:
                print("Вводите сумму числами!")
                continue
                
            if monuy < charity_number:
                print(f"У вас недостаточно денег! На балансе всего {monuy}$")
                continue
                
            monuy -= charity_number
            print(f"Вы успешно пожертвовали {charity_number}$ в '{charity_buy}'!")
            
            if charity_number <= 100:
                reputation += 1
            elif charity_number <= 1000:
                reputation += random.randint(1, 3)
            elif charity_number <= 10000:
                reputation += random.randint(2, 5)
            elif charity_number <= 100000:
                reputation += random.randint(4, 10)
            elif charity_number <= 1000000:
                reputation += random.randint(8, 20)
            else:
                reputation += random.randint(16, 100)
                
            print(f"Ваша репутация поднялась! Текущая репутация: {reputation}")
        else:
            print("Такого места нет в списке.")

    elif player_input_lobby == 5:
        clear_screen_with_logo()
        print("\n=== РЫНОК НЕДВИЖИМОСТИ ===")
        count = 1
        for home_name, home_info in real_estate.items():
            print(f"{count}. {home_name.capitalize()} | Куплено: {home_info['owned']} шт. | Цена: {home_info['price']}$ | Нужна репутация: {home_info['req_rep']} | Доход в день: +{home_info['income']}$")
            count += 1
            
        buy_home = input("\nКакую недвижимость хотите купить? ").lower().strip()
        
        if buy_home in real_estate:
            if reputation < real_estate[buy_home]["req_rep"]:
                print(f"У вас маловато репутации! Нужно хотя бы {real_estate[buy_home]['req_rep']}.")
                continue
            if monuy < real_estate[buy_home]["price"]:
                print("У вас недостаточно денег для покупки этой недвижимости!")
                continue
                
            monuy -= real_estate[buy_home]["price"]
            real_estate[buy_home]["owned"] += 1
            print(f"Поздравляем! Вы приобрели объект: {buy_home.capitalize()}!")
        else:
            print("Такого объекта недвижимости нет на рынке.")

    elif player_input_lobby == 0:
        clear_screen_with_logo()
        save_data = {
            "money": monuy,
            "reputation": reputation,
            "day": day,
            "exchanges": exchanges,
            "real_estate": real_estate
        }
        with open("save.json", "w", encoding="utf-8") as file:
            json.dump(save_data, file, indent=4, ensure_ascii=False)
            
        print("Прогресс успешно сохранен! До встречи!")
        break
        
    else:
        print("Число вне диапазона. Введите число от 0 до 5")
        
print("\nСпасибо, что попробовали продукт от KET_KAT")
