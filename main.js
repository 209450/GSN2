const reviewsMetadata = require('./mard_reviews.json');
const fs = require('fs');

const allTags = [
  'rock',             'pop',               'alternative',
  'indie',            'electronic',        'female vocalists',
  'favorites',        'love',              'dance',
  '00s',              'alternative rock',  'jazz',
  'beautiful',        'singer-songwriter', 'metal',
  'chillout',         'male vocalists',    'awesome',
  'classic rock',     'soul',              'indie rock',
  'mellow',           'electronica',       '80s',
  'folk',             'british',           '90s',
  'chill',            'american',          'instrumental',
  'punk',             'oldies',            'seen live',
  'blues',            'hard rock',         'cool',
  'favorite',         'ambient',           'acoustic',
  'experimental',     'favourites',        'female vocalist',
  'guitar',           'hip-hop',           '70s',
  'party',            'country',           'easy listening',
  'sexy',             'catchy',            'funk',
  'favourite',        'electro',           'heavy metal',
  'progressive rock', '60s',               'fun',
  'rnb',              'indie pop',         'soundtrack',
  'loved',            'sad',               'house',
  'favorite songs',   'happy',             'punk rock',
  'piano',            'psychedelic',       'hip hop',
  'male vocalist',    'classic',           'pop rock',
  'downtempo',        'trance',            'melancholy',
  'female',           'amazing',           'hardcore',
  'rap',              'lounge',            'cover',
  'techno',           'reggae',            'nice',
  'relax',            'new wave',          'relaxing',
  'upbeat',           'good',              'romantic',
  'epic',             'ballad',            'melancholic',
  'death metal',      'summer',            'usa',
];

const onlyReview = reviewsMetadata.map(record => record.reviewText);
const reviewsWithTags = onlyReview
  .map(rview => rview.toLowerCase().split('.'))
  .map(descriptions => descriptions
    .map(description => description.trim())
    .filter(description => description.length > 0))
  .map(descriptions => descriptions
    .filter(description => description.includes(...allTags)))
  .filter(descriptions => descriptions.length > 0)
  .flat()

const createRegularCorpus = () => {
  fs.writeFileSync('data.txt', reviewsWithTags.join('\n'));
}

const createSpacyCorpus = () => {
  const tagReview = {};
  for(const review of reviewsWithTags) {
    allTags.forEach(tag => {
      if(review.includes(tag)) {
        if(tag in tagReview) {
          tagReview[tag].push(review)
        } else {
          tagReview[tag] = [review];
        }
      }
    })
  }
  
  let spacy_corpus = `
  categories:
  - songs
  conversations:
  `;
  for(const [tag, reviews] of Object.entries(tagReview)) {
    spacy_corpus += `- - ${tag}\n`;
    reviews.forEach(review => {
      spacy_corpus += `  - ${review.replace(/[^\w\s]/gi, '')}\n`
    });
  }
  fs.writeFileSync('song-tags-reviews.yml', spacy_corpus);
}

createRegularCorpus();