import datetime
import lorem
import psycopg2
import pytz
import random


def random_date():
    seconds = random.randint(0, 157784630)
    return pytz.timezone('utc').localize(
        datetime.datetime(2013, 1, 1, 0, 0,) +
        datetime.timedelta(seconds=seconds)
    )


if __name__ == '__main__':
    connection = psycopg2.connect(
        'host=localhost dbname=szkolenie user=zefciu password=zelgad00'
    )
    cursor = connection.cursor()
    # tuples = []
    # for i in range(1000000):
    #     tuples.append(cursor.mogrify('(%s, %s, %s)', (random.randint(1, 100000), lorem.sentence(), random_date())))

    #     if i % 1000 == 0:
    #         tuples_block = b','.join(tuples)
    #         print(i//1000)
    #         cursor.execute(
    #             b'INSERT INTO wpisy(autor_id, tresc, utworzony) VALUES ' + tuples_block
    #         )
    #         tuples = []
    connection.commit()

    tuples = []
    for i in range(10000000):
        tuples.append(cursor.mogrify(
            '(%s, %s, %s, %s)',
            (
                random.randint(1, 100000),
                random.randint(2, 999002),
                lorem.sentence(),
                random_date())
            )
        )
        if i % 1000 == 0:
            tuples_block = b','.join(tuples)
            print(i//1000)
            cursor.execute(
                b'INSERT INTO komentarze(autor_id, wpis_id, tresc, utworzony) VALUES ' + tuples_block
            )
            tuples = []
    connection.commit()
