#!/usr/bin/node
const request = require('request');
const filmid = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${filmid}`;

request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const data = JSON.parse(body);
    const chars = data.characters;
    chars.forEach(char => {
      request(char, (error, response, body) => {
        if (!error && response.statusCode === 200) {
          const chardata = JSON.parse(body);
          console.log(chardata.name);
        }
      });
    });
  }
});
