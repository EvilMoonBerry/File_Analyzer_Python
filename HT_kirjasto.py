# task_libraryHT
import sys
import datetime
# Tehdään olio lets make an object


class INFO:
    day = None
    weight = 0
# Aliohjelma, joka tulostaa käyttäjälle valikon ja tarkastaa käyttäjän syötteen / A subroutine that prints a menu to the user and checks the user's input


def menu():
    print("Mitä haluat tehdä:")
    print("1) Lue kuormatiedot"'\n'"2) Analysoi kuormatiedot"'\n'"3) Tallenna kuormien tulostiedot"'\n'"4) Analysoi viikonpäivittäin"'\n'"5) Analysoi kumulatiivisesti tiedostoon"'\n'"6) Analysoi kumulatiivisesti näytölle"'\n'"0) Lopeta")
    while True:
        try:
            choice = int(input("Valintasi: "))
            break
        except ValueError:
            print("Valintaa ei tunnistettu, yritä uudestaan.")
    return choice
# Aliohjelma, joka avaa tiedoston ja purkaa sen sisältämät tiedot olioon / # A subroutine that opens a file and unpacks the data it contains into an object


def reader():
    file_n = input("Anna kuormatietotiedoston nimi: ")
    things = []
    i = 0
    try:
        file_r = open(file_n, "r", encoding="UTF-8")
        while True:
            try:
                line = file_r.readline()
                if (len(line) == 0):
                    break
                else:
                    section = line[:-1].split(';')
                    info = INFO()
                    info.weight = int(section[2])
                    dayz = section[0] + section[1]
                    info.day = datetime.datetime.strptime(
                        dayz, "%d.%m.%Y%H:%M:%S")
                    things.append(info)
                    i = i + 1
            except ValueError:
                pass
    except Exception:
        print("Tiedoston '{0}' käsittelyssä virhe, lopetetaan.".format(file_n))
        sys.exit(0)
    file_r.close()
    print("Tiedosto '{0}' luettu, {1} riviä.".format(file_n, i))
    return things
# aliohjelma, joka saa parametrina paaohjelmalta listan, joka sisältää oliot. / a subroutine that receives a list of objects as a parameter from the main program.
# Puretaan tiedot ja lisätään listaan haluttavat tiedot / Extract the data and add the desired data to the list


def analyzer(info):
    i = 0
    stuff = []  # Luodaan lista, johon tiedot tallennetaan
    everything = 0
    min_kg = info[0].weight
    max_kg = info[0].weight
    pv_max = info[0].day
    pv_min = info[0].day
    last_pv = info[0].day
    first_pv = info[0].day
    for kg in info:
        i += 1
        everything += kg.weight
        if (first_pv > kg.day):
            first_pv = kg.day
        if (last_pv < kg.day):
            last_pv = kg.day
        if (min_kg > kg.weight):  # Etsitään pienin paino / Looking for the lowest weight
            min_kg = kg.weight
            pv_min = kg.day  # Pienimmän arvon saanut päivä / Day with the lowest value
        if (max_kg < kg.weight):  # Etsitään suurin arvo / Looking for the highest value
            max_kg = kg.weight
            pv_max = kg.day  # Suurimman arvon saanut päivä / The day with the highest value
    # Isoimman ja pienimmän arvon saaneiden päivien erotus / Difference between the days with the highest and lowest values
    d_day = pv_max - pv_min
    dayz = d_day.days
    pv_max = pv_max.strftime("%d.%m.%Y")
    pv_min = pv_min.strftime("%d.%m.%Y")
    # Lisätään tiedot listaan / Add information to the list
    stuff.append(max_kg)
    stuff.append(min_kg)
    stuff.append(everything)
    stuff.append(i)
    stuff.append(dayz)
    stuff.append(pv_max)
    stuff.append(pv_min)
    medium = int(everything/i)
    stuff.append(medium)
    left_d = last_pv - first_pv
    dz = left_d.days
    stuff.append(dz)
    first = first_pv.strftime("%d.%m.%Y")
    last = last_pv.strftime("%d.%m.%Y")
    print("Data analysoitu ajalta {0} - {1}.".format(first, last))
    return stuff
