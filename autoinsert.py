import requests

def map_score_to_rating(score):
    if score >= 8:
        return '5'
    elif score >= 6:
        return '4'
    elif score >= 4:
        return '3'
    elif score >= 2:
        return '2'
    else:
        return '1'

def sanitize(text):
    return text.replace("'", "''") if text else ''

insert_values = []

for page in range(1, 5):  # Adjust range to fetch more
    res = requests.get(f'https://api.jikan.moe/v4/top/anime?page={page}')
    if res.status_code != 200:
        print("Failed to fetch data on page", page)
        continue

    data = res.json()['data']

    for anime in data:
        title = sanitize(anime.get('title'))
        type_ = anime.get('type')
        if type_ == 'TV Special':
            type_ = 'Special'
        elif type_ not in ['TV', 'Movie', 'ONA', 'OVA', 'Special']:
            continue  # Skip unsupported types

        episodes = anime.get('episodes') or 12
        status = anime.get('status')
        if status == 'Currently Airing':
            status = 'Airing'
        elif status == 'Finished Airing':
            status = 'Completed'
        elif status == 'Not yet aired':
            status = 'Upcoming'
        else:
            status = 'Upcoming'

        start_date = anime.get('aired', {}).get('from')
        end_date = anime.get('aired', {}).get('to')
        airing_start = f"'{start_date[:10]}'" if start_date else 'NULL'
        airing_end = f"'{end_date[:10]}'" if end_date else 'NULL'

        score = anime.get('score') or 0
        rating = map_score_to_rating(score)
        synopsis = sanitize(anime.get('synopsis') or '')
        studio_id = 1  # Customize or map dynamically
        tag_id = 1     # Same here
        image_url = anime.get('images', {}).get('jpg', {}).get('image_url', '')
        image_url = sanitize(image_url)

        insert_values.append(
            f"('{title}', '{type_}', {episodes}, '{status}', {airing_start}, {airing_end}, '{rating}', '{synopsis}', {studio_id}, {tag_id}, '{image_url}')"
        )

# Final output
with open("anime_insert.sql", "w", encoding="utf-8") as file:
    file.write("INSERT INTO anime (title, type, episodes, status, airing_start, airing_end, rating, synopsis, StudioID, TagID, image_url)\nVALUES\n")
    file.write(",\n".join(insert_values) + ";")

print("Done! All insert values saved in a single statement inside anime_insert.sql")
