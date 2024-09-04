var request = require('request');
const filmid = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${filmid}`;

request(url, (error, response, body) => {
  const data = JSON.parse(body);
  const chars = data.characters;
  chars.forEach(char => {
    request(char, (error, response, body) => {
      const chardata = JSON.parse(body);
      console.log(chardata.name)
    })
  });
});
