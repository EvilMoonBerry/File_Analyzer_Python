#task_Harjoitustyo_tavoite
######################################################################
# Päivämäärä: 16.11.2020
#######################################################################

import HT_kirjasto as stuff

def paaohjelma ():
    while True:
        choices = [1,2,3,4,5,6,0]
        try:
            choice = stuff.menu()
            a = choices[choice]
        except IndexError:
            print("Valintaa ei tunnistettu, yritä uudestaan.")
            pass
        else:
            try:
                if (choice == 0):
                    print("Kiitos ohjelman käytöstä.")
                    break
                elif (choice == 1):
                    info = stuff.reader()
                    print()
                elif (choice == 2):
                    values = stuff.analyzer(info)
                    data = info
                    print()
            except UnboundLocalError:
                print("Lista on tyhjä. Lue ensin tiedosto.")
                print()
            else:
                try:
                    if(choice == 3):
                        stuff.writer(values)
                        print()
                except UnboundLocalError:
                    print("Ei tuloksia. Analysoi data ennen tallennusta.")
                    print()
                else:
                    try:
                        if (choice == 4):
                            stuff.Analyze_week(data)
                            print()
                        elif (choice == 5):
                            stuff.writer_flo(data,values)
                            print()
                        elif (choice == 6):
                            stuff.printer(data,values)
                            print()
                    except UnboundLocalError:
                        print("Ei tuloksia. Analysoi data ensin.")
                        print()
                    
    return None

paaohjelma()