# Aliohjelma, joka tulostaa analyzoidut tidot ja lisää ne annettuun tiedostoon / A subroutine that prints the analysed tidbits and adds them to the given file


def writer(values):
    file_n = input("Anna tulostiedoston nimi: ")
    try:
        file_o = open(file_n, "w", encoding="UTF-8")
        text_0 = "Pienin jätekuorma tuli {0} ja oli {1} kg.".format(
            values[6], values[1])
        text_1 = "Suurin jätekuorma tuli {0} ja oli {1} kg.".format(
            values[5], values[0])
        text_2 = "Pienimmän ja suurimman kuorman toimitusten välissä oli {0} päivää.".format(
            values[4])
        text_3 = "Analyysijaksolla jätettä tuli yhteensä {0} kg.".format(
            values[2])
        text_4 = "Keskimäärin jätekuorma oli {0} kg.".format(values[7])
        text_5 = "Tulokset tallennettu tiedostoon '{0}'.".format(file_n)
        file_o.write(text_0 + '\n')
        # Kirjoitetaan lauseet tiedostoon / Write the sentences to a file
        file_o.write(text_1 + '\n')
        file_o.write(text_2 + '\n')
        file_o.write(text_3 + '\n')
        file_o.write(text_4 + '\n')
        print(text_0)
        print(text_1)
        print(text_2)
        print(text_3)
        print(text_4)
        print(text_5)
        file_o.close()  # Suljetaan tiedosto / Close the file
    except Exception:
        print("Tiedoston '{0}' käsittelyssä virhe, lopetetaan.".format(file_n))
        sys.exit(0)
    return None

# Aliohjelma joka analysoi datan ja printtaa paljonko jätettä kertyi viikonpäivinä / A subroutine that analyses the data and prints how much waste was accumulated per day of the week


def Analyze_week(data):
    # Tehdää kirjasto ja alustetaan se viikonpäivillä englanniksi koska kone lukee kaikki englanniksi. Annetaan jokaiselle viikonpäivälle(avaimelle) arvoksi 0
    # Make a library and format it on weekdays in English because the machine reads everything in English. Give each day of the week (key) a value of 0
    weekz = {"Monday": 0,
             "Tuesday": 0,
             "Wednesday": 0,
             "Thursday": 0,
             "Friday": 0,
             "Saturday": 0,
             "Sunday": 0}
    # Käydään data läpi pivä päivältä ja käytetään datetimea, etsieessämme samoja viikonpäiviä
    # Let's go through the data day by day and use datetime, looking for the same days of the week
    for t in data:
        day_g = datetime.datetime.date(t.day)
        day_h = day_g.strftime("%A")
        # Lisätään viikonpäivä avaimeen aina löydetyn saman viikonpäivän arvo / Always add the value of the same day of the week found to the key
        weekz[day_h] += t.weight

    # Koska tehtävän anto haluaa, että tiedot tulostetaan suomeksi, joten korvataan olemassa olevat englanninkieliset päivät suomalaisilla
    # Since the assigner wants the information to be printed in Finnish, so let's replace the existing English dates with Finnish ones
    # Avaimen Mondayn arvo on man / The value of the key Monday is man
    man = weekz["Monday"]
    # Annetaan vanha arvo uudelle / Give the old value to the new
    weekz["Maanantai"] = man
    del weekz["Monday"]  # Poistetaan vanha / Deleting the old
    # Jatketaan kaikille päiville / Let's continue for all days
    ti = weekz["Tuesday"]
    weekz["Tiistai"] = ti
    del weekz["Tuesday"]
    ke = weekz["Wednesday"]
    weekz["Keskiviikko"] = ke
    del weekz["Wednesday"]
    to = weekz["Thursday"]
    weekz["Torstai"] = to
    del weekz["Thursday"]
    pe = weekz["Friday"]
    weekz["Perjantai"] = pe
    del weekz["Friday"]
    la = weekz["Saturday"]
    weekz["Lauantai"] = la
    del weekz["Saturday"]
    su = weekz["Sunday"]
    weekz["Sunnuntai"] = su
    del weekz["Sunday"]

    # Tulostetaan kirjasto / Printed from the library
    print("Eri viikonpäivinä tuli seuraavat määrät jätettä:")
    for p in weekz:
        print("{0};{1}".format(p, weekz[p]))

    return None

