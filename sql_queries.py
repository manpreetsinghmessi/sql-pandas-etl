# DROP TABLES

songplay_table_drop = "drop table if exists songplays"
user_table_drop = "drop table if exists users"
song_table_drop = "drop table if exists songs"
artist_table_drop = "drop table if exists artists"
time_table_drop = "drop table if exists time"

# CREATE TABLES

songplay_table_create = ("""create table if not exists songplays  (songplay_id SERIAL PRIMARY KEY, start_time bigint not null, user_id int, level varchar, song_id varchar, artist_id varchar, session_id int, location varchar, user_agent varchar)
""")

user_table_create = ("""create table if not exists users (user_id int primary key, first_name varchar, last_name varchar , gender char , level varchar)
""")

song_table_create = ("""create table if not exists songs (song_id varchar primary key, title varchar, artist_id varchar, year int, duration float)
""")

artist_table_create = ("""create table if not exists artists (artist_id varchar primary key, name varchar, location varchar, latitude float, longitude float) """)

time_table_create = ("""create table if not exists time (start_time timestamp not null , hour int, day int, week int, month int, year int, weekday int)
""")

# INSERT RECORDS

songplay_table_insert = ("""insert into songplays(start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) values(%s,%s,%s,%s,%s,%s,%s,%s)""")

user_table_insert = ("""insert into users(user_id, first_name, last_name, gender, level) values(%s,%s,%s,%s,%s)
 ON CONFLICT (user_id) DO UPDATE
    SET level = excluded.level """)

song_table_insert = ("""insert into songs(song_id, title, artist_id, year, duration) values(%s,%s,%s,%s,%s)
ON CONFLICT (song_id) DO NOTHING """)

artist_table_insert = ("""INSERT INTO artists
    (artist_id, name, location, latitude, longitude)
VALUES
    (%s, %s, %s, %s, %s)
ON CONFLICT (artist_id) DO NOTHING
""")


time_table_insert = ("""insert into time(start_time, hour, day, week, month, year, weekday) values(%s,%s,%s,%s,%s,%s,%s)
""")

# FIND SONGS

song_select = (""" SELECT
    s.song_id, s.artist_id
FROM
    songs s
        JOIN artists a ON s.artist_id = a.artist_id
WHERE
    s.title = %s
    AND a.name = %s
    AND s.duration = %s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]