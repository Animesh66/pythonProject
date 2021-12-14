import random

songs_list = [
    'Onra - Tfbs Intro',
    'Malik Abdul Rahmaan - Mailbox Money [Nipsey Flip]',
    'Nekolai - No No',
    'Paal Singh - Huffr',
    'Middleeast - Devil In You',
    'Mr. Hong - Roses (Feat. Dvdkm And Christine Kim)',
    'Cam Matthews - Lykme',
    'Ercentius - Awake (%Ercentius Footworkout)',
    'Low Key - The Gloves',
    'Co$Mo - I Want To Be Loved.',
]

new_list = []
while songs_list:
    input("Enter your choice:")
    current_song = random.choice(songs_list)
    new_list.append(current_song)
    print(current_song)
    songs_list.remove(current_song)
    if len(songs_list) == 0:
        songs_list = new_list[:]