# Aliohjelma, joka analysoi paaohjelmasta tulevan datan ja tallentaa sen tiedostoon / A subroutine that analyses the data from the main program and stores it in a file


def writer_flo(data, values):
    first_pv = data[0].day
    for kg in data:
        if (first_pv > kg.day):
            first_pv = kg.day
    result = {}  # Tehdään kirjasto johon alustetaan kaikki päivät / Let's make a library to initialise all the days
    # Alustettavien päivien määrä / Number of days to be scheduled
    dz = values[8]
    first = first_pv.strftime("%d.%m.%Y")
    for i in range(dz):  # Lisätään kirjastoon avain per päivä ja annetaan sille arvoksi 0 / Add a key per day to the library and set it to 0
        # Laitetaan kirjastoon muodossa "%d.%m.%Y" : 0 / Put in the library as "%d.%m.%Y" : 0
        result[first] = 0
        first = datetime.datetime.strptime(first, "%d.%m.%Y")
        first = first + datetime.timedelta(days=+1)
        first = first.strftime("%d.%m.%Y")

    waste = {}  # Laitetaan tiedostosta saadut päivät ja niiden jätemäärät kirjastoon ja järjestetään ne päivämäärän  / Put the dates from the file and their waste amounts in the library and organise them by date
    for u in data:
        waste[u.day] = u.weight
    s_waste = sorted(waste)

    for w in s_waste:  # Lisätään kirjaston waste tiedot kirjastoon result. Näin joka päivälle on arvo 0 tai kaikki sinä päivänä saapuneet roskat / Added library waste information to the library result. This way each day will have a value of 0 or all garbage received that day
        number = w.strftime("%d.%m.%Y")
        if number in result:
            result[number] += waste[w]
        else:
            result[number] = waste[w]
    # Lasketaan kumulatiivista määrää ja sijoitetaan niille päiville joina ei tullut roskia sen hetken kumulatiivinen jätemäärä /
    # Calculate the cumulative amount and place the cumulative amount of waste for the days when there was no litter at that time
    try:
        fold_o = open("kumulatiivinen.txt", "w", encoding="UTF-8")
        total = 0
        final_waste = {}
        text = "Jätettä kertyi vuoden aikana päivittäin seuraavalla tavalla:"
        fold_o.write(text+'\n')
        for l in result:  # Kirjoitetaan
            total = total + result[l]
            final_waste[l] = total
            line = "{0};{1}".format(l, total)
            fold_o.write(line + '\n')
        fold_o.close()
        print("Tiedosto 'kumulatiivinen.txt' tallennettu.")
    except Exception:
        print("Tiedoston käsittelyssä virhe")
        sys.exit(0)
    return None

# Aliohjelma, joka analysoi ja tulostaa pääohjelmalta tulleen datan. / A subroutine that analyses and prints the data from the main program.
# Tulostaa paljonko jätettä saapui päivittäin / Print how much waste arrived daily


def printer(data, values):
    # Alku on sama kuin aliohjelmassa writer_flo
    first_pv = data[0].day
    first_pv = data[0].day
    for kg in data:
        if (first_pv > kg.day):
            first_pv = kg.day
    result = {}
    dz = values[8]
    first = first_pv.strftime("%d.%m.%Y")
    for i in range(dz):
        result[first] = 0
        first = datetime.datetime.strptime(first, "%d.%m.%Y")
        first = first + datetime.timedelta(days=+1)
        first = first.strftime("%d.%m.%Y")

    waste = {}
    for u in data:
        waste[u.day] = u.weight
    s_waste = sorted(waste)

    for w in s_waste:
        number = w.strftime("%d.%m.%Y")
        if number in result:
            result[number] += waste[w]
        else:
            result[number] = waste[w]
    # Tulostetaan analyysi käyttäjälle / Print the analysis to the user
    print("Jätettä kertyi vuoden aikana päivittäin seuraavalla tavalla:")
    total = 0
    for l in result:
        total = total + result[l]
        print("{0};{1}".format(l, total))
    return None
