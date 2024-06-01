import sqlite3
import os

def add_product(genre: str):
    try:
        database_path = 'diplom_database.db'
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        price = 0
        g_id = 0
        description = ""

        if conn:
            directory = f'D:/diplom_kartigo/diplom_kartigo/backend/src/music/genres/{genre}/'
            all_entries = os.listdir(directory)
            wav_files = [entry for entry in all_entries if os.path.isfile(os.path.join(directory, entry))]

            for wav in wav_files:
                if genre == 'Beat Switch Type Beat':
                    if wav == 'RESTYLING.mp3':
                        description = ("Подразумевает клубное и репрезентабельное настроение, "
                                       "что может передать ощущение стиля, моды и элегантности. "
                                       "Такая музыка может вдохновлять и создавать атмосферу в любом месте")
                    if wav == 'Счастливые люди.mp3':
                        description = ("Она передает настроение размышлений о том, что истинно счастливые люди "
                                       "наслаждаются моментами и радостью жизни")
                    price = 24.99
                    g_id = 1
                if genre == 'Lyrical':
                    if wav == 'BALADA.mp3':
                        description = ("Передает грустное, но одновременно и тёплое состояние "
                                       "непоколебимой надежды на лучшее")
                    if wav == 'DESERVE.mp3':
                        description = ("Данная композиция получилась эмоционально насыщенной с долей грусти и "
                                       "одновременно  вдохновением на преодоление трудностей")
                    price = 19.99
                    g_id = 2
                if genre == 'Reggaeton':
                    if wav == 'Baila Conmigo.mp3':
                        description = ("Танцевальная музыка с латинскими нотками. "
                                       "Такой ритм идеально подойдёт для песни, где лирический герой будет "
                                       "описывать сильные страстные чувства к своей возлюбленной")
                    if wav == 'Я и не знал.mp3':
                        description = ("Данная аранжировка пропитана болью и всплеском ностальгических эмоций. "
                                       "Идеально подойдёт артистам, которые делятся в "
                                       "своих песнях о истории неразделенной любви")
                    price = 29.99
                    g_id = 3
                if genre == 'Rock':
                    description = ("Под этот инструментал артисты могут высказаться о своём нелегком пути к "
                                   "мечте и о том, что только упорство и постоянный труд могут приблизить вас к ней")
                    price = 14.99
                    g_id = 4
                if genre == 'Trap':
                    if wav == 'Breaking Bad.mp3':
                        description = "Яркий динамичный бит для хип-хоп артистов. Тем может быть безгранично"
                    if wav == 'Закрытый клуб.mp3':
                        description = ("Этот бит передаёт уверенность и непоколебимую решимость. "
                                       "Идеальная композиция для того, чтобы стильно описать как "
                                       "ты становишься только лучше с каждый днем")
                    if wav == 'Я был прав.mp3':
                        description = ("Стильный и в то же время в меру агрессивный бит. "
                                       "Подойдет для артистов, которые хотят высказаться о том, "
                                       "как все были неправы раньше, когда утверждали, что ничего не получится")
                    price = 34.99
                    g_id = 5

                cursor.execute('''
                    INSERT INTO products (data_name, description, price, genre_id)
                    VALUES (?, ?, ?, ?)
                    ''', (wav, description, price, g_id))
                print(wav)
            conn.commit()
        else:
            conn.rollback()
        print("YES!!")
    except Exception as e:
        print("ERRORRRR:", e)


add_product('Beat Switch Type Beat')
add_product('Lyrical')
add_product('Reggaeton')
add_product('Rock')
add_product('Trap')