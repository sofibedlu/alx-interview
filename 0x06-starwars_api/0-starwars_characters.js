#!/usr/bin/node

const request = require('request');

function getCharacters (movieId) {
  const url = `https://swapi.dev/api/films/${movieId}/`;

  request(url, { json: true }, (error, response, filmData) => {
    if (error) {
      console.error('Error fetching movie data:', error);
      return;
    }

    const characterUrls = filmData.characters;
    const characterPromises = characterUrls.map((characterUrl) =>
      new Promise((resolve, reject) => {
        request(characterUrl, { json: true }, (error, response, characterData) => {
          if (error) {
            reject(error);
          } else {
            resolve(characterData);
          }
        });
      })
    );

    Promise.all(characterPromises)
      .then((characters) => {
        characters.forEach((characterData) => {
          console.log(characterData.name);
        });
      })
      .catch((error) => {
        console.error('Error fetching character data:', error);
      });
  });
}

const movieId = process.argv[2];
if (!movieId) {
  console.log('Please provide the Movie ID as a command line argument.');
  console.log('Example usage: node script.js 3');
} else {
  getCharacters(movieId);
}
