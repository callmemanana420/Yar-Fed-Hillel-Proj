ukranian_word_day = str()

sec = int(input("Введіть кількість секунд(0-8640000): "))

if 0 <= sec <= 8640000:
    sec_in_day = 24 * 60 * 60
    sec_in_houre = 60 * 60
    sec_in_minute = 60

    days = str(sec // sec_in_day)
    hours = str(sec % sec_in_day // sec_in_houre).zfill(2)
    minutes = str(sec % sec_in_day % sec_in_houre // sec_in_minute).zfill(2)
    seconds = str(sec % sec_in_day % sec_in_houre % sec_in_minute).zfill(2)

    

    if int(days[-1]) == 0 or int(days[-1]) >= 5 or 5 <= int(days) < 20:
        ukranian_word_day = "днів"

    elif int(days[-1]) == 1:
        ukranian_word_day = "день"
        
    else:
        ukranian_word_day = "дні"

    print(f"{days} {ukranian_word_day}, {hours}:{minutes}:{seconds}")
else:
    print("Неправильний інпут!")

