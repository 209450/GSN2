import random

def getDescriptionFromTags(tags):
    result = ''
    for tag in tags:
        tagDescription = random.choice(musicTypesDescriptions[tag])
        if len(result) == 0:
            result = tagDescription
        else:
            result += '. ' + tagDescription
    return result

musicTypesDescriptions = {
    "rock": [
      "The sound of rock is traditionally centered on the amplified electric guitar",
      "Good guitar sounds",
      "Energetic songs with guitar sounds"
    ],
    "pop": [
        "Songs have good rhythm",
        "Easy to remember lyrics",
        "Catchy melody"
    ],
    "alternative": [
        "Category of rock music",
        "Is greatly in terms of its sound, social context and regional roots",
        "There is many different variations"
    ],
    "indie": [
        "Is produced independently from commercial record labels or their subsidiaries",
        "Production that may include an autonomous, do-it-yourself approach to recording and publishing",
        "Interesting approach to the music making"
    ],
    "electronic": [
        "Is made using electronic instruments",
        "Uses electronic equipment to make music ",
        "Typically not organic-sounding"
    ],
    "female vocalists": [
        "Women singing on stage",
        "Can by done by single vocalist or in band",
        "Pleasant to listen"
    ],
    "favorites": [
        "Most frequently listened to",
        "Contains specific elements",
        "Gives joy"
    ],
    "Love": [
        "Often tells about romance",
        "Nice to hear when sadness comes",
        "Hard do describe it in one way"
    ],
    "dance": [
        "Very catchy lyrics",
        "Dance rhythm",
        "The best one to dance to"
    ],
    "00s": [
        "Dominated by the garage rock revival",
        "Very catchy and dancy",
        "Interesting videoclips to songs"

    ],
    "alternative rock": [
        "Built on distorted guitars and rooted in generational discontent",
        "Pop music style",
        "Nice electric guitars tones"
    ],
    "jazz": [
        "Is a distinctively American style of music that developed in the early decades of the 20th century",
        "Its roots include many Afro-American folk music traditions and blues",
        "Also has been influenced by, traditional classical music and popular music"
    ],
    "beautiful": [
        "The ones that is loved the most by listener",
        "Tells different stories in lyrics",
        "We like to come back to it"
    ],
    "singer-songwriter": [
        "Do both things: sings and writes songs",
        "Often songs contains huge emotional message",
        "Hard to do but worth doing it"
    ],
    "metal": [
        "The most commercially successful genre of rock music",
        "Genre of rock music",
        "Driven by the aggressive sounds of the distorted electric guitar"
    ],
    "chillout": [
        "Great to sit and just listen to it",
        "Beautiful songs and lyrics",
        "Nice to hear"
    ],
    "male vocalists": [
        "Men singing on stage",
        "Can by done by single vocalist or in band",
        "Mostly done by barytone voiced men"
    ],
    "Awesome": [
        "The best one for us to listen",
        "Can be dancy but also can be calm",
        "You can relax when listen to it"
    ],
    "classic rock": [
        "Is a radio format which developed from the album-oriented rock",
        "Is a genre of music that combines a particular guitar-driven rock sound with a particular era of time.",
        "Ones of the most popular bands is The Beatles and Rolling Stones"
    ],
    "soul": [
        "Is a return to African American music's roots—gospel and blues",
        "is characterized by a wide range of emotions.",
        "The artists use various sounds from gentle, smooth to harsh and raspy to convey their messages"
    ],
    "indie rock": [
        "The influences and styles of the artists have been extremely diverse",
        "Includes punk, psychedelia, post-punk and country.",
        "A genre of alternative rock"
    ],
    "Mellow": [
        "Soft rock, and adult contemporary tunes"
    ],
    "electronica": [
        "Similar to eloctronic",
        "Includes electronic instruments",
        "Interesting sounding"
    ],
    "80s": [
        "Electronic dance music and new wave",
        "Soft rock, glam metal, thrash metal, shred guitar characterized by heavy distortion, pinch harmonics",
        "Became very popular"
    ],
    "folk": [
        "Created only by a local people of region",
        "Type of traditional and generally rural music that originally was passed down through families",
        "Folk music, like folk literature, lives in oral tradition; it is learned through hearing rather than reading"
    ],
    "british": [
        "Popular music in Britan",
        "Includes folk music, jazz, rapping/hip hop, pop and rock music.",
        "Mostly common in Great Kingdom of Britain"
    ],
    "90s": [
        "Popular music in the 1990s",
        "Features a fusion of horn-based music with rock music elements.",
        "Continuation of teen pop and dance-pop trends"

    ],
    "chill": [
        "Is a loosely defined form of popular music",
        "Characterized by slow tempos and relaxed moods",
        "Some of the genres of chill include downtempo, classical, dance"
    ],
    "american": [
        "Is characterized by the use of syncopation and asymmetrical rhythms, long, irregular melodies",
        "Reflects the wide open geography of the American landscape",
        "Reflects sense of personal freedom characteristic of American life"
    ],
    "instrumental": [
        "Created only by using instruments",
        "Commonly spotted in soundtracks of films or games",
        "Often can be classified to classic music"
    ],
    "punk": [
        "Typically produced short, fast-paced songs with hard-edged melodies and singing styles,",
        "Often shouted political, anti-establishment lyrics",
        "Hard-edged melodies and singing styles"
    ],
    "oldies": [
        "Musical genres such as pop music, rock and roll, doo-wop, surf music",
        "Any piece of music that was released at least 15 years ago at bare minimum",
        "Something that makes people feel old really quick"
    ],
    "seen live": [
        "You can see it live on TV",
        "No place on error when You are performing it",
        "Interesting to hear"
    ],
    "blues": [
        "Is essentially a vocal form",
        "Blues songs are lyrical rather than narrative",
        "Blues singers are expressing feelings rather than telling stories"
    ],
    "hard rock": [
        "Is a loosely defined subgenre of rock music",
        "Typified by a heavy use of aggressive vocals, distorted electric guitars, bass guitar",
        "It began in the mid-1960s with the garage, psychedelic and blues rock movements"
    ],
    "cool": [
        "The best one to listen when "
    ],
    "Favorite": [
        "It is my favourite song",
        "I like this song soo much",
        "I love this song"
    ],
    "ambient": [
        "Is a genre of music that emphasizes tone and atmosphere",
        "Do not emphasizes traditional musical structure or rhythm",
        "A form of instrumental music"
    ],
    "acoustic": [
        "Music that uses instruments that produce sound through acoustic means",
        "Is opposided to electric or electronic music",
        "It stood in contrast to various other types of music in various eras"
    ],
    "experimental": [
        "Is a general label for any music that pushes existing boundaries and genre definitions",
        "Elements of experimental music include indeterminate music",
        "Composer introduces the elements of chance or unpredictability with regard to either the composition or its performance"
    ],
    "Favourites": [
        "My favourite songs",
        "I like these songs soo much",
        "I love these song"
    ],
    "female vocalist": [
        "Women singing on stage",
        "Can by done by single vocalist",
        "Pleasant to listen"
    ],
    "guitar": [
        "Guitars can be sweet, warm, bassy, melodious, harmonious,  and many other adjectives.",
        "Can be done on any kind of guitar",
        "Easy to learn"
    ],
    "Hip-Hop": [
        "Musical genre consisting of a stylized rhythmic music originally created by DJs",
        "Widely considered a synonym for rap music",
        "Rap is one of the most distinctive features of hip-hop"
    ],
    "70s": [
        "The top tunes from the '70s feel incredibly diverse, both in sound and content",
        "There are dance-oriented topics, but also ideas about a better world",
        "Golden era for vinyl records"

    ],
    "party": [
        "You can dance to it",
        "Nice to hear on a parties",
        "Easy and simple lyrics"
    ],
    "country": [
        "Main focus on the Country music has always been the guitar and voice",
        "Some of the topics that influence the composition of these songs include love",
        "Made mostly in USA"
    ],
    "easy listening": [
        "Easy to listen",
        "Nice to listen",
        "Enjoyable"
    ],
    "sexy": [
        "Has part of romance",
        "Mostly spotted in clubs",
        "Has a lot of female voices"
    ],
    "catchy": [
        "Has catchy lyrics",
        "Has catchy rhythm",
        "Can by done by any type of instrument"
    ],
    "funk": [
        "Ss a style of popular music that emerged in the late 1960s",
        "Outgrowth of rhythm and blues",
        "Funk features strong bass lines, or music lines played by low-pitched instruments "
    ],
    "favourite": [
        "Such a good song",
        "This song is amazing",
        "The best song ever"
    ],
    "electro": [
        "Electronic music is music that employs electronic musical instruments, digital instruments",
        "It includes both music made using electronic and electromechanical means",
        "Sometimes refferd to as electroacoustic music"
    ],
    "heavy metal": [
        "Genre of rock music",
        "Includes a group of related styles that are intense, virtuosic, and powerful",
        "Driven by the aggressive sounds of the distorted electric guitar"
    ],
    "Progressive rock": [
        "Can be named also as prog rock",
        "Subgenre of rock music that emphasizes ambitious compositions",
        "The first progressive rock bands formed in the late 1960s"
    ],
    "60s": [
        "Dominated by jazz, pop, and folk music",
        "Funk and soul music rising in popularity",
        "Nice to listen"
    ],
    "fun": [
        "I am always laughing while listening this song",
        "This song is hilarious",
        "Super funny song"
    ],
    "rnb": [
        "Stands for Rhythm and Blues",
        "Music that is rhythmic and has the soulful achings of the blues",
        "Has morphed into a crossbreed of genres, one that has allowed space"
    ],
    "indie pop": [
        "Is a music genre and subculture that combines guitar pop with DIY ethic",
        "Is more melodic, less abrasive, and relatively angst-free compared to indie rock",
        "Independently released music is not directly financially dependent on any of the four major labels"
    ],
    "Soundtrack": [
        "Used in films or games",
        "Can contain elements of every music genre",
        "One of the best known compositors of soundtracks is Hans Zimmer"
    ],
    "loved": [],
    "sad": [
        "Makes you sad",
        "Often listen to when You are sad",
        "Calm and with an emotional charge"
    ],
    "House": [
        "is a genre of electronic dance music characterized by a repetitive four-on-the-floor",
        "typical tempo of 120 to 130 beats per minute",
        "Often used in clubs or on parties"
    ],
    "favorite songs": [
        "Most frequently listened songs to",
        "Contains your favourite songs",
        "Gives incredible pleasure"
    ],
    "happy": [
        "Makes You happy",
        "Remainds of happier times",
        "Joyful and nice to listen"
    ],
    "punk rock": [
        "Punk bands rejected the perceived excesses of mainstream 1970s rock",
        "Short, fast-paced songs with hard-edged melodies and singing styles, stripped-down instrumentation",
        "Often shouted political, anti-establishment lyrics"
    ],
    "piano": [
        "Main instrument is piano",
        "Can be accompanied with different instruments",
        "Can be accompanied with Singers"
    ],
    "psychedelic": [
        "Style of rock music popular in the late 1960s that was largely inspired by hallucinogens",
        "Songs often have more disjunctive song structures, key and time signature changes and modal melodies",
        "Mostly done under the influence mind-expanding drugs"
    ],
    "hip hop": [
        "Musical genre consisting of a stylized rhythmic music originally created by DJs",
        "Widely considered a synonym for rap music",
        "Rap is one of the most distinctive features of hip-hop"
    ],
    "male vocalist": [
        "Done by male",
        "Can be a single male performance or in a band"
        "Mostly male voices can be heard"
    ],
    "classic": [
        "Very general term which normally refers to the standard music of countries in the western world",
        "Music that has been composed by musicians who are trained in the art of writing music",
        "It is mainly homophonic—melody above chordal accompaniment"
    ],
    "pop rock": [
        "Is rock music with a greater emphasis on professional songwriting and recording craft",
        "Less emphasis on attitude",
        "The detractors of pop rock often deride it as a slick, commercial product, less authentic than rock music."
    ],
    "downtempo": [
        "Sometimes used synonymously with trip hop",
        "Is a genre of electronic music similar to ambient music",
        "with a greater emphasis on beats and a less earthy sound than trip hop"
    ],
    "trance": [
        "Is characterized by a tempo lying between 135–150 bpm (BPM)",
        "Repeating melodic phrases",
        "musical form that distinctly builds tension and elements throughout a track"
    ],
    "melancholy": [
        "It is more than sadness",
        "It is a nuanced mix of emotions that seems steeped in articulacy",
        "Arguably melancholy is as much a driving force to songwriting as any idea or emotion"
    ],
    "female": [
        "Done by female",
        "Can be a single female performance or in a band"
        "Mostly female voices can be heard"
    ],
    "amazing": [
        "Amazing to listen to",
        "Amazing sounding of instruments",
        "Amazing lyrics and singing"
    ],
    "hardcore": [
        "Is a punk rock music genre and subculture that originated in the late 1970s",
        "It is generally faster, harder, and more aggressive than other forms of punk rock",
        "Hardcore has spawned the straight edge movement and its associated sub-movements, hardline and youth crew"
    ],
    "rap": [
        "Musical style in which rhythmic and/or rhyming speech is chanted to musical accompaniment",
        "Originated in African American communities in New York City",
        "If you rap on something or rap it, you hit it with a series of quick blows"
    ],
    "lounge": [
        "Type of easy listening music popular in the 1950s and 1960s",
        "It may be meant to evoke in the listeners the feeling of being in a specific place"
        "Consists of the baby Grand Piano surrounded by more microphones and several percussion instruments"
    ],
    "cover": [
        "Is a new performance or recording by someone other than the original performer or composer of a song.",
        "Can be done either by voice or using instrument, or by both in the same time",
        "Great opportunity for new artist to show theirs skills"
    ],
    "techno": [
        "Is a genre of electronic dance music",
        "Predominantly characterized by a repetitive four on the floor beat",
        "Generally produced for use in a continuous DJ set"
    ],
    "reggae": [
        "Reggae is based on ska, an earlier form of Jamaican popular music",
        "Employs a heavy four-beat rhythm driven by drums, bass guitar, electric guitar",
        "Has its own special music instrument - scrapter"
    ],
    "nice": [
        "Nice to listen",
        "Nice sounding of instruments"
        "Nice lyrics and rhythm"
    ],
    "relax": [
        "You can relax when listening to it",
        "Nice to listen when having a lnog bath",
        "Different types of music for everybody"
    ],
    "new wave": [
        "New wave is a broad music genre that encompasses numerous pop and rock styles from the late 1970s and the 1980s.",
        "This trend was characterized by a more refined and richer comparison to punk rock music.",
        "The first new wave song to chart in the US was “Cars” by Gary Numan in 1980."
    ],
    "relaxing": [
        "Relaxes you when you listen to it",
        "Nice to listen when under the blanket with cup of tea"
        "You can easily fall asleep"
    ],
    "upbeat": [
        "Fast-tempo music",
        "Might make you want to dance all night or sing out loud",
        "Tempo is measured in BPMs or beats per minute"
    ],
    "good": [
        "Good to listen",
        "Can be any genere of music",
        "Depends on personal preferences"
    ],
    "romantic": [
        "Freedom of form and design",
        "Song-like melodies (lyrical), as well as many chromatic harmonies and discords",
        "Dramatic contrasts of dynamics and pitch."
    ],
    "epic": [
        "Intresting to listen or make",
        "Can by done by a lot of instruments",
        "Dosent have one specific feature"
    ],
    "Ballad": [
        "Tells story",
        "Often lyrics is writen based on the book",
        "Has elements of romance"
    ],
    "melancholic": [
        "Sends back to the land of memories",
        "Reminds about the time that had passed",
        "Often played in rainy days"
    ],
    "death metal": [
        "Heavily distorted and low tuned guitars, played with techniques such as palm muting and tremolo picking.",
        "The percussion is usually aggressive and powerful.",
        "Is known for its abrupt tempo, key, and time signature changes"
    ],
    "summer": [
        "Reminds of wacations and journeys",
        "It can be classified to chillout music",
        "Best one to play when You have a grill"
    ],
    "USA": [
        "A lot of country music",
        "A big part of it is hip-hop",
        "Sometimes hard to understand lyrics"
    ],
    "2000s": [
        "The most popular song is 'Hanging by a Moment' by Lifehouse",
        "Same as 00s music",
        "Dancy melody catchy lyrics"
    ],
    "emo": [
        "Is a subgenre of punk rock, indie rock, and alternative rock music",
        "Defined by its heavy emotional expression",
        "Emo is part of the post-hardcore band scene, with artists delving into songs with more substance and feeling"
    ],
    "UK": [
        "Mostly made in Britain",
        "Similar to british music",
        "You can hear it in british pubs"
    ],
}