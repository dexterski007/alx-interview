#!/usr/bin/node
const request = require('request');
const filmid = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api';

request(`${url}/films/${filmid}/`, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const chars = JSON.parse(body).characters;
    const chararr = chars.map(
      charurl => new Promise((resolve, reject) => {
        request(charurl, (errorpr, resppr, bodypr) => {
          if (errorpr) {
            reject(errorpr);
          }
          if (resppr.statusCode === 200) {
            resolve(JSON.parse(bodypr).name);
          }
        });
      })
    );
    Promise.all(chararr)
      .then(names => console.log(names.join('\n')))
      .catch(errors => console.log(errors));
  }
});